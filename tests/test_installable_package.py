from planning_application_specification import Specification
from planning_application_specification.application_types import (
    canonical_application_ref,
    normalise_application_types,
)
from planning_application_specification.applications import (
    get_active_combined_application_refs,
)
from planning_application_specification.models import ApplicationDef
from planning_application_specification.specification import (
    CodelistUsages,
    ComponentUsages,
    FieldUsages,
    ResolvedComponentReference,
    ResolvedField,
    SelectionContext,
)


def test_application_type_normalisation_is_shared_and_stable():
    assert normalise_application_types(" lbc ; hh ; hh ") == ("hh", "lbc")
    assert normalise_application_types(["hh;lbc", "full"]) == ("full", "hh", "lbc")
    assert canonical_application_ref(["lbc", "hh"]) == "hh;lbc"


def test_specification_load_reads_local_checkout(project_root):
    spec = Specification.load(project_root)

    assert spec.source_path == project_root
    assert "description" in spec.fields
    assert "planning-application" in spec.datasets
    assert "tenure-type" in spec.tables["codelist"]


def test_canonical_codelist_lookup_returns_items(project_root):
    spec = Specification.load(project_root)

    codelist = spec.codelist("tenure-type")
    item_refs = [item.reference for item in codelist.items]

    assert codelist.ref == "tenure-type"
    assert "market-housing" in item_refs
    assert "london-affordable-rent" in item_refs
    assert codelist.usage == "data/usage/tenure-type-usage.csv"


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
    assert field.codelist is None


def test_canonical_field_lookup_exposes_codelist_when_defined(project_root):
    spec = Specification.load(project_root)

    field = spec.field("decision-maker")

    assert field.ref == "decision-maker"
    assert field.codelist == "decision-maker"


def test_canonical_component_lookup_returns_component_definition(project_root):
    spec = Specification.load(project_root)

    component = spec.component("bedroom-count")

    assert component.ref == "bedroom-count"
    assert component.name == "Bedroom count"
    assert len(component.field_usages) > 0


def test_canonical_component_lookup_exposes_rules_and_validation(project_root):
    spec = Specification.load(project_root)

    submission_details_component = spec.component("submission-details")
    owner_component = spec.component("owner")

    assert submission_details_component.rules[0]["rule"] == "submission-reference must identify the submitted payload"
    assert owner_component.rules[0]["rule"] == "person details must be complete for identification purposes"


def test_canonical_module_lookup_returns_module_definition(project_root):
    spec = Specification.load(project_root)

    module = spec.module("proposal-details")

    assert module.ref == "proposal-details"
    assert module.name == "Description of the proposal"
    assert len(module.field_usages) > 0


def test_canonical_module_lookup_exposes_rules(project_root):
    spec = Specification.load(project_root)

    module = spec.module("con-remove-vary")

    assert module.rules == [
        "Reason must explain why the applicant wishes condition(s) to be removed or changed",
        "Condition change should specify how the condition should vary if modification is sought",
    ]


def test_canonical_codelist_lookup_exposes_source_metadata(project_root):
    spec = Specification.load(project_root)

    codelist = spec.codelist("application-type")

    assert codelist.ref == "application-type"
    assert codelist.source == "data/planning-application-type.csv"


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
    assert "householder planning permission" in application.description
    assert application.allow_additional_properties is True
    assert len(application.items) == 1
    assert len(application.field_usages) == 0
    assert len(application.component_usages) == 1
    assert application.component_usages[0].component.ref == "submission-details"
    assert len(application.modules) > 0
    assert all(hasattr(module, "ref") for module in application.modules)


def test_applications_with_module_returns_canonical_applications_in_sorted_order(project_root):
    spec = Specification.load(project_root)

    applications = spec.applications_with_module("proposal-details")

    refs = [application.ref for application in applications]
    assert refs == sorted(refs)
    assert "hh" in refs
    assert "lbc" in refs
    assert "technical-details-consent" in refs
    assert "hh;lbc" in refs
    assert "outline" not in refs
    assert "outline-all" in refs
    assert "outline-some" in refs
    assert any(application.ref == "hh;lbc" and application.is_combined for application in applications)


def test_applications_with_module_rejects_unknown_module(project_root):
    spec = Specification.load(project_root)

    try:
        spec.applications_with_module("not-a-real-module")
    except KeyError as exc:
        assert "Unknown module" in str(exc)
    else:
        raise AssertionError("Expected KeyError for unknown module")


def test_field_usages_returns_grouped_def_and_usage_matches(project_root):
    spec = Specification.load(project_root)

    usages = spec.field_usages("description")

    assert isinstance(usages, FieldUsages)
    assert len(usages.modules) > 0
    assert all(match.container_type == "module" for match in usages.modules)
    assert all(match.container.ref for match in usages.modules)
    assert all(match.usage.original.ref == "description" for match in usages.modules)
    assert any(match.container.ref == "proposal-details" for match in usages.modules)
    assert all(match.container_type == "component" for match in usages.components)
    assert all(match.usage.original.ref == "description" for match in usages.components)
    assert all(match.container_type == "dataset" for match in usages.datasets)
    assert all(match.usage.original.ref == "description" for match in usages.datasets)
    assert any(
        match.container.ref == "planning-application" for match in usages.datasets
    )


def test_field_usages_returns_component_matches(project_root):
    spec = Specification.load(project_root)

    usages = spec.field_usages("reference")

    assert len(usages.components) > 0
    assert all(match.container_type == "component" for match in usages.components)
    assert all(match.usage.original.ref == "reference" for match in usages.components)


def test_field_usages_rejects_unknown_field(project_root):
    spec = Specification.load(project_root)

    try:
        spec.field_usages("not-a-real-field")
    except KeyError as exc:
        assert "Unknown field" in str(exc)
    else:
        raise AssertionError("Expected KeyError for unknown field")


def test_codelist_usages_returns_canonical_field_matches(project_root):
    spec = Specification.load(project_root)

    usages = spec.codelist_usages("decision-maker")

    assert isinstance(usages, CodelistUsages)
    assert [field.ref for field in usages.fields] == ["decision-maker"]


def test_codelist_usages_returns_module_usage_override_matches(project_root):
    spec = Specification.load(project_root)

    usages = spec.codelist_usages("applicant-interest-type")

    assert [field.ref for field in usages.fields] == ["applicant-interest-type"]

    module_matches = {
        match.container.ref: match for match in usages.modules
    }
    assert "interest-details" in module_matches
    assert "ldc-interest" in module_matches

    interest_details = module_matches["interest-details"]
    assert interest_details.container_type == "module"
    assert interest_details.usage.original.ref == "applicant-interest-type"
    assert interest_details.usage.original.codelist == "applicant-interest-type"


def test_codelist_usages_returns_component_usage_override_matches(project_root):
    spec = Specification.load(project_root)

    usages = spec.codelist_usages("waste-throughput-unit")

    component_matches = {
        match.container.ref: match for match in usages.components
    }
    assert "waste-management" in component_matches

    waste_management = component_matches["waste-management"]
    assert waste_management.container_type == "component"
    assert waste_management.usage.original.ref == "unit-type"
    assert waste_management.usage.original.codelist == "waste-capacity-unit"
    assert waste_management.usage.overrides["codelist"] == "waste-throughput-unit"


def test_codelist_usages_supports_external_source_codelists(project_root):
    spec = Specification.load(project_root)

    usages = spec.codelist_usages("listed-building-grade")

    assert isinstance(usages, CodelistUsages)


def test_codelist_usages_rejects_unknown_codelist(project_root):
    spec = Specification.load(project_root)

    try:
        spec.codelist_usages("not-a-real-codelist")
    except KeyError as exc:
        assert "Unknown codelist" in str(exc)
    else:
        raise AssertionError("Expected KeyError for unknown codelist")


def test_component_usages_returns_fields_and_modules(project_root):
    spec = Specification.load(project_root)

    usages = spec.component_usages("applicant")

    assert isinstance(usages, ComponentUsages)
    assert [field.ref for field in usages.fields] == ["applicants"]

    module_matches = {match.container.ref: match for match in usages.modules}
    assert "applicant-details" in module_matches

    applicant_details = module_matches["applicant-details"]
    assert applicant_details.container_type == "module"
    assert applicant_details.usage.original.ref == "applicants"
    assert applicant_details.usage.original.component == "applicant"


def test_component_usages_rejects_unknown_component(project_root):
    spec = Specification.load(project_root)

    try:
        spec.component_usages("not-a-real-component")
    except KeyError as exc:
        assert "Unknown component" in str(exc)
    else:
        raise AssertionError("Expected KeyError for unknown component")


def test_application_rejects_unknown_combined_type(project_root):
    spec = Specification.load(project_root)

    try:
        spec.application(["hh", "full"])
    except KeyError as exc:
        assert "Unknown combined application type" in str(exc)
    else:
        raise AssertionError("Expected KeyError for unknown combined application type")


def test_application_rejects_inactive_combined_type(project_root):
    spec = Specification.load(project_root)

    try:
        spec.application(["full", "haz-substance-consent"])
    except ValueError as exc:
        assert "recognised but not yet active" in str(exc)
    else:
        raise AssertionError("Expected ValueError for inactive combined application type")


def test_package_exposes_active_combined_application_refs(project_root):
    spec = Specification.load(project_root)

    refs = get_active_combined_application_refs(spec.tables)

    assert "hh;lbc" in refs
    assert "full;lbc" in refs
    assert "full;haz-substance-consent" not in refs


def test_combined_application_uses_false_allow_additional_properties_if_either_member_is_false(
    project_root,
):
    spec = Specification.load(project_root)

    original_value = spec.applications["lbc"].allow_additional_properties
    spec.applications["lbc"].allow_additional_properties = False
    try:
        application = spec.application(["hh", "lbc"])
    finally:
        spec.applications["lbc"].allow_additional_properties = original_value

    assert application.allow_additional_properties is False


def test_combined_application_dedupes_application_level_items(project_root):
    spec = Specification.load(project_root)

    application = spec.application(["hh", "lbc"])

    item_keys = []
    for item in application.items:
        if hasattr(item, "original"):
            item_keys.append(("field", item.original.ref))
        else:
            item_keys.append(
                (
                    "component",
                    item.component.ref,
                    item.referenced_by_field.original.ref,
                )
            )

    assert item_keys == [
        ("component", "submission-details", "submission-details")
    ]


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


def test_resolve_field_supports_combined_application_selection_with_or_semantics(
    project_root,
):
    spec = Specification.load(project_root)

    applicable = spec.resolve_field(
        "has-falling-trees-risk",
        module="trees-hedges",
        selection=SelectionContext(application_type=["hh", "lbc"]),
    )
    not_applicable = spec.resolve_field(
        "has-falling-trees-risk",
        module="trees-hedges",
        selection=SelectionContext(application_type="lbc"),
    )

    assert applicable.applies is True
    assert not_applicable.applies is False


def test_resolve_field_supports_semicolon_delimited_combined_application_selection(
    project_root,
):
    spec = Specification.load(project_root)

    applicable = spec.resolve_field(
        "has-falling-trees-risk",
        module="trees-hedges",
        selection=SelectionContext(application_type="hh;lbc"),
    )

    assert applicable.applies is True


def test_resolve_field_applies_if_matches_parent_application_type(project_root):
    spec = Specification.load(project_root)

    inherited_from_outline = spec.resolve_field(
        "description",
        module="proposal-details",
        selection=SelectionContext(application_type="outline-some"),
    )
    full_only = spec.resolve_field(
        "is-psi",
        module="proposal-details",
        selection=SelectionContext(application_type="outline-some"),
    )

    assert inherited_from_outline.applies is True
    assert full_only.applies is False


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
