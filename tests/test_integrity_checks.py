# tests/test_integrity_checks.py
import pytest

from bin.integrity_checks import applications as application_checks
from bin.integrity_checks.components import check_field_condition_references
from bin.integrity_checks.codelists import (
    check_codelist_blank_keys,
    check_codelist_duplicate_keys,
    check_codelist_parent_column,
    check_codelist_parent_references,
)
from bin.integrity_checks.modules import (
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
