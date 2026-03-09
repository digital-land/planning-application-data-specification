# tests/test_integrity_checks.py
import pytest
from bin.integrity_checks.components import check_field_condition_references
from bin.integrity_checks.codelists import check_codelist_source_data
from bin.integrity_checks.modules import (
    check_all,
    check_applies_if_structure,
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


class TestCodelistSourceData:
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

            assert check_codelist_source_data(codelists)
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

            assert not check_codelist_source_data(codelists)
        finally:
            source_path.unlink(missing_ok=True)
