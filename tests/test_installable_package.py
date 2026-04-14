from planning_application_specification import Specification
from planning_application_specification.models import ApplicationDef
from planning_application_specification.specification import (
    ResolvedComponentReference,
    ResolvedField,
    SelectionContext,
)


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


def test_application_returns_uniform_application_view_for_single_type(project_root):
    spec = Specification.load(project_root)

    application = spec.application("hh")

    assert isinstance(application, ApplicationDef)
    assert application.ref == "hh"
    assert application.application_types == ["hh"]
    assert application.is_combined is False
    assert application.allow_additional_properties is True
    assert len(application.items) == 1
    assert len(application.component_usages) == 1
    assert len(application.modules) > 0
    assert application.modules[0].ref


def test_application_returns_uniform_application_view_for_combined_type(project_root):
    spec = Specification.load(project_root)

    application = spec.application(["hh", "lbc"])

    assert isinstance(application, ApplicationDef)
    assert application.ref == "hh;lbc"
    assert application.application_types == ["hh", "lbc"]
    assert application.is_combined is True
    assert application.entry_date == "2026-04-14"
    assert application.start_date == "2026-04-14"
    assert application.end_date == ""
    assert "connected consent" in application.description
    assert application.allow_additional_properties is True
    assert len(application.items) == 1
    assert len(application.field_usages) == 0
    assert len(application.component_usages) == 1
    assert application.component_usages[0].component.ref == "application"
    assert len(application.modules) > 0
    assert all(hasattr(module, "ref") for module in application.modules)


def test_resolve_field_returns_module_level_override(project_root):
    spec = Specification.load(project_root)

    resolved = spec.resolve_field("description", module="tree-work-details")

    assert isinstance(resolved, ResolvedField)
    assert resolved.ref == "description"
    assert (
        resolved.description
        == "Description of work applicant wishes to carry out, including identifying the trees, species and setting out the work"
    )
    assert resolved.required is True
    assert resolved.container_kind == "module"
    assert resolved.container_ref == "tree-work-details"


def test_resolve_field_returns_component_level_override(project_root):
    spec = Specification.load(project_root)

    resolved = spec.resolve_field("no-bedrooms-unknown", component="bedroom-count")

    assert resolved.ref == "no-bedrooms-unknown"
    assert resolved.required is True
    assert resolved.container_kind == "component"
    assert resolved.container_ref == "bedroom-count"


def test_resolve_field_respects_applies_if_selection(project_root):
    spec = Specification.load(project_root)

    applicable = spec.resolve_field(
        "is-psi",
        module="proposal-details",
        selection=SelectionContext(application_type="full"),
    )
    not_applicable = spec.resolve_field(
        "is-psi",
        module="proposal-details",
        selection=SelectionContext(application_type="outline"),
    )

    assert applicable.applies is True
    assert not_applicable.applies is False
    assert applicable.required is True
    assert isinstance(applicable.required_if, type(None))


def test_resolve_container_items_returns_mixed_module_items_in_order(project_root):
    spec = Specification.load(project_root)

    items = spec.resolve_container_items(module="tree-work-details")

    assert len(items) == 2
    assert isinstance(items[0], ResolvedField)
    assert isinstance(items[1], ResolvedComponentReference)
    assert items[0].ref == "description"
    assert items[1].ref == "tree-details"
    assert items[1].component_ref == "tree-details"
    assert items[1].container_kind == "module"
    assert items[1].container_ref == "tree-work-details"


def test_resolve_container_items_returns_component_items(project_root):
    spec = Specification.load(project_root)

    items = spec.resolve_container_items(component="bedroom-count")

    assert len(items) > 0
    assert all(isinstance(item, ResolvedField) for item in items)
    assert any(item.ref == "no-bedrooms-unknown" for item in items)
    assert all(item.container_kind == "component" for item in items)
    assert all(item.container_ref == "bedroom-count" for item in items)


def test_resolve_container_items_applies_selection_to_component_reference_rows(project_root):
    spec = Specification.load(project_root)

    applicable_items = spec.resolve_container_items(
        module="proposal-details",
        selection=SelectionContext(application_type="reserved-matters"),
    )
    not_applicable_items = spec.resolve_container_items(
        module="proposal-details",
        selection=SelectionContext(application_type="full"),
    )

    applicable = next(item for item in applicable_items if item.ref == "related-application")
    not_applicable = next(
        item for item in not_applicable_items if item.ref == "related-application"
    )

    assert isinstance(applicable, ResolvedComponentReference)
    assert applicable.applies is True
    assert not_applicable.applies is False


def test_resolve_container_items_requires_exactly_one_container(project_root):
    spec = Specification.load(project_root)

    try:
        spec.resolve_container_items()
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError when no container is provided")

    try:
        spec.resolve_container_items(module="proposal-details", component="bedroom-count")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError when both containers are provided")
