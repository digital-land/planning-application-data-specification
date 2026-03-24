from bin import forms


def test_load_2025_form_data_uses_analysis_path(monkeypatch):
    calls = []

    def fake_read_csv(path, as_dict=False):
        calls.append((path, as_dict))
        return [{"application-types": "hh;full"}]

    monkeypatch.setattr(forms, "read_csv", fake_read_csv)

    data = forms.load_2025_form_data()

    assert calls == [(forms.FORMS_2025_FILEPATH, True)]
    assert data == [{"application-types": ["hh", "full"]}]


def test_get_2025_form_returns_matching_form():
    form_data = [
        {"reference": "form-a", "name": "Form A", "application-types": ["hh"]},
        {"reference": "form-b", "name": "Form B", "application-types": ["full"]},
    ]

    result = forms.get_2025_form("form-b", form_data)

    assert result == {"reference": "form-b", "name": "Form B", "application-types": ["full"]}


def test_get_2025_forms_by_refs_returns_matches_in_requested_order():
    form_data = [
        {"reference": "form-a", "name": "Form A", "application-types": ["hh"]},
        {"reference": "form-b", "name": "Form B", "application-types": ["full"]},
    ]

    result = forms.get_2025_forms_by_refs(["form-b", "missing", "form-a"], form_data)

    assert [form["reference"] for form in result] == ["form-b", "form-a"]
