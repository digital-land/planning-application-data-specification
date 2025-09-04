from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

from models import (
    ApplicationDef,
    ComponentDef,
    ComponentInstance,
    FieldDef,
    FieldInstance,
    ModuleDef,
)
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter

# ---------- Traversal helpers ----------


def walk_component_paths(
    node: Any, prefix: List[str]
) -> List[Tuple[List[str], FieldInstance]]:
    """
    Return list of (path_names, field) where path_names is the chain of component names
    leading to the field (e.g. ['agent', 'person', 'first-name'] but we keep field separate).
    """
    rows: List[Tuple[List[str], FieldInstance]] = []
    # node can be a ComponentInstance, ComponentDef, or unexpectedly a FieldInstance
    if isinstance(node, ComponentInstance):
        comp_def = node.component
        ref_field = node.referenced_by_field  # FieldInstance
        base = ref_field.original.name
        if ref_field.original.cardinality == "n":
            base += "[]"
    elif isinstance(node, ComponentDef):
        comp_def = node
        base = comp_def.name
    elif isinstance(node, FieldInstance):
        # reached a field instance directly - return it as a leaf
        rows.append((prefix, node))
        return rows
    else:
        # unknown node type
        return rows

    # comp_def.items preserves author-specified order; each item is FieldInstance or ComponentInstance
    for item in getattr(comp_def, "items", []):
        if isinstance(item, FieldInstance):
            rows.append((prefix + [base], item))
        else:
            rows.extend(walk_component_paths(item, prefix + [base]))
    return rows


def flatten_module_to_rows(mod: ModuleDef) -> List[Tuple[List[str], FieldInstance]]:
    """
    Produce rows for a module. For each field:
      - path is [component1, component2, ..., field_name] (module name goes in 'top-level').
      - we return (path_without_fieldname_components, field) so caller can split into fieldN cols.
    """
    rows: List[Tuple[List[str], FieldDef]] = []
    # module-level items may include fields and embedded components; preserve order
    for item in mod.items:
        if isinstance(item, FieldInstance):
            # simple module-level field instance: no component path
            rows.append(([], item))
        else:
            # item may be ComponentDef or ComponentInstance; return its component path
            for comp_path, f in walk_component_paths(item, []):
                rows.append((comp_path, f))
    return rows


# ---------- Excel writing ----------


def format_field_name(f: Any) -> str:
    # Accept either FieldDef or FieldInstance
    if isinstance(f, FieldInstance):
        orig = f.original
        name = f.overrides.get("name") or orig.name
        cardinality = f.overrides.get("cardinality") or orig.cardinality
    else:
        name = getattr(f, "name", "")
        cardinality = getattr(f, "cardinality", None)
    if cardinality == "n":
        name += "[]"
    return name


def requirement_label(required: bool) -> str:
    return "MUST" if required else "MAY"


def make_row(application, app_desc, top, top_desc, field_chain, f: FieldInstance):
    orig = f.original
    overrides = f.overrides
    requirement_level = overrides.get("required", orig.required)
    return {
        "application": application,
        "application_description": app_desc,
        "top_level": top,
        "top_description": top_desc,
        "field_chain": field_chain,
        "description": overrides.get("description", orig.description),
        "datatype": getattr(orig, "datatype", "string"),
        "requirement": requirement_label(requirement_level),
    }


def auto_width(ws):
    widths = defaultdict(int)
    for row in ws.iter_rows(values_only=True):
        for i, val in enumerate(row, start=1):
            if val is None:
                continue
            widths[i] = max(widths[i], len(str(val)))
    for i, w in widths.items():
        ws.column_dimensions[get_column_letter(i)].width = min(72, w + 2)


def write_application_excel(
    app: ApplicationDef, modules_index: Dict[str, ModuleDef], out_dir: Path
) -> Path:
    """
    Writes one XLSX with columns:
      application, application-description, top-level, field1..N, description, datatype, requirement
    Merges:
      - application/application-description across all rows
      - top-level across its contiguous block
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Specification"

    app_ref = app.application
    app_desc = app.description

    # Build flat rows
    flat_rows: List[Dict[str, Any]] = []

    # 1) Application-level items (fields and possibly embedded components)
    for item in app.items:
        if isinstance(item, FieldDef):
            top = item.ref
            top_desc = item.description
            field_chain = [item.ref]
            flat_rows.append(
                make_row(app_ref, app_desc, top, top_desc, field_chain, item)
            )
        elif isinstance(item, ComponentInstance):
            # embedded component at application level
            for comp_path, f in walk_component_paths(item, []):
                top = item.referenced_by_field.original.name
                top_desc = (
                    item.referenced_by_field.overrides.get("description")
                    or item.referenced_by_field.original.description
                )
                subpath = (
                    comp_path[1:] if comp_path and comp_path[0] == top else comp_path
                )
                field_name = format_field_name(f)
                field_chain = subpath + [field_name]
                flat_rows.append(
                    make_row(app_ref, app_desc, top, top_desc, field_chain, f)
                )
        else:
            # defensive: skip unknown item types
            continue

    # 2) Modules

    for mod in app.modules:
        if not mod:
            continue

        # Produce rows for this module
        mod_rows = flatten_module_to_rows(mod)

        # If a module has zero fields/components, still emit a placeholder row
        if not mod_rows:
            flat_rows.append(
                dict(
                    application=app_ref,
                    application_description=app_desc,
                    top_level=mod.name,
                    top_description=mod.description,
                    field_chain=[""],  # no field
                    description="",
                    datatype="",
                    requirement="",
                )
            )
        else:
            for comp_path, f in mod_rows:
                # top-level is the module name
                top = mod.name
                # field_chain is the component path + field name
                field_chain = comp_path + [format_field_name(f)]
                flat_rows.append(
                    make_row(app_ref, app_desc, top, mod.description, field_chain, f)
                )

    # If there are no rows, add a single empty placeholder so headers still render
    if not flat_rows:
        flat_rows.append(
            dict(
                application=app_ref or "",
                application_description=app_desc or "",
                top_level="",
                top_description="",
                field_chain=[""],
                description="",
                datatype="",
                requirement="",
            )
        )

    # Figure out max depth of field_chain to create field1..N columns
    max_depth = max((len(r["field_chain"]) for r in flat_rows), default=1)

    # Header
    header = [
        "application",
        "application-description",
        "top-level",
        "top-level-description",
    ]
    header += [f"field{i}" for i in range(1, max_depth + 1)]
    header += ["description", "datatype", "requirement"]
    ws.append(header)
    for c in ws[1]:
        c.font = Font(bold=True)
        c.alignment = Alignment(wrap_text=True, vertical="top")

    # Write rows while remembering blocks for merging
    start_row_for_app = ws.max_row + 1
    # We also merge top-level blocks: whenever top_level value changes, close the previous block
    current_top = None
    top_block_start = None

    def close_top_block(end_row: int):
        if top_block_start is not None and end_row >= top_block_start:
            # Merge the 'top-level' column (3rd column) for the block
            ws.merge_cells(
                start_row=top_block_start, start_column=3, end_row=end_row, end_column=3
            )
            ws.cell(row=top_block_start, column=3).alignment = Alignment(
                vertical="top", wrap_text=True
            )
            # Merge the 'top-level-description' column (4th column) for the block
            ws.merge_cells(
                start_row=top_block_start, start_column=4, end_row=end_row, end_column=4
            )
            ws.cell(row=top_block_start, column=4).alignment = Alignment(
                vertical="top", wrap_text=True
            )

    for row in flat_rows:
        # flush/rotate top-level block if the value changes
        if row["top_level"] != current_top:
            # close previous block
            prev_end = ws.max_row
            close_top_block(prev_end)
            # start new block
            current_top = row["top_level"]
            top_block_start = prev_end + 1

        # Expand field_chain into field columns with padding
        chain = row["field_chain"]
        padded = chain + [""] * (max_depth - len(chain))

        ws.append(
            [
                row["application"],
                row["application_description"],
                row["top_level"],
                row["top_description"],
                *padded,
                row["description"],
                row["datatype"],
                row["requirement"],
            ]
        )

    # Close last top-level block
    close_top_block(ws.max_row)

    # Merge application/application-description across all rows
    end_row_for_app = ws.max_row
    if end_row_for_app >= start_row_for_app:
        ws.merge_cells(
            start_row=start_row_for_app,
            start_column=1,
            end_row=end_row_for_app,
            end_column=1,
        )
        ws.merge_cells(
            start_row=start_row_for_app,
            start_column=2,
            end_row=end_row_for_app,
            end_column=2,
        )
        ws.cell(row=start_row_for_app, column=1).alignment = Alignment(
            vertical="top", wrap_text=True
        )
        ws.cell(row=start_row_for_app, column=2).alignment = Alignment(
            vertical="top", wrap_text=True
        )

    # Formatting
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")

    auto_width(ws)

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{app_ref}.xlsx"
    wb.save(out_path)
    return out_path


# ---------- Run for all applications ----------
if __name__ == "__main__":
    from loader import load_specification_model

    model = load_specification_model()
    output_dir = Path("tmp/app_specs")
    # for app in APPLICATIONS:
    #     path = write_application_excel(app, MODULES, output_dir)
    #     print("Wrote:", path)
    # test with a single one
    path = write_application_excel(
        model["applications"]["hh"], model["modules"], output_dir
    )
    print("Wrote:", path)
