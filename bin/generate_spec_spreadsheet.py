from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter

# ---------- Declarative model primitives ----------


@dataclass
class FieldDef:
    ref: str
    name: str
    datatype: str = "string"
    required: bool = False
    description: str = ""


@dataclass
class ComponentDef:
    ref: str
    name: str
    description: str = ""
    fields: List[FieldDef] = field(default_factory=list)
    components: List["ComponentDef"] = field(
        default_factory=list
    )  # allow nested components


@dataclass
class ModuleDef:
    ref: str
    name: str
    description: str = ""
    # Modules can have their own fields and/or nested components
    fields: List[FieldDef] = field(default_factory=list)
    components: List[ComponentDef] = field(default_factory=list)


# ---------- Example minimal model (replace with your loader) ----------

# site-details → site-location → site-boundary
site_location = ComponentDef(
    ref="site-location",
    name="site-location",
    description="Where the proposed development sits.",
    fields=[
        FieldDef(
            ref="site-boundary",
            name="site-boundary",
            datatype="geojson",
            required=False,
            description="Geometry of the site",
        ),
    ],
)

site_details = ModuleDef(
    ref="site-details",
    name="site-details",
    description="Location and extent of the site.",
    components=[site_location],
)

# agent-details → agent → person → first-name
person = ComponentDef(
    ref="person",
    name="person",
    fields=[
        FieldDef(
            ref="first-name",
            name="first-name",
            datatype="string",
            required=True,
            description="The first name of the individual",
        ),
        FieldDef(
            ref="surname-name",
            name="surname-name",
            datatype="string",
            required=True,
            description="The surname of the individual",
        ),
    ],
)
agent = ComponentDef(
    ref="agent",
    name="agent",
    components=[person],
    fields=[
        FieldDef(
            ref="reference",
            name="reference",
            datatype="string",
            required=True,
            description="The reference of the agent",
        ),
    ],
)
agent_details = ModuleDef(
    ref="agent-details",
    name="agent-details",
    description="Information about the agent.",
    components=[agent],
)

MODULES: Dict[str, ModuleDef] = {
    "site-details": site_details,
    "agent-details": agent_details,
}

# Application definition (like your YAML example)
HOUSEHOLDER = {
    "application": "hh",
    "name": "Householder planning application",
    "description": "A simplified process for applications to alter or enlarge a single house (but not a flat), including works within the boundary/garden",
    "fields": [  # app-level fields
        {
            "field": "application",
            "required": True,
            "datatype": "string",
            "description": "Application identifier",
        },
    ],
    "modules": [
        {"module": "site-details"},
        {"module": "agent-details"},
    ],
}

APPLICATIONS = [HOUSEHOLDER]  # add more as needed


# ---------- Traversal helpers ----------


def walk_component_paths(
    component: ComponentDef, prefix: List[str]
) -> List[Tuple[List[str], FieldDef]]:
    """
    Return list of (path_names, field) where path_names is the chain of component names
    leading to the field (e.g. ['agent', 'person', 'first-name'] but we keep field separate).
    """
    rows: List[Tuple[List[str], FieldDef]] = []
    # fields at this component level
    for f in component.fields:
        rows.append((prefix + [component.name], f))
    # recurse into nested components
    for c in component.components:
        rows.extend(walk_component_paths(c, prefix + [component.name]))
    return rows


def flatten_module_to_rows(mod: ModuleDef) -> List[Tuple[List[str], FieldDef]]:
    """
    Produce rows for a module. For each field:
      - path is [component1, component2, ..., field_name] (module name goes in 'top-level').
      - we return (path_without_fieldname_components, field) so caller can split into fieldN cols.
    """
    rows: List[Tuple[List[str], FieldDef]] = []
    # module-level fields (no component); path will just be [field_name]
    for f in mod.fields:
        rows.append(([mod.name], f))  # keep module name in path head for consistency
    # component trees
    for c in mod.components:
        for comp_path, f in walk_component_paths(c, []):
            rows.append((comp_path, f))
    return rows


# ---------- Excel writing ----------


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
    app: Dict[str, Any], modules_index: Dict[str, ModuleDef], out_dir: Path
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

    app_code = app["application"]
    app_desc = app["description"]

    # Build flat rows
    flat_rows: List[Dict[str, Any]] = []

    # 1) Application-level fields
    for fld in app.get("fields", []):
        # top-level = the field name at the application level
        top = fld["field"]
        top_desc = fld["description"]
        field_chain = [
            fld["field"]
        ]  # no nested components under app field in this example
        flat_rows.append(
            dict(
                application=app_code,
                application_description=app_desc,
                top_level=top,
                top_description=top_desc,
                field_chain=field_chain,  # includes the final field name
                description=fld.get("description", ""),
                datatype=fld.get("datatype", "string"),
                requirement="MUST" if fld.get("required", False) else "MAY",
            )
        )

    # 2) Modules
    for m in app.get("modules", []):
        mod_id = m["module"]
        mod = modules_index.get(mod_id)
        if not mod:
            continue

        # Produce rows for this module
        mod_rows = flatten_module_to_rows(mod)

        # If a module has zero fields/components, still emit a placeholder row
        if not mod_rows:
            flat_rows.append(
                dict(
                    application=app_code,
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
                field_chain = comp_path + [f.name]
                flat_rows.append(
                    dict(
                        application=app_code,
                        application_description=app_desc,
                        top_level=top,
                        top_description=mod.description,
                        field_chain=field_chain,
                        description=f.description,
                        datatype=f.datatype,
                        requirement="MUST" if f.required else "MAY",
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
    out_path = out_dir / f"{app_code}.xlsx"
    wb.save(out_path)
    return out_path


# ---------- Run for all applications ----------
if __name__ == "__main__":
    output_dir = Path("tmp/app_specs")
    for app in APPLICATIONS:
        path = write_application_excel(app, MODULES, output_dir)
        print("Wrote:", path)
