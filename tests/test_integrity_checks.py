# tests/test_integrity_checks.py
import pytest

from bin.integrity_checks import applications as application_checks
from bin.integrity_checks import components as component_checks
from bin.integrity_checks import datasets as dataset_checks
from bin.integrity_checks import justifications as justification_checks
from bin.integrity_checks import needs as need_checks
from bin.integrity_checks import specifications as specification_checks
from bin.integrity_checks import utils as integrity_utils
from bin.integrity_checks import usage as usage_checks
from bin.integrity_checks.components import check_field_condition_references
from bin.integrity_checks.codelists import (
    check_codelist_blank_keys,
    check_codelist_declared_fields_present,
    check_codelist_duplicate_keys,
    check_codelist_field_references,
    check_codelist_parent_column,
    check_codelist_parent_references,
    check_codelist_usage_source,
)
from bin.integrity_checks.fields import (
    check_codelist_exists,
    check_datetime_precision,
    check_enum_codelist,
    check_object_components,
)
from bin.integrity_checks.modules import (
    check_applies_if_structure,
    check_redundant_component_overrides as check_module_redundant_component_overrides,
    check_required_if_fields,
)


@pytest.fixture
def valid_applies_if_module():
    """Module with valid applies-if structure."""
    return {
        "test-module": {
            "fields": [
                {
                    "field": "test-field",
                    "applies-if": {"application-type": {"in": ["full", "outline"]}},
                }
            ]
        }
    }


@pytest.fixture
def invalid_applies_if_module():
    """Module with invalid applies-if structure (list instead of dict)."""
    return {
        "test-module": {
            "fields": [
                {
                    "field": "test-field",
                    "applies-if": ["not", "a", "dict"],  # Should be dict
                }
            ]
        }
    }


@pytest.fixture
def multiple_modules_mixed():
    """Multiple modules with mix of valid/invalid applies-if."""
    return {
        "valid-module": {
            "fields": [
                {
                    "field": "valid-field",
                    "applies-if": {"application-type": {"in": ["hh"]}},
                }
            ]
        },
        "invalid-module": {
            "fields": [
                {
                    "field": "invalid-field",
                    "applies-if": "should-be-dict",
                }
            ]
        },
    }


@pytest.fixture
def module_without_applies_if():
    """Module with no applies-if conditions (should pass)."""
    return {
        "simple-module": {
            "fields": [
                {
                    "field": "simple-field",
                    "description": "Just a normal field",
                }
            ]
        }
    }


class TestAppliesIfStructure:
    """Test applies-if structure validation."""

    def test_valid_structure_passes(self, valid_applies_if_module):
        """Test that valid applies-if structure passes."""
        has_no_errors = check_applies_if_structure(valid_applies_if_module)
        assert has_no_errors

    def test_application_type_must_exist(self):
        modules = {
            "test-module": {
                "fields": [
                    {
                        "field": "test-field",
                        "applies-if": {
                            "application-type": {
                                "in": ["full", "tehcnical-details-consent"]
                            }
                        },
                    }
                ]
            }
        }

        has_no_errors = check_applies_if_structure(
            modules, application_types={"full": {}, "technical-details-consent": {}}
        )
        assert not has_no_errors

    def test_invalid_structure_fails(self, invalid_applies_if_module):
        """Test that invalid applies-if structure fails."""
        has_no_errors = check_applies_if_structure(invalid_applies_if_module)
        assert not has_no_errors
        # should test it returns type of error too (check currently does not)
        # assert "applies-if should be a dict" in errors[0]

    def test_no_applies_if_passes(self, module_without_applies_if):
        """Test that modules without applies-if pass validation."""
        has_no_errors = check_applies_if_structure(module_without_applies_if)
        assert has_no_errors

    def test_mixed_modules(self, multiple_modules_mixed):
        """Test validation with mix of valid/invalid modules."""
        has_no_errors = check_applies_if_structure(multiple_modules_mixed)
        assert not has_no_errors
        # can we check that it reports the invalid one?


class TestComplexAppliesIfScenarios:
    """Test complex applies-if validation scenarios."""

    @pytest.fixture
    def nested_applies_if_module(self):
        """Module with nested applies-if conditions."""
        return {
            "complex-module": {
                "fields": [
                    {
                        "field": "complex-field",
                        "applies-if": {
                            "application-type": {"in": ["full", "outline"]},
                            "development-type": {"equals": "new-build"},
                        },
                    }
                ]
            }
        }

    def test_nested_conditions_valid(self, nested_applies_if_module):
        """Test that nested applies-if conditions are valid."""
        has_no_errors = check_applies_if_structure(nested_applies_if_module)
        assert has_no_errors

    @pytest.mark.parametrize(
        "invalid_applies_if", [["list", "not", "dict"], "string-not-dict", 123]
    )
    def test_various_invalid_types(self, invalid_applies_if):
        """Test various invalid applies-if types."""
        modules = {
            "test-module": {
                "fields": [{"field": "test-field", "applies-if": invalid_applies_if}]
            }
        }
        has_no_errors = check_applies_if_structure(modules)
        assert not has_no_errors


class TestRequiredIfFieldReferences:
    """Test required-if field reference validation against local object fields."""

    def test_module_required_if_field_must_exist_in_same_module(self):
        modules = {
            "part-discharge": {
                "fields": [
                    {"field": "is-discharging-part", "required": True},
                    {
                        "field": "discharging-part-details",
                        "required-if": [{"field": "discharging-part", "value": True}],
                    },
                ]
            }
        }

        has_no_errors = check_required_if_fields(modules)
        assert not has_no_errors

    def test_module_required_if_field_in_same_module_passes(self):
        modules = {
            "part-discharge": {
                "fields": [
                    {"field": "is-discharging-part", "required": True},
                    {
                        "field": "discharging-part-details",
                        "required-if": [{"field": "is-discharging-part", "value": True}],
                    },
                ]
            }
        }

        has_no_errors = check_required_if_fields(modules)
        assert has_no_errors

    def test_module_required_if_dotted_field_path_is_allowed_for_now(self):
        modules = {
            "agent-contact": {
                "fields": [
                    {
                        "field": "contact-details",
                        "required-if": [
                            {
                                "field": "agent-details.agent.reference",
                                "operator": "not_empty",
                            }
                        ],
                    },
                ]
            }
        }

        has_no_errors = check_required_if_fields(modules)
        assert has_no_errors

    def test_module_required_if_nested_contains_selector_is_allowed_for_now(self):
        modules = {
            "non-res-floorspace": {
                "fields": [
                    {"field": "floorspace-details"},
                    {
                        "field": "room-details",
                        "required-if": [
                            {
                                "field": "floorspace-details",
                                "contains": {
                                    "field": "use",
                                    "in": ["c1", "c2", "c2a", "other"],
                                },
                            }
                        ],
                    },
                ]
            }
        }

        has_no_errors = check_required_if_fields(modules)
        assert has_no_errors

    def test_component_required_if_field_must_exist_in_same_component(self):
        components = {
            "test-component": {
                "fields": [
                    {"field": "is-enabled"},
                    {
                        "field": "details",
                        "required-if": [{"field": "missing-local-field", "value": True}],
                    },
                ]
            }
        }

        has_no_errors = check_field_condition_references(
            components,
            fields={},
            application_types={},
        )
        assert not has_no_errors

    def test_component_required_if_with_application_type_and_local_field_passes(self):
        components = {
            "test-component": {
                "fields": [
                    {"field": "is-enabled"},
                    {
                        "field": "details",
                        "required-if": [
                            {
                                "any": [
                                    {"field": "is-enabled", "value": True},
                                    {"application-type": {"in": ["full"]}},
                                ]
                            }
                        ],
                    },
                ]
            }
        }

        has_no_errors = check_field_condition_references(
            components,
            fields={},
            application_types={"full": {}},
        )
        assert has_no_errors

    def test_component_required_if_dotted_field_path_is_allowed_for_now(self):
        components = {
            "contact-details": {
                "fields": [
                    {
                        "field": "email",
                        "required-if": [
                            {
                                "field": "agent-details.agent.reference",
                                "operator": "not_empty",
                            }
                        ],
                    },
                ]
            }
        }

        has_no_errors = check_field_condition_references(
            components,
            fields={},
            application_types={},
        )
        assert has_no_errors


class TestRedundantFieldComponentOverrides:
    def test_module_component_override_fails_when_it_repeats_field_default(self):
        modules = {
            "applicant-details": {
                "fields": [{"field": "person", "component": "person"}]
            }
        }
        fields = {"person": {"component": "person"}}

        assert not check_module_redundant_component_overrides(modules, fields)

    def test_module_component_override_passes_when_it_changes_field_default(self):
        modules = {
            "agent-details": {
                "fields": [{"field": "person", "component": "other-contact"}]
            }
        }
        fields = {"person": {"component": "person"}}

        assert check_module_redundant_component_overrides(modules, fields)

    def test_component_component_override_fails_when_it_repeats_field_default(self):
        components = {
            "applicant": {
                "fields": [{"field": "person", "component": "person"}]
            }
        }
        fields = {"person": {"component": "person"}}

        assert not component_checks.check_redundant_component_overrides(
            components, fields
        )

    def test_component_component_override_passes_when_it_changes_field_default(self):
        components = {
            "other-contact": {
                "fields": [{"field": "person", "component": "other-contact"}]
            }
        }
        fields = {"person": {"component": "person"}}

        assert component_checks.check_redundant_component_overrides(components, fields)


class TestFieldIntegrityChecks:
    def test_object_field_without_component_fails(self):
        fields = {
            "site-location": {
                "field": "site-location",
                "datatype": "object",
            }
        }

        has_no_errors = check_object_components(fields, components={})
        assert not has_no_errors

    def test_object_field_with_unknown_component_fails(self):
        fields = {
            "site-location": {
                "field": "site-location",
                "datatype": "object",
                "component": "missing-component",
            }
        }

        has_no_errors = check_object_components(fields, components={"address": {}})
        assert not has_no_errors

    def test_object_field_with_known_component_passes(self):
        fields = {
            "site-location": {
                "field": "site-location",
                "datatype": "object",
                "component": "address",
            }
        }

        has_no_errors = check_object_components(fields, components={"address": {}})
        assert has_no_errors

    def test_enum_field_without_codelist_fails(self):
        fields = {
            "decision-maker": {
                "field": "decision-maker",
                "datatype": "enum",
            }
        }

        has_no_errors = check_enum_codelist(fields)
        assert not has_no_errors

    def test_non_enum_field_with_codelist_fails(self):
        fields = {
            "decision-maker": {
                "field": "decision-maker",
                "datatype": "string",
                "codelist": "decision-maker",
            }
        }

        has_no_errors = check_enum_codelist(fields)
        assert not has_no_errors

    def test_enum_field_with_codelist_passes(self):
        fields = {
            "decision-maker": {
                "field": "decision-maker",
                "datatype": "enum",
                "codelist": "decision-maker",
            }
        }

        has_no_errors = check_enum_codelist(fields)
        assert has_no_errors

    def test_field_codelist_reference_must_exist(self):
        fields = {
            "decision-maker": {
                "field": "decision-maker",
                "datatype": "enum",
                "codelist": "decision-maker",
            }
        }

        has_no_errors = check_codelist_exists(fields, codelists={"provided-by": {}})
        assert not has_no_errors

    def test_field_codelist_reference_passes_when_present(self):
        fields = {
            "decision-maker": {
                "field": "decision-maker",
                "datatype": "enum",
                "codelist": "decision-maker",
            }
        }

        has_no_errors = check_codelist_exists(fields, codelists={"decision-maker": {}})
        assert has_no_errors

    def test_datetime_field_without_date_precision_fails(self):
        fields = {
            "agricultural-use-start-date": {
                "field": "agricultural-use-start-date",
                "datatype": "datetime",
            }
        }

        has_no_errors = check_datetime_precision(fields)
        assert not has_no_errors

    def test_datetime_field_with_date_precision_passes(self):
        fields = {
            "agricultural-use-start-date": {
                "field": "agricultural-use-start-date",
                "datatype": "datetime",
                "date_precision": "month",
            }
        }

        has_no_errors = check_datetime_precision(fields)
        assert has_no_errors


class TestDatasetIntegrityChecks:
    @pytest.fixture
    def valid_dataset(self):
        return {
            "attribution": "Department",
            "collection": "planning-application",
            "consideration": "required",
            "dataset": "planning-application",
            "description": "Planning application dataset",
            "end-date": "9999-12-31",
            "entity-maximum": "1",
            "entity-minimum": "1",
            "entry-date": "2024-01-01",
            "fields": [{"field": "reference"}],
            "key-field": "reference",
            "licence": "OGL",
            "name": "Planning application",
            "notes": "Notes",
            "phase": "alpha",
            "plural": "Planning applications",
            "prefix": "plan",
            "realm": "planning",
            "replacement-dataset": "",
            "start-date": "2024-01-01",
            "themes": ["planning"],
            "typology": "dataset",
            "version": "1",
            "semantics": "state",
        }

    def test_dataset_name_fails_when_frontmatter_mismatches_key(self):
        datasets = {
            "planning-application": {
                "dataset": "planning-application-record",
            }
        }

        assert not dataset_checks.check_dataset_names(datasets)

    def test_field_references_fail_when_field_name_missing(self):
        datasets = {
            "planning-application": {
                "fields": [{}],
            }
        }

        assert not dataset_checks.check_field_references(datasets, fields={"reference": {}})

    def test_field_references_fail_when_field_reference_unknown(self):
        datasets = {
            "planning-application": {
                "fields": [{"field": "missing-field"}],
            }
        }

        assert not dataset_checks.check_field_references(datasets, fields={"reference": {}})

    def test_field_references_pass_when_all_fields_known(self):
        datasets = {
            "planning-application": {
                "fields": [{"field": "reference"}, {"field": "name"}],
            }
        }

        assert dataset_checks.check_field_references(
            datasets,
            fields={"reference": {}, "name": {}},
        )

    def test_dates_fail_when_entry_date_missing(self):
        datasets = {
            "planning-application": {
                "end-date": "9999-12-31",
            }
        }

        assert not dataset_checks.check_dates(datasets)

    def test_dates_fail_when_end_date_missing(self):
        datasets = {
            "planning-application": {
                "entry-date": "2024-01-01",
            }
        }

        assert not dataset_checks.check_dates(datasets)

    def test_dates_pass_when_both_required_dates_present(self):
        datasets = {
            "planning-application": {
                "entry-date": "2024-01-01",
                "end-date": "9999-12-31",
            }
        }

        assert dataset_checks.check_dates(datasets)

    def test_attrs_fail_when_expected_attribute_missing(self, valid_dataset):
        invalid_dataset = dict(valid_dataset)
        invalid_dataset.pop("licence")

        assert not dataset_checks.check_attrs({"planning-application": invalid_dataset})

    def test_attrs_warn_for_extra_attribute_but_still_pass(self, monkeypatch, valid_dataset):
        warnings = []
        dataset_with_extra = dict(valid_dataset)
        dataset_with_extra["unexpected"] = "extra"

        monkeypatch.setattr(
            dataset_checks,
            "print_warning",
            lambda category, ref, message: warnings.append((category, ref, message)),
        )

        assert dataset_checks.check_attrs({"planning-application": dataset_with_extra})
        assert warnings == [
            ("dataset", "planning-application", "unexpected attribute 'unexpected'")
        ]


class TestApplicationIntegrityChecks:
    def test_application_field_required_when_application_does_not_extend(self):
        applications = {
            "householder": {
                "fields": [{"field": "site-address"}],
                "modules": [{"module": "site-details"}],
            }
        }

        assert not application_checks.check_application_field_present(
            applications,
            fields={"submission-details": {}, "site-address": {}},
        )

    def test_application_field_not_required_when_application_extends(self):
        applications = {
            "householder-amendment": {
                "extends": "householder",
                "fields": [{"field": "site-address"}],
            }
        }

        assert application_checks.check_application_field_present(
            applications,
            fields={"site-address": {}},
        )

    def test_application_field_references_must_exist(self):
        applications = {
            "householder": {
                "fields": [{"field": "submission-details"}, {"field": "missing-field"}],
                "modules": [{"module": "site-details"}],
            }
        }

        assert not application_checks.check_application_field_present(
            applications,
            fields={"submission-details": {}},
        )

    def test_application_field_check_passes_with_application_field_and_known_references(self):
        applications = {
            "householder": {
                "fields": [{"field": "submission-details"}, {"field": "site-address"}],
                "modules": [{"module": "site-details"}],
            }
        }

        assert application_checks.check_application_field_present(
            applications,
            fields={"submission-details": {}, "site-address": {}},
        )

    def test_modules_attribute_required_when_application_does_not_extend(self):
        applications = {
            "householder": {
                "fields": [{"field": "submission-details"}],
            }
        }

        assert not application_checks.check_modules_attr_present(applications)

    def test_modules_attribute_not_required_when_application_extends(self):
        applications = {
            "householder-amendment": {
                "extends": "householder",
                "fields": [{"field": "submission-details"}],
            }
        }

        assert application_checks.check_modules_attr_present(applications)

    def test_module_references_must_exist(self):
        applications = {
            "householder": {
                "modules": [{"module": "missing-module"}],
            }
        }

        assert not application_checks.check_module_references_exist(
            applications,
            modules_list={"site-details": {}},
        )

    def test_module_references_pass_when_all_modules_known(self):
        applications = {
            "householder": {
                "modules": [{"module": "site-details"}, {"module": "ownership"}],
            }
        }

        assert application_checks.check_module_references_exist(
            applications,
            modules_list={"site-details": {}, "ownership": {}},
        )


class TestComponentIntegrityChecks:
    def test_component_name_must_be_kebab_case(self):
        components = {
            "BadComponentName": {
                "fields": [],
            }
        }

        assert not component_checks.check_component_names(components)

    def test_component_names_pass_when_kebab_case(self):
        components = {
            "site-address": {
                "fields": [],
            }
        }

        assert component_checks.check_component_names(components)

    def test_component_field_references_fail_when_field_name_missing(self):
        components = {
            "site-address": {
                "fields": [{}],
            }
        }

        assert not component_checks.check_field_references(
            components,
            fields={"uprn": {}},
        )

    def test_component_field_references_fail_when_field_unknown(self):
        components = {
            "site-address": {
                "fields": [{"field": "missing-field"}],
            }
        }

        assert not component_checks.check_field_references(
            components,
            fields={"uprn": {}},
        )

    def test_component_field_references_fail_for_deprecated_fields(self):
        components = {
            "site-address": {
                "fields": [{"field": "uprn"}],
            }
        }

        assert not component_checks.check_field_references(
            components,
            fields={"uprn": {"end-date": "2024-12-31"}},
        )

    def test_component_field_references_pass_for_known_active_fields(self):
        components = {
            "site-address": {
                "fields": [{"field": "uprn"}, {"field": "postcode"}],
            }
        }

        assert component_checks.check_field_references(
            components,
            fields={"uprn": {}, "postcode": {}},
        )

    def test_component_dates_fail_when_entry_date_missing(self):
        components = {
            "site-address": {
                "end-date": "9999-12-31",
            }
        }

        assert not component_checks.check_dates(components)

    def test_component_dates_fail_when_end_date_missing(self):
        components = {
            "site-address": {
                "entry-date": "2024-01-01",
            }
        }

        assert not component_checks.check_dates(components)

    def test_component_dates_pass_when_required_dates_present(self):
        components = {
            "site-address": {
                "entry-date": "2024-01-01",
                "end-date": "9999-12-31",
            }
        }

        assert component_checks.check_dates(components)


class TestIntegrityCheckUtils:
    def test_has_reference_error_rejects_non_string_reference(self):
        assert integrity_utils.has_reference_error(123, "field", seen_fields=[])

    def test_has_reference_error_rejects_non_kebab_case_reference(self):
        assert integrity_utils.has_reference_error(
            "BadFieldName",
            "field",
            seen_fields=[],
        )

    def test_has_reference_error_rejects_duplicate_reference(self):
        assert integrity_utils.has_reference_error(
            "site-address",
            "field",
            seen_fields=["site-address"],
        )

    def test_has_reference_error_passes_for_unique_kebab_case_reference(self):
        assert not integrity_utils.has_reference_error(
            "site-address",
            "field",
            seen_fields=[],
        )

    def test_get_object_field_names_collects_string_field_names_only(self):
        field_definitions = [
            {"field": "site-address"},
            {"field": "uprn"},
            {"field": 123},
            {"name": "missing-field-key"},
            "not-a-dict",
        ]

        assert integrity_utils.get_object_field_names(field_definitions) == {
            "site-address",
            "uprn",
        }

    def test_iter_required_if_field_refs_walks_nested_conditions(self):
        required_if = [
            {"field": "is-enabled", "value": True},
            {
                "any": [
                    {"field": ["is-primary", "is-secondary"]},
                    {"all": [{"field": "has-details"}]},
                    {"application-type": {"in": ["full"]}},
                ]
            },
        ]

        assert list(integrity_utils.iter_required_if_field_refs(required_if)) == [
            "is-enabled",
            "is-primary",
            "is-secondary",
            "has-details",
        ]

    def test_run_checks_returns_true_when_all_checks_pass(self):
        def check_one():
            return True

        def check_two(arg):
            return arg

        assert integrity_utils.run_checks(
            [(check_one, []), (check_two, [True])]
        )

    def test_run_checks_returns_false_when_any_check_fails(self):
        def check_one():
            return True

        def check_two():
            return False

        assert not integrity_utils.run_checks(
            [(check_one, []), (check_two, [])]
        )


class TestUsageIntegrityChecks:
    def write_usage_csv(self, project_root, tmp_path, rows):
        csv_path = project_root / "tmp" / f"test-usage-{tmp_path.name}.csv"
        csv_path.write_text("\n".join(rows) + "\n", encoding="utf-8")
        return csv_path

    def patch_usage_source_path(self, monkeypatch, csv_path):
        monkeypatch.setattr(usage_checks, "_source_path", lambda meta: csv_path)

    def test_declared_fields_must_exist_in_usage_csv(self, project_root, tmp_path, monkeypatch):
        csv_path = self.write_usage_csv(
            project_root,
            tmp_path,
            [
                "reference,name",
                "full,Full planning application",
            ],
        )
        self.patch_usage_source_path(monkeypatch, csv_path)

        usage_tables = {
            "specification/usage/test-usage.schema.md": {
                "usage": "test-usage",
                "source": "data/test-usage.csv",
                "fields": [{"field": "reference"}, {"field": "missing-column"}],
            }
        }

        try:
            assert not usage_checks.check_usage_declared_fields_exist(usage_tables)
        finally:
            csv_path.unlink(missing_ok=True)

    def test_declared_fields_pass_when_all_columns_exist(self, project_root, tmp_path, monkeypatch):
        csv_path = self.write_usage_csv(
            project_root,
            tmp_path,
            [
                "reference,name",
                "full,Full planning application",
            ],
        )
        self.patch_usage_source_path(monkeypatch, csv_path)

        usage_tables = {
            "specification/usage/test-usage.schema.md": {
                "usage": "test-usage",
                "source": "data/test-usage.csv",
                "fields": [{"field": "reference"}, {"field": "name"}],
            }
        }

        try:
            assert usage_checks.check_usage_declared_fields_exist(usage_tables)
        finally:
            csv_path.unlink(missing_ok=True)

    def test_blank_usage_key_field_fails(self, project_root, tmp_path, monkeypatch):
        csv_path = self.write_usage_csv(
            project_root,
            tmp_path,
            [
                "reference,name",
                ",Missing reference",
            ],
        )
        self.patch_usage_source_path(monkeypatch, csv_path)

        usage_tables = {
            "specification/usage/test-usage.schema.md": {
                "usage": "test-usage",
                "source": "data/test-usage.csv",
                "key-field": "reference",
            }
        }

        try:
            assert not usage_checks.check_usage_key_field_values(usage_tables)
        finally:
            csv_path.unlink(missing_ok=True)

    def test_duplicate_usage_key_field_fails(self, project_root, tmp_path, monkeypatch):
        csv_path = self.write_usage_csv(
            project_root,
            tmp_path,
            [
                "reference,name",
                "full,Full planning application",
                "full,Duplicate full planning application",
            ],
        )
        self.patch_usage_source_path(monkeypatch, csv_path)

        usage_tables = {
            "specification/usage/test-usage.schema.md": {
                "usage": "test-usage",
                "source": "data/test-usage.csv",
                "key-field": "reference",
            }
        }

        try:
            assert not usage_checks.check_usage_key_field_values(usage_tables)
        finally:
            csv_path.unlink(missing_ok=True)

    def test_usage_key_field_passes_with_unique_non_blank_values(self, project_root, tmp_path, monkeypatch):
        csv_path = self.write_usage_csv(
            project_root,
            tmp_path,
            [
                "reference,name",
                "full,Full planning application",
                "outline,Outline planning application",
            ],
        )
        self.patch_usage_source_path(monkeypatch, csv_path)

        usage_tables = {
            "specification/usage/test-usage.schema.md": {
                "usage": "test-usage",
                "source": "data/test-usage.csv",
                "key-field": "reference",
            }
        }

        try:
            assert usage_checks.check_usage_key_field_values(usage_tables)
        finally:
            csv_path.unlink(missing_ok=True)

    def test_specification_profile_must_exist(self, project_root, tmp_path, monkeypatch):
        csv_path = self.write_usage_csv(
            project_root,
            tmp_path,
            [
                "reference,specification-profile",
                "full,missing-profile",
            ],
        )
        self.patch_usage_source_path(monkeypatch, csv_path)
        monkeypatch.setattr(
            usage_checks,
            "_load_codelist_keys",
            lambda codelists, codelist_name: {"draft", "submission"},
        )

        usage_tables = {
            "specification/usage/test-usage.schema.md": {
                "usage": "test-usage",
                "source": "data/test-usage.csv",
            }
        }

        try:
            assert not usage_checks.check_specification_profiles_exist(usage_tables, codelists={})
        finally:
            csv_path.unlink(missing_ok=True)

    def test_specification_profile_passes_when_known(self, project_root, tmp_path, monkeypatch):
        csv_path = self.write_usage_csv(
            project_root,
            tmp_path,
            [
                "reference,specification-profile",
                "full,submission",
            ],
        )
        self.patch_usage_source_path(monkeypatch, csv_path)
        monkeypatch.setattr(
            usage_checks,
            "_load_codelist_keys",
            lambda codelists, codelist_name: {"draft", "submission"},
        )

        usage_tables = {
            "specification/usage/test-usage.schema.md": {
                "usage": "test-usage",
                "source": "data/test-usage.csv",
            }
        }

        try:
            assert usage_checks.check_specification_profiles_exist(usage_tables, codelists={})
        finally:
            csv_path.unlink(missing_ok=True)

    def test_application_types_must_exist(self, project_root, tmp_path, monkeypatch):
        csv_path = self.write_usage_csv(
            project_root,
            tmp_path,
            [
                "reference,application-types",
                "full,full;missing",
            ],
        )
        self.patch_usage_source_path(monkeypatch, csv_path)

        usage_tables = {
            "specification/usage/test-usage.schema.md": {
                "usage": "test-usage",
                "source": "data/test-usage.csv",
            }
        }

        try:
            assert not usage_checks.check_application_types_exist(
                usage_tables,
                applications={"full": {}, "outline": {}},
            )
        finally:
            csv_path.unlink(missing_ok=True)

    def test_application_types_pass_when_all_known(self, project_root, tmp_path, monkeypatch):
        csv_path = self.write_usage_csv(
            project_root,
            tmp_path,
            [
                "reference,application-types",
                "full,full;outline",
            ],
        )
        self.patch_usage_source_path(monkeypatch, csv_path)

        usage_tables = {
            "specification/usage/test-usage.schema.md": {
                "usage": "test-usage",
                "source": "data/test-usage.csv",
            }
        }

        try:
            assert usage_checks.check_application_types_exist(
                usage_tables,
                applications={"full": {}, "outline": {}},
            )
        finally:
            csv_path.unlink(missing_ok=True)


class TestJustificationIntegrityChecks:
    def test_need_refs_fail_when_need_id_is_used(self):
        justifications = {
            "just-1": {
                "need_id": "need-1",
                "needs": ["need-1"],
            }
        }

        assert not justification_checks.check_need_refs(
            justifications,
            needs={"need-1": {}},
        )

    def test_need_refs_fail_when_needs_is_missing(self):
        justifications = {
            "just-1": {}
        }

        assert not justification_checks.check_need_refs(justifications, needs={})

    def test_need_refs_fail_when_needs_is_not_a_list(self):
        justifications = {
            "just-1": {
                "needs": "need-1",
            }
        }

        assert not justification_checks.check_need_refs(
            justifications,
            needs={"need-1": {}},
        )

    def test_need_refs_fail_when_needs_list_is_empty(self):
        justifications = {
            "just-1": {
                "needs": [],
            }
        }

        assert not justification_checks.check_need_refs(justifications, needs={})

    def test_need_refs_pass_with_known_needs_list(self):
        justifications = {
            "just-1": {
                "needs": ["need-1", "need-2"],
            }
        }

        assert justification_checks.check_need_refs(
            justifications,
            needs={"need-1": {}, "need-2": {}},
        )

    def test_body_present_fails_when_content_is_missing(self):
        justifications = {
            "just-1": {
                "content": "",
            }
        }

        assert not justification_checks.check_body_present(justifications)

    def test_body_present_passes_with_non_empty_content(self):
        justifications = {
            "just-1": {
                "content": "This justification explains the link.",
            }
        }

        assert justification_checks.check_body_present(justifications)

    def test_walk_satisfied_by_extracts_nested_dataset_and_field_references(self):
        satisfied_by = {
            "allOf": [
                {"dataset": "decision-notice", "field": "decision"},
                {
                    "anyOf": [
                        {"dataset": "decision-notice", "field": "decision-maker"},
                        {"requires": {"dataset": "committee-meeting", "field": "date"}},
                    ]
                },
            ]
        }

        refs = list(justification_checks._walk_satisfied_by(satisfied_by))

        assert ("decision-notice", "decision") in refs
        assert ("decision-notice", "decision-maker") in refs
        assert ("committee-meeting", "date") in refs

    def test_satisfied_by_refs_fail_for_unknown_dataset(self):
        justifications = {
            "just-1": {
                "satisfied_by": [{"dataset": "missing-dataset", "field": "decision"}]
            }
        }

        assert not justification_checks.check_satisfied_by_refs(
            justifications,
            datasets={"decision-notice": {"fields": [{"field": "decision"}]}},
            fields={"decision": {}},
        )

    def test_satisfied_by_refs_fail_for_unknown_field(self):
        justifications = {
            "just-1": {
                "satisfied_by": [{"dataset": "decision-notice", "field": "missing-field"}]
            }
        }

        assert not justification_checks.check_satisfied_by_refs(
            justifications,
            datasets={"decision-notice": {"fields": [{"field": "decision"}]}},
            fields={"decision": {}},
        )

    def test_satisfied_by_refs_fail_when_field_not_listed_for_dataset(self):
        justifications = {
            "just-1": {
                "satisfied_by": [
                    {
                        "allOf": [
                            {"dataset": "decision-notice", "field": "decision-maker"},
                        ]
                    }
                ]
            }
        }

        assert not justification_checks.check_satisfied_by_refs(
            justifications,
            datasets={"decision-notice": {"fields": [{"field": "decision"}]}},
            fields={"decision": {}, "decision-maker": {}},
        )

    def test_satisfied_by_refs_pass_for_nested_valid_references(self):
        justifications = {
            "just-1": {
                "satisfied_by": {
                    "allOf": [
                        {"dataset": "decision-notice", "field": "decision"},
                        {
                            "anyOf": [
                                {
                                    "dataset": "decision-notice",
                                    "field": "decision-maker",
                                }
                            ]
                        },
                    ]
                }
            }
        }

        assert justification_checks.check_satisfied_by_refs(
            justifications,
            datasets={
                "decision-notice": {
                    "fields": [
                        {"field": "decision"},
                        {"field": "decision-maker"},
                    ]
                }
            },
            fields={"decision": {}, "decision-maker": {}},
        )


class TestNeedIntegrityChecks:
    def test_need_identifier_fails_when_frontmatter_mismatches_key(self):
        needs = {
            "need-1": {
                "need": "need-2",
                "name": "Need one",
                "statement": "A valid statement",
                "status": "draft",
                "priority": "high",
            }
        }

        assert not need_checks.check_need_identifiers(needs)

    def test_status_must_be_valid(self):
        needs = {
            "need-1": {"status": "invalid-status"}
        }

        assert not need_checks.check_status(needs)

    def test_priority_must_be_valid(self):
        needs = {
            "need-1": {"priority": "urgent"}
        }

        assert not need_checks.check_priority(needs)

    def test_name_must_be_non_empty_string(self):
        needs = {
            "need-1": {"name": "   "}
        }

        assert not need_checks.check_name(needs)

    def test_statement_must_be_non_empty_string(self):
        needs = {
            "need-1": {"statement": ""}
        }

        assert not need_checks.check_statement(needs)

    def test_variations_must_be_a_list(self):
        needs = {
            "need-1": {"variations": "need-2"},
            "need-2": {},
        }

        assert not need_checks.check_variations(needs)

    def test_variations_must_reference_known_needs(self):
        needs = {
            "need-1": {"variations": ["missing-need"]},
        }

        assert not need_checks.check_variations(needs)

    def test_variations_pass_with_known_need_refs(self):
        needs = {
            "need-1": {"variations": ["need-2"]},
            "need-2": {},
        }

        assert need_checks.check_variations(needs)

    def test_next_step_must_be_valid_when_present(self):
        needs = {
            "need-1": {"next_step": "ship-it"}
        }

        assert not need_checks.check_next_step(needs)

    def test_next_step_passes_when_blank_or_known(self):
        needs = {
            "need-1": {"next_step": ""},
            "need-2": {"next_step": "review"},
        }

        assert need_checks.check_next_step(needs)

    def test_sources_must_be_a_list(self):
        needs = {
            "need-1": {"sources": "interview"}
        }

        assert not need_checks.check_sources(needs)

    def test_source_entries_must_be_mappings(self):
        needs = {
            "need-1": {"sources": ["interview"]}
        }

        assert not need_checks.check_sources(needs)

    def test_source_type_must_be_valid(self):
        needs = {
            "need-1": {"sources": [{"type": "random"}]}
        }

        assert not need_checks.check_sources(needs)

    def test_sources_pass_with_valid_source_types(self):
        needs = {
            "need-1": {
                "sources": [
                    {"type": "interview"},
                    {"type": "community-session"},
                ]
            }
        }

        assert need_checks.check_sources(needs)


class TestSpecificationIntegrityChecks:
    def test_datasets_exist_fails_when_dataset_attribute_is_missing(self):
        specifications = {
            "decision-stage": {
                "datasets": [{}]
            }
        }

        assert not specification_checks.check_datasets_exist(
            specifications,
            datasets={"decision-notice": {}},
        )

    def test_datasets_exist_fails_when_dataset_is_unknown(self):
        specifications = {
            "decision-stage": {
                "datasets": [{"dataset": "missing-dataset"}]
            }
        }

        assert not specification_checks.check_datasets_exist(
            specifications,
            datasets={"decision-notice": {}},
        )

    def test_datasets_exist_passes_when_all_datasets_are_known(self):
        specifications = {
            "decision-stage": {
                "datasets": [{"dataset": "decision-notice"}]
            }
        }

        assert specification_checks.check_datasets_exist(
            specifications,
            datasets={"decision-notice": {}},
        )

    def test_dataset_fields_fail_when_field_attribute_is_missing(self):
        specifications = {
            "decision-stage": {
                "datasets": [
                    {
                        "dataset": "decision-notice",
                        "fields": [{}],
                    }
                ]
            }
        }

        datasets = {
            "decision-notice": {
                "fields": [{"field": "decision"}]
            }
        }

        assert not specification_checks.check_dataset_fields(specifications, datasets)

    def test_dataset_fields_fail_when_field_not_defined_on_dataset(self):
        specifications = {
            "decision-stage": {
                "datasets": [
                    {
                        "dataset": "decision-notice",
                        "fields": [{"field": "decision-maker"}],
                    }
                ]
            }
        }

        datasets = {
            "decision-notice": {
                "fields": [{"field": "decision"}]
            }
        }

        assert not specification_checks.check_dataset_fields(specifications, datasets)

    def test_dataset_fields_pass_when_fields_match_dataset_definition(self):
        specifications = {
            "decision-stage": {
                "datasets": [
                    {
                        "dataset": "decision-notice",
                        "fields": [
                            {"field": "decision"},
                            {"field": "decision-maker"},
                        ],
                    }
                ]
            }
        }

        datasets = {
            "decision-notice": {
                "fields": [
                    {"field": "decision"},
                    {"field": "decision-maker"},
                ]
            }
        }

        assert specification_checks.check_dataset_fields(specifications, datasets)


class TestCombinedApplicationTypeIntegrityChecks:
    def write_combined_csv(self, tmp_path, rows):
        csv_path = tmp_path / "combined-application-types.csv"
        headers = [
            "application-types",
            "name",
            "description",
            "notes",
            "entry-date",
            "start-date",
            "end-date",
        ]
        lines = [",".join(headers)]
        lines.extend(rows)
        csv_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return csv_path

    def patch_combined_paths(self, monkeypatch, csv_path, planning_types_path=None):
        monkeypatch.setattr(application_checks, "COMBINED_APPLICATION_TYPES_PATH", csv_path)
        if planning_types_path is None:
            planning_types_path = csv_path.parent / "planning-application-type.csv"
        monkeypatch.setattr(
            application_checks,
            "PLANNING_APPLICATION_TYPE_PATH",
            planning_types_path,
        )

    def test_valid_combined_application_row_passes(self, tmp_path, monkeypatch):
        csv_path = self.write_combined_csv(
            tmp_path,
            [
                "hh;lbc,Householder and listed building consent,Valid combo,,2026-04-14,2026-04-14,"
            ],
        )
        self.patch_combined_paths(monkeypatch, csv_path)

        errors = []
        warnings = []
        monkeypatch.setattr(
            application_checks, "print_error", lambda element, name, message: errors.append(message)
        )
        monkeypatch.setattr(
            application_checks,
            "print_warning",
            lambda element, name, message: warnings.append(message),
        )

        result = application_checks.check_combined_application_type_rows(
            {"hh": {}, "lbc": {}}
        )

        assert result is True
        assert errors == []
        assert warnings == []

    def test_non_canonical_order_fails(self, tmp_path, monkeypatch):
        csv_path = self.write_combined_csv(
            tmp_path,
            [
                "lbc;hh,Householder and listed building consent,Wrong order,,2026-04-14,2026-04-14,"
            ],
        )
        self.patch_combined_paths(monkeypatch, csv_path)

        errors = []
        monkeypatch.setattr(
            application_checks, "print_error", lambda element, name, message: errors.append(message)
        )
        monkeypatch.setattr(application_checks, "print_warning", lambda *args: None)

        result = application_checks.check_combined_application_type_rows(
            {"hh": {}, "lbc": {}}
        )

        assert result is False
        assert any("canonical alphabetical order 'hh;lbc'" in message for message in errors)

    def test_unknown_application_type_fails(self, tmp_path, monkeypatch):
        csv_path = self.write_combined_csv(
            tmp_path,
            [
                "hh;missing,Householder and missing type,Unknown member,,2026-04-14,2026-04-14,"
            ],
        )
        self.patch_combined_paths(monkeypatch, csv_path)

        errors = []
        monkeypatch.setattr(
            application_checks, "print_error", lambda element, name, message: errors.append(message)
        )
        monkeypatch.setattr(application_checks, "print_warning", lambda *args: None)

        result = application_checks.check_combined_application_type_rows({"hh": {}})

        assert result is False
        assert any("references unknown application type 'missing'" in message for message in errors)

    def test_duplicate_combination_fails(self, tmp_path, monkeypatch):
        csv_path = self.write_combined_csv(
            tmp_path,
            [
                "hh;lbc,Householder and listed building consent,First row,,2026-04-14,2026-04-14,",
                "hh;lbc,Householder and listed building consent,Duplicate row,,2026-04-14,2026-04-14,",
            ],
        )
        self.patch_combined_paths(monkeypatch, csv_path)

        errors = []
        monkeypatch.setattr(
            application_checks, "print_error", lambda element, name, message: errors.append(message)
        )
        monkeypatch.setattr(application_checks, "print_warning", lambda *args: None)

        result = application_checks.check_combined_application_type_rows(
            {"hh": {}, "lbc": {}}
        )

        assert result is False
        assert any("duplicate combined application type 'hh;lbc'" in message for message in errors)

    def test_blank_start_date_warns_but_passes(self, tmp_path, monkeypatch):
        csv_path = self.write_combined_csv(
            tmp_path,
            [
                "hh;lbc,Householder and listed building consent,Inactive combo,,2026-04-14,,"
            ],
        )
        self.patch_combined_paths(monkeypatch, csv_path)

        errors = []
        warnings = []
        monkeypatch.setattr(
            application_checks, "print_error", lambda element, name, message: errors.append(message)
        )
        monkeypatch.setattr(
            application_checks,
            "print_warning",
            lambda element, name, message: warnings.append(message),
        )

        result = application_checks.check_combined_application_type_rows(
            {"hh": {}, "lbc": {}}
        )

        assert result is True
        assert errors == []
        assert any("recognised but inactive" in message for message in warnings)

    def test_three_or_more_application_types_warns_but_passes(
        self, tmp_path, monkeypatch
    ):
        csv_path = self.write_combined_csv(
            tmp_path,
            [
                "advertising;full;lbc,Three-way combo,Three members,,2026-04-14,2026-04-14,"
            ],
        )
        self.patch_combined_paths(monkeypatch, csv_path)

        errors = []
        warnings = []
        monkeypatch.setattr(
            application_checks, "print_error", lambda element, name, message: errors.append(message)
        )
        monkeypatch.setattr(
            application_checks,
            "print_warning",
            lambda element, name, message: warnings.append(message),
        )

        result = application_checks.check_combined_application_type_rows(
            {"advertising": {}, "full": {}, "lbc": {}}
        )

        assert result is True
        assert errors == []
        assert any("three or more application types" in message for message in warnings)

    def test_invalid_date_ordering_fails(self, tmp_path, monkeypatch):
        csv_path = self.write_combined_csv(
            tmp_path,
            [
                "hh;lbc,Householder and listed building consent,Bad dates,,2026-04-14,2026-04-15,2026-04-13"
            ],
        )
        self.patch_combined_paths(monkeypatch, csv_path)

        errors = []
        monkeypatch.setattr(
            application_checks, "print_error", lambda element, name, message: errors.append(message)
        )
        monkeypatch.setattr(application_checks, "print_warning", lambda *args: None)

        result = application_checks.check_combined_application_type_rows(
            {"hh": {}, "lbc": {}}
        )

        assert result is False
        assert any("'end-date' must not be earlier than 'start-date'" in message for message in errors)


class TestCodelistSourceData:
    def test_codelist_field_references_pass_when_fields_exist(self):
        codelists = {
            "specification/codelist/test.schema.md": {
                "fields": [
                    {"field": "reference"},
                    {"field": "name"},
                ],
            }
        }

        assert check_codelist_field_references(
            codelists,
            fields={"reference": {}, "name": {}},
        )

    def test_codelist_field_references_fail_when_field_missing(self):
        codelists = {
            "specification/codelist/test.schema.md": {
                "fields": [
                    {"field": "reference"},
                    {"field": "missing-field"},
                ],
            }
        }

        assert not check_codelist_field_references(
            codelists,
            fields={"reference": {}},
        )

    def test_codelist_declared_fields_pass_when_source_columns_exist(self, project_root):
        source_path = project_root / "data" / "test-codelist-validation.csv"
        source_path.write_text(
            "\n".join(
                [
                    "reference,name",
                    "outline,Outline",
                ]
            ),
            encoding="utf-8",
        )

        try:
            codelists = {
                "specification/codelist/test.schema.md": {
                    "source": "data/test-codelist-validation.csv",
                    "fields": [
                        {"field": "reference"},
                        {"field": "name"},
                    ],
                }
            }

            assert check_codelist_declared_fields_present(codelists)
        finally:
            source_path.unlink(missing_ok=True)

    def test_codelist_declared_fields_fail_when_source_column_missing(
        self, project_root
    ):
        source_path = project_root / "data" / "test-codelist-validation.csv"
        source_path.write_text(
            "\n".join(
                [
                    "reference,name",
                    "outline,Outline",
                ]
            ),
            encoding="utf-8",
        )

        try:
            codelists = {
                "specification/codelist/test.schema.md": {
                    "source": "data/test-codelist-validation.csv",
                    "fields": [
                        {"field": "reference"},
                        {"field": "missing-field"},
                    ],
                }
            }

            assert not check_codelist_declared_fields_present(codelists)
        finally:
            source_path.unlink(missing_ok=True)

    def test_codelist_usage_source_passes_when_usage_csv_exists(self):
        codelists = {
            "specification/codelist/tenure-type.schema.md": {
                "usage": "data/usage/tenure-type-usage.csv",
            }
        }

        assert check_codelist_usage_source(codelists)

    def test_codelist_usage_source_fails_when_path_is_not_usage_csv(self):
        codelists = {
            "specification/codelist/test.schema.md": {
                "usage": "data/codelist/test.csv",
            }
        }

        assert not check_codelist_usage_source(codelists)

    def test_parent_column_allows_valid_parent_reference(self, project_root):
        source_path = project_root / "data" / "test-codelist-validation.csv"
        source_path.write_text(
            "\n".join(
                [
                    "reference,name,parent",
                    "outline,Outline,",
                    "outline-all,Outline all,outline",
                ]
            ),
            encoding="utf-8",
        )

        try:
            codelists = {
                "specification/codelist/test.schema.md": {
                    "codelist": "test-codelist",
                    "source": "data/test-codelist-validation.csv",
                    "fields": [
                        {"field": "reference"},
                        {"field": "name"},
                        {"field": "parent"},
                    ],
                    "key-field": "reference",
                }
            }

            assert check_codelist_parent_references(codelists)
        finally:
            source_path.unlink(missing_ok=True)

    def test_parent_column_rejects_unknown_parent_reference(self, project_root):
        source_path = project_root / "data" / "test-codelist-validation.csv"
        source_path.write_text(
            "\n".join(
                [
                    "reference,name,parent",
                    "outline-all,Outline all,missing-parent",
                ]
            ),
            encoding="utf-8",
        )

        try:
            codelists = {
                "specification/codelist/test.schema.md": {
                    "codelist": "test-codelist",
                    "source": "data/test-codelist-validation.csv",
                    "fields": [
                        {"field": "reference"},
                        {"field": "name"},
                        {"field": "parent"},
                    ],
                    "key-field": "reference",
                }
            }

            assert not check_codelist_parent_references(codelists)
        finally:
            source_path.unlink(missing_ok=True)

    def test_missing_parent_column_fails_when_declared(self, project_root):
        source_path = project_root / "data" / "test-codelist-validation.csv"
        source_path.write_text(
            "\n".join(
                [
                    "reference,name",
                    "outline,Outline",
                ]
            ),
            encoding="utf-8",
        )

        try:
            codelists = {
                "specification/codelist/test.schema.md": {
                    "codelist": "test-codelist",
                    "source": "data/test-codelist-validation.csv",
                    "fields": [
                        {"field": "reference"},
                        {"field": "name"},
                        {"field": "parent"},
                    ],
                    "key-field": "reference",
                }
            }

            assert not check_codelist_parent_column(codelists)
        finally:
            source_path.unlink(missing_ok=True)

    def test_blank_reference_fails(self, project_root):
        source_path = project_root / "data" / "test-codelist-validation.csv"
        source_path.write_text(
            "\n".join(
                [
                    "reference,name",
                    ",Outline",
                ]
            ),
            encoding="utf-8",
        )

        try:
            codelists = {
                "specification/codelist/test.schema.md": {
                    "codelist": "test-codelist",
                    "source": "data/test-codelist-validation.csv",
                    "fields": [
                        {"field": "reference"},
                        {"field": "name"},
                    ],
                    "key-field": "reference",
                }
            }

            assert not check_codelist_blank_keys(codelists)
        finally:
            source_path.unlink(missing_ok=True)

    def test_duplicate_reference_fails(self, project_root):
        source_path = project_root / "data" / "test-codelist-validation.csv"
        source_path.write_text(
            "\n".join(
                [
                    "reference,name",
                    "outline,Outline",
                    "outline,Outline duplicate",
                ]
            ),
            encoding="utf-8",
        )

        try:
            codelists = {
                "specification/codelist/test.schema.md": {
                    "codelist": "test-codelist",
                    "source": "data/test-codelist-validation.csv",
                    "fields": [
                        {"field": "reference"},
                        {"field": "name"},
                    ],
                    "key-field": "reference",
                }
            }

            assert not check_codelist_duplicate_keys(codelists)
        finally:
            source_path.unlink(missing_ok=True)
