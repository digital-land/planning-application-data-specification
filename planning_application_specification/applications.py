from __future__ import annotations

import csv
from pathlib import Path

from .application_types import canonical_application_ref, normalise_application_types


def _resolve_repo_root_from_specification(specification: dict) -> Path:
    root = specification.get("__root_path__")
    if isinstance(root, Path):
        return root
    if isinstance(root, str) and root:
        return Path(root)

    for candidate in [Path.cwd(), *Path.cwd().parents]:
        if (candidate / "specification").exists():
            return candidate

    raise FileNotFoundError("Could not detect the repository root from specification")


def _combined_application_types_path(specification: dict) -> Path:
    return (
        _resolve_repo_root_from_specification(specification)
        / "specification"
        / "combined-application-types.csv"
    )


def _read_combined_application_rows(specification: dict) -> list[dict]:
    csv_path = _combined_application_types_path(specification)
    if not csv_path.exists():
        return []

    with csv_path.open(newline="", encoding="utf-8") as csvfile:
        return list(csv.DictReader(csvfile))


def get_active_combined_application_refs(specification: dict) -> set[str]:
    active_refs = set()
    for row in _read_combined_application_rows(specification):
        if not (row.get("start-date") or "").strip():
            continue
        canonical_ref = canonical_application_ref(row.get("application-types"))
        if canonical_ref:
            active_refs.add(canonical_ref)
    return active_refs


def _coerce_application_type_list(application: object) -> list[str] | None:
    if isinstance(application, str):
        if ";" in application:
            return list(normalise_application_types(application))
        return None

    if isinstance(application, (list, tuple, set)):
        return list(normalise_application_types(application))

    return None


def _extract_module_ref(entry) -> str | None:
    if isinstance(entry, str):
        return entry
    if isinstance(entry, dict):
        if "module" in entry:
            return _extract_module_ref(entry["module"])
        for value in entry.values():
            ref = _extract_module_ref(value)
            if ref:
                return ref
    return None


def _iter_module_entries(app_obj: dict) -> list:
    modules = app_obj.get("modules")
    if modules is None:
        modules = app_obj.get("module", [])
    if isinstance(modules, dict):
        return list(modules.values())
    return list(modules or [])


def _iter_parent_application_refs(app_obj: dict) -> list[str]:
    extends = app_obj.get("extends")
    if not extends:
        return []
    parent_refs = extends if isinstance(extends, list) else [extends]
    return [ref for ref in parent_refs if isinstance(ref, str) and ref]


def _collect_single_application_module_refs(app_obj: dict, applications: dict) -> list[str]:
    collected = set()
    visited_apps = set()

    def collect_from_app(current_app: dict) -> None:
        for module_entry in _iter_module_entries(current_app):
            module_ref = _extract_module_ref(module_entry)
            if module_ref:
                collected.add(module_ref)

        for parent_ref in _iter_parent_application_refs(current_app):
            if parent_ref in visited_apps:
                continue
            visited_apps.add(parent_ref)
            parent_app = applications.get(parent_ref)
            if parent_app:
                collect_from_app(parent_app)

    collect_from_app(app_obj)
    return sorted(collected)


def _find_combined_application_row(
    canonical_ref: str, specification: dict
) -> dict | None:
    for row in _read_combined_application_rows(specification):
        raw_application_types = row.get("application-types") or ""
        candidate_types = normalise_application_types(raw_application_types)
        if candidate_types and canonical_application_ref(candidate_types) == canonical_ref:
            return row
    return None


def _resolve_component_applications(
    application_types: list[str], applications: dict
) -> list[dict]:
    resolved = []
    for application_type in application_types:
        app_obj = applications.get(application_type)
        if not app_obj:
            raise KeyError(f"Unknown application type '{application_type}'")
        resolved.append(app_obj)
    return resolved


def _build_combined_application(
    application_types: list[str], combo_row: dict, applications: dict
) -> dict:
    module_refs = set()
    for app_obj in _resolve_component_applications(application_types, applications):
        module_refs.update(_collect_single_application_module_refs(app_obj, applications))

    canonical_ref = canonical_application_ref(application_types)
    return {
        "application": canonical_ref,
        "ref": canonical_ref,
        "application-types": application_types,
        "name": combo_row.get("name", canonical_ref) or canonical_ref,
        "description": combo_row.get("description", "") or "",
        "notes": combo_row.get("notes", "") or "",
        "entry-date": combo_row.get("entry-date"),
        "start-date": combo_row.get("start-date"),
        "end-date": combo_row.get("end-date"),
        "modules": [{"module": module_ref} for module_ref in sorted(module_refs)],
    }


def resolve_application(application: object | str | list[str], specification: dict) -> dict | None:
    applications = specification.get("application", {}) or {}

    application_types = _coerce_application_type_list(application)
    if application_types is None:
        if isinstance(application, str):
            return applications.get(application)
        if hasattr(application, "get") and callable(getattr(application, "get")):
            return application
        return None

    if not application_types:
        return None

    if len(application_types) == 1:
        return applications.get(application_types[0])

    canonical_ref = canonical_application_ref(application_types)
    combo_row = _find_combined_application_row(canonical_ref, specification)
    if combo_row is None:
        raise KeyError(f"Unknown combined application type '{canonical_ref}'")

    if not (combo_row.get("start-date") or "").strip():
        raise ValueError(
            f"Combined application type '{canonical_ref}' is recognised but not yet active"
        )

    return _build_combined_application(application_types, combo_row, applications)


def get_application_module_refs(application: object | str | list[str], specification: dict) -> list:
    """
    Given an application object, application ref string, or list of application refs,
    return a deduplicated, alphabetical list of module reference strings.
    """
    applications = specification.get("application", {}) or {}
    app_obj = resolve_application(application, specification)
    if not app_obj:
        return []

    return _collect_single_application_module_refs(app_obj, applications)
