from loader import load_content
from generate_info_model import generate_module


def test_generate_module_uses_resolved_field_name_for_top_level_rows():
    specification = load_content()

    module_markdown = generate_module("desc-proposed-works-lb-ldc", specification)

    assert (
        "| description | Description of Proposed Works |" in module_markdown
    )


def test_generate_module_keeps_component_reference_rows():
    specification = load_content()

    module_markdown = generate_module("tree-work-details", specification)

    assert "| tree-details | Tree details[]{} |" in module_markdown
