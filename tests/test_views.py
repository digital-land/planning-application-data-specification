from copy import deepcopy
import pytest
from planning_application_specification import Specification
from planning_application_specification.views import view_errors
from integrity_checks.specifications import check_views


@pytest.fixture
def spec(project_root):
    return Specification.load(project_root)


def test_real_view_selection_resolution_and_filters(spec):
    view = spec.view('national-public')
    definition = spec.tables['specification']['national-public-view']
    assert [d.ref for d in view.datasets()] == [d['dataset'] for d in definition['datasets']]
    for entry in definition['datasets']:
        items = view.resolve_container_items(dataset=entry['dataset'])
        assert [f.ref for f in items] == [f['field'] for f in entry['fields']]
    field = view.resolve_field('description', dataset='planning-application')
    assert field.requirement_level == 'MUST'
    assert field.base is spec.field('description')
    assert field.dataset_field.container_kind == 'dataset'
    assert field.datatype == field.dataset_field.datatype
    assert field.cardinality == field.dataset_field.cardinality
    assert view.dataset('planning-application').record_inclusion is None
    filtered = [d for d in view.datasets() if d.record_inclusion]
    assert any(d.record_inclusion['include-values'] == ['publish'] for d in filtered)
    assert any(isinstance(d.record_inclusion['include-values'], dict) for d in filtered)
    assert check_views({'national-public-view': definition}, spec.tables['dataset'])
    with pytest.raises(KeyError):
        view.resolve_field('officer-name', dataset='planning-application')
    with pytest.raises(KeyError):
        view.dataset('not-selected')
    with pytest.raises(KeyError):
        spec.view('missing')


def test_precedence_and_independent_requirements(spec):
    definition = {'datasets': [{'dataset': 'planning-application', 'fields': [
        {'field': 'officer-name'}, {'field': 'description', 'name': 'View name', 'description': ''}]}]}
    spec.tables['specification']['test-view'] = definition
    view = spec.view('test')
    officer = view.resolve_field('officer-name', dataset='planning-application')
    assert officer.name == 'Case officer'
    description = view.resolve_field('description', dataset='planning-application')
    assert description.name == 'View name'
    assert description.description == ''
    assert description.requirement_level is None
    assert description.dataset_field.requirement_level == 'MUST'
    description.usage.overrides['name'] = 'changed'
    assert definition['datasets'][0]['fields'][1]['name'] == 'View name'


@pytest.mark.parametrize('mutation', ['duplicate-dataset', 'duplicate-field', 'unknown-field', 'datatype', 'cardinality', 'requirement', 'filter'])
def test_authoring_and_resolver_share_validation(spec, mutation):
    definition = {'datasets': [{'dataset': 'planning-application', 'fields': [{'field': 'description'}]}]}
    entry = definition['datasets'][0]
    if mutation == 'duplicate-dataset':
        definition['datasets'].append(deepcopy(entry))
    elif mutation == 'duplicate-field':
        entry['fields'].append({'field': 'description'})
    elif mutation == 'unknown-field':
        entry['fields'][0]['field'] = 'missing'
    elif mutation in ('datatype', 'cardinality'):
        entry['fields'][0][mutation] = 'string'
    elif mutation == 'requirement':
        entry['fields'][0]['requirement-level'] = 'sometimes'
    else:
        entry['record-inclusion'] = {'field': 'missing', 'include-values': []}
    errors = view_errors('test-view', definition, spec.tables['dataset'])
    assert errors
    assert not check_views({'test-view': definition}, spec.tables['dataset'])
    spec.tables['specification']['test-view'] = definition
    with pytest.raises(ValueError) as exc:
        spec.view('test')
    assert str(exc.value) == '\n'.join(errors)
