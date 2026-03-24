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
