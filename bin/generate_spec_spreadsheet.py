from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from models import (
    ApplicationDef,
    ComponentDef,
    ComponentInstance,
    FieldDef,
    FieldInstance,
    ModuleDef,
)
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, Side
from openpyxl.utils import get_column_letter
from utils import to_anchor

# ---------- Traversal helpers ----------


def is_node_applicable(node: Any, application_type: Optional[str] = None):

    if not application_type:
        # there is no application type specified so all apply
        return True

    if isinstance(node, FieldInstance):
        overrides = node.overrides
        field = node.original

    if isinstance(node, ComponentInstance):
        overrides = node.referenced_by_field.overrides
        field = node.referenced_by_field.original

    applies_if_conditions = overrides.get("applies-if")

    # assuming applies_if_conditions is dict with key "application-type"
    if applies_if_conditions:
        for k, app_type_cond in applies_if_conditions.items():
            if not k == "application-type":
                print("no an application-type condition")
            allowed_types = app_type_cond.get("in", [])

            if application_type not in allowed_types:
                print(f"for {field.ref}", application_type, " not ", app_type_cond)
                return False
    else:
        # if no applies-if condition then universally apply
        return True
    return True


def walk_component_paths(
    node: Any, prefix: List[str], application_type: Optional[str] = None
) -> List[Tuple[List[str], FieldInstance]]:
    """
    Return list of (path_names, field) where path_names is the chain of component names
    leading to the field (e.g. ['agent', 'person', 'first-name'] but we keep field separate).
    """
    rows: List[Tuple[List[str], FieldInstance]] = []
    # node can be a ComponentInstance, ComponentDef, or unexpectedly a FieldInstance
    if isinstance(node, ComponentInstance):
        # check if node is applicable to this application type (if provided)
        if is_node_applicable(node, application_type):
            comp_def = node.component
            ref_field = node.referenced_by_field  # FieldInstance
            base = ref_field.original.name
            if ref_field.original.cardinality == "n":
                base += "[]"

            # comp_def.items preserves author-specified order; each item is FieldInstance or ComponentInstance
            for item in getattr(comp_def, "items", []):
                level_prefix = prefix + [base]
                # handle leaf nodes
                if isinstance(item, FieldInstance):
                    if is_node_applicable(item, application_type):
                        rows.append((level_prefix, item))
                else:
                    # handle nested nodes
                    # do we need to repeat this check?
                    if is_node_applicable(item, application_type):
                        rows.extend(
                            walk_component_paths(item, level_prefix, application_type)
                        )
                    else:
                        # component instance not applicable for this application type
                        pass

    else:
        # unknown node type
        print("unknown node type")

    return rows


def flatten_module_to_rows(
    mod: ModuleDef, application_type: Optional[str] = None
) -> List[Tuple[List[str], FieldInstance]]:
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
            if is_node_applicable(item, application_type):
                rows.append(([], item))
        else:
            # item may be ComponentDef or ComponentInstance; return its component path
            for comp_path, f in walk_component_paths(item, [], application_type):
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


def make_row(
    application,
    app_desc,
    top,
    top_desc,
    field_chain,
    f: FieldInstance,
    incl_app_details: bool = True,
):
    orig = f.original
    overrides = f.overrides
    requirement_level = overrides.get("required", orig.required)
    row = {
        "top_level": top,
        "top_description": top_desc,
        "field_chain": field_chain,
        "description": overrides.get("description", orig.description),
        "datatype": getattr(orig, "datatype", "string"),
        "requirement": requirement_label(requirement_level),
    }

    if incl_app_details:
        row["application"] = application
        row["application_description"] = app_desc

    return row


def auto_width(ws):
    widths = defaultdict(int)
    for row in ws.iter_rows(values_only=True):
        for i, val in enumerate(row, start=1):
            if val is None:
                continue
            widths[i] = max(widths[i], len(str(val)))
    for i, w in widths.items():
        ws.column_dimensions[get_column_letter(i)].width = min(72, w + 2)


def format_header_row(ws):
    """
    Format the header row of the worksheet.
    ws = worksheet
    """
    thin_border = Side(border_style="thin", color="000000")
    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        cell.border = Border(bottom=thin_border)


def merge_cells_vertical(ws, col_num: int, row_start, row_end):
    ws.merge_cells(
        start_row=row_start, start_column=col_num, end_row=row_end, end_column=col_num
    )
    ws.cell(row=row_start, column=col_num).alignment = Alignment(
        vertical="top", wrap_text=True
    )


def set_cell_alignment(cell, alignment: Alignment):
    cell.alignment = alignment


def set_alignment_all(ws, vertical_alignment="top", start_from_row=2):
    cell_alignment = Alignment(wrap_text=True, vertical=vertical_alignment)
    for row in ws.iter_rows(min_row=start_from_row):
        for cell in row:
            set_cell_alignment(cell, cell_alignment)


def write_application_excel(
    app: ApplicationDef,
    out_dir: Path,
    incl_app_details: bool = True,
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
    app_name = app.name

    # Build flat rows
    flat_rows: List[Dict[str, Any]] = []

    # 1) Application-level items (fields and possibly embedded components)
    for item in app.items:
        if isinstance(item, FieldDef):
            top = item.ref
            top_desc = item.description
            field_chain = [item.ref]
            flat_rows.append(
                make_row(
                    app_ref,
                    app_desc,
                    top,
                    top_desc,
                    field_chain,
                    item,
                    incl_app_details=incl_app_details,
                )
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
                    make_row(
                        app_ref,
                        app_desc,
                        top,
                        top_desc,
                        field_chain,
                        f,
                        incl_app_details=incl_app_details,
                    )
                )
        else:
            # defensive: skip unknown item types
            continue

    # 2) Modules

    for mod in app.modules:
        if not mod:
            continue

        # Produce rows for this module
        mod_rows = flatten_module_to_rows(mod, app_ref)

        # If a module has zero fields/components, still emit a placeholder row
        if not mod_rows:
            row = {
                "top_level": mod.name,
                "top_description": mod.description,
                "field_chain": [""],  # no field
                "description": "",
                "datatype": "",
                "requirement": "",
            }
            if incl_app_details:
                row["application"] = app_ref
                row["application_description"] = app_desc
            flat_rows.append(row)
        else:
            for comp_path, f in mod_rows:
                # top-level is the module name
                top = mod.name
                # field_chain is the component path + field name
                field_chain = comp_path + [format_field_name(f)]
                flat_rows.append(
                    make_row(
                        app_ref,
                        app_desc,
                        top,
                        mod.description,
                        field_chain,
                        f,
                        incl_app_details=incl_app_details,
                    )
                )

    # If there are no rows, add a single empty placeholder so headers still render
    if not flat_rows:
        row = {
            "top_level": "",
            "top_description": "",
            "field_chain": [""],
            "description": "",
            "datatype": "",
            "requirement": "",
        }
        if incl_app_details:
            row["application"] = app_ref or ""
            row["application_description"] = app_desc or ""
        flat_rows.append(row)

    # Figure out max depth of field_chain to create field1..N columns
    max_depth = max((len(r["field_chain"]) for r in flat_rows), default=1)

    # Header
    header = []
    if incl_app_details:
        header += ["application", "application-description"]
    header += [
        "top-level",
        "top-level-description",
    ]
    header += [f"field{i}" for i in range(1, max_depth + 1)]
    header += ["description", "datatype", "requirement"]
    ws.append(header)

    # format the heeader row
    format_header_row(ws)

    # Write rows while remembering blocks for merging
    start_row_for_app = ws.max_row + 1
    # We also merge top-level blocks: whenever top_level value changes, close the previous block
    current_top = None
    top_block_start = None
    module_cols = [1, 2]
    if incl_app_details:
        module_cols = [3, 4]

    def close_top_block(end_row: int, cols: List[int]):
        if top_block_start is not None and end_row >= top_block_start:
            # merge the top-level and top-level-description cols
            for col in cols:
                merge_cells_vertical(ws, col, top_block_start, end_row)

    for row in flat_rows:
        # flush/rotate top-level block if the value changes
        if row["top_level"] != current_top:
            # close previous block
            prev_end = ws.max_row
            close_top_block(prev_end, cols=module_cols)
            # start new block
            current_top = row["top_level"]
            top_block_start = prev_end + 1

        # Expand field_chain into field columns with padding
        chain = row["field_chain"]
        padded = chain + [""] * (max_depth - len(chain))

        spreadsheet_row = []
        if incl_app_details:
            spreadsheet_row += [
                row["application"],
                row["application_description"],
            ]
        spreadsheet_row += [
            row["top_level"],
            row["top_description"],
            *padded,
            row["description"],
            row["datatype"],
            row["requirement"],
        ]
        ws.append(spreadsheet_row)

    # Close last top-level block
    close_top_block(ws.max_row, cols=module_cols)

    # Merge application/application-description across all rows
    if incl_app_details:
        end_row_for_app = ws.max_row
        if end_row_for_app >= start_row_for_app:
            # merge application cells
            merge_cells_vertical(ws, 1, start_row_for_app, end_row_for_app)
            merge_cells_vertical(ws, 2, start_row_for_app, end_row_for_app)

    # Excel formatting
    set_alignment_all(ws)
    auto_width(ws)

    filename = f"{app_name} ({app_ref})"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{to_anchor(filename)}.xlsx"
    wb.save(out_path)
    return out_path


# ---------- Run for all applications ----------
if __name__ == "__main__":
    from loader import load_specification_model

    model = load_specification_model()
    output_dir = Path("generated/spreadsheet")
    for app in model["applications"].values():
        # check it isn't a sub-type
        if app.extends is None:
            path = write_application_excel(app, output_dir, incl_app_details=False)
            print("Wrote:", path)
