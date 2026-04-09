from planning_application_specification import Specification
from planning_application_specification.specification import SelectionContext


def test_specification_load_reads_local_checkout(project_root):
    spec = Specification.load(project_root)

    assert spec.source_path == project_root
    assert "description" in spec.fields
    assert "tenure-type" in spec.tables["codelist"]


def test_canonical_codelist_lookup_returns_items(project_root):
    spec = Specification.load(project_root)

    codelist = spec.codelist("tenure-type")
    item_refs = [item.reference for item in codelist.items]

    assert codelist.ref == "tenure-type"
    assert "market-housing" in item_refs
    assert "london-affordable-rent" in item_refs


def test_applicable_codelist_filters_by_profile_and_application_type(project_root):
    spec = Specification.load(project_root)

    applicable = spec.codelist("tenure-type").applicable(
        selection=SelectionContext(
            specification_profile="gla",
            application_type="full",
        )
    )
    item_refs = [item.reference for item in applicable.items]

    assert applicable.usage_rules_applied is True
    assert "market-for-sale" in item_refs
    assert "london-affordable-rent" in item_refs
    assert "market-housing" not in item_refs
    assert "social-rented" not in item_refs


def test_canonical_field_lookup_returns_field_definition(project_root):
    spec = Specification.load(project_root)

    field = spec.field("description")

    assert field.ref == "description"
    assert field.name == "Description"


def test_canonical_component_lookup_returns_component_definition(project_root):
    spec = Specification.load(project_root)

    component = spec.component("bedroom-count")

    assert component.ref == "bedroom-count"
    assert component.name == "Bedroom count"
    assert len(component.field_usages) > 0


def test_canonical_module_lookup_returns_module_definition(project_root):
    spec = Specification.load(project_root)

    module = spec.module("proposal-details")

    assert module.ref == "proposal-details"
    assert module.name == "Description of the proposal"
    assert len(module.field_usages) > 0
