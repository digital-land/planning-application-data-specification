from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable


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


def _normalise_application_types(values: Iterable[object]) -> list[str]:
    cleaned = []
    for value in values:
        if not isinstance(value, str):
            continue
        item = value.strip()
        if item:
            cleaned.append(item)
    return sorted(cleaned)


def _coerce_application_type_list(application: object) -> list[str] | None:
    if isinstance(application, str):
        if ";" in application:
            return _normalise_application_types(application.split(";"))
        return None

    if isinstance(application, (list, tuple, set)):
        return _normalise_application_types(application)

    return None


def _extract_module_ref(entry):
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


def _collect_single_application_module_refs(app_obj: dict, applications: dict) -> list[str]:
    collected = set()
    visited_apps = set()

    def collect_from_app(current_app):
        mods = current_app.get("modules", None)
        if mods is None:
            mods = current_app.get("module", [])
        mods_iter = list(mods.values()) if isinstance(mods, dict) else (mods or [])

        for module_entry in mods_iter:
            module_ref = _extract_module_ref(module_entry)
            if isinstance(module_ref, str) and module_ref:
                collected.add(module_ref)

        extends = current_app.get("extends")
        if not extends:
            return

        parent_refs = extends if isinstance(extends, list) else [extends]
        for parent_ref in parent_refs:
            if not isinstance(parent_ref, str) or not parent_ref:
                continue
            if parent_ref in visited_apps:
                continue
            visited_apps.add(parent_ref)
            parent_app = applications.get(parent_ref)
            if parent_app:
                collect_from_app(parent_app)

    collect_from_app(app_obj)
    return sorted(collected)


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

    canonical_ref = ";".join(application_types)
    combo_row = None
    for row in _read_combined_application_rows(specification):
        raw_application_types = row.get("application-types") or ""
        candidate_types = _normalise_application_types(raw_application_types.split(";"))
        if candidate_types and ";".join(candidate_types) == canonical_ref:
            combo_row = row
            break

    if combo_row is None:
        raise KeyError(f"Unknown combined application type '{canonical_ref}'")

    if not (combo_row.get("start-date") or "").strip():
        raise ValueError(
            f"Combined application type '{canonical_ref}' is recognised but not yet active"
        )

    module_refs = set()
    for application_type in application_types:
        app_obj = applications.get(application_type)
        if not app_obj:
            raise KeyError(f"Unknown application type '{application_type}'")
        module_refs.update(_collect_single_application_module_refs(app_obj, applications))

    return {
        "application-types": application_types,
        "name": combo_row.get("name", canonical_ref) or canonical_ref,
        "description": combo_row.get("description", "") or "",
        "modules": [{"module": module_ref} for module_ref in sorted(module_refs)],
    }


def get_application_module_refs(application: object | str | list[str], specification: dict) -> list:
    """
    Given an application object, application ref string, or list of application refs,
    return a deduplicated, alphabetical list of module reference strings.
    """
    applications = specification.get("application", {}) or {}
    app_obj = resolve_application(application, specification)
    if not app_obj:
        return []

    if "application-types" in app_obj and "application" not in app_obj:
        return [
            _extract_module_ref(module_entry)
            for module_entry in app_obj.get("modules", [])
            if _extract_module_ref(module_entry)
        ]

    return _collect_single_application_module_refs(app_obj, applications)
