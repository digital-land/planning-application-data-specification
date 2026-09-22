import pytest
from planning_application_specification import Specification


def test_real_specification(project_root):
    spec = Specification.load(project_root)
    assembly = spec.specification('planning-application-data')
    authored = spec.tables['specification']['planning-application-data']
    assert [d.ref for d in assembly.datasets()] == [d['dataset'] for d in authored['datasets']]
    for entry in authored['datasets']:
        items = assembly.resolve_container_items(dataset=entry['dataset'])
        assert [f.ref for f in items] == [f['field'] for f in entry['fields']]
    field = assembly.resolve_field('discharged-by', dataset='decision-condition')
    assert field.target_dataset == 'decision-notice'
    assert field.requirement_level == 'MUST'
    assert field.base is spec.field('discharged-by')
    assert field.specification_ref == 'planning-application-data'
    with pytest.raises(KeyError):
        assembly.dataset('missing')
    with pytest.raises(KeyError):
        assembly.resolve_field('missing', dataset='decision-condition')
    with pytest.raises(KeyError):
        spec.specification('missing')


def test_selection_and_fallback(project_root):
    spec = Specification.load(project_root)
    definition = {'datasets': [{'dataset': 'decision-condition'}]}
    spec.tables['specification']['test'] = definition
    assembly = spec.specification('test')
    assert len(assembly.resolve_container_items(dataset='decision-condition')) == len(spec.dataset('decision-condition').items)
    assert assembly.resolve_field('discharged-by', dataset='decision-condition').requirement_level == 'MUST'
    definition['datasets'][0]['fields'] = []
    assert spec.specification('test').resolve_container_items(dataset='decision-condition') == ()
    definition['datasets'][0]['fields'] = [{'field': 'discharged-by', 'name': 'Custom', 'requirement-level': 'MAY'}]
    field = spec.specification('test').resolve_field('discharged-by', dataset='decision-condition')
    assert field.name == 'Custom'
    assert field.requirement_level == 'MAY'
    assert field.dataset_field.requirement_level == 'MUST'
    assert assembly.resolve_field('discharged-by', dataset='decision-condition').name != 'Custom'


@pytest.mark.parametrize('extra', [{'datatype':'integer'}, {'cardinality':'0:9'}, {'codelist':'other'}, {'dataset':'site'}, {'requirement-level':'sometimes'}])
def test_invalid_overrides(project_root, extra):
    spec = Specification.load(project_root)
    spec.tables['specification']['test'] = {'datasets':[{'dataset':'decision-condition','fields':[{'field':'discharged-by', **extra}]}]}
    with pytest.raises(ValueError):
        spec.specification('test')


def test_matching_structural_declarations_and_duplicate_rejection(project_root):
    spec = Specification.load(project_root)
    base = spec.resolve_field('discharged-by', dataset='decision-condition')
    field = {'field':'discharged-by', 'datatype':base.datatype, 'cardinality':base.cardinality, 'dataset':base.target_dataset}
    definition = {'datasets':[{'dataset':'decision-condition','fields':[field]}]}
    spec.tables['specification']['test'] = definition
    resolved = spec.specification('test').resolve_field('discharged-by', dataset='decision-condition')
    assert resolved.datatype == base.datatype
    definition['datasets'][0]['fields'].append(dict(field))
    with pytest.raises(ValueError, match='duplicate selection'):
        spec.specification('test')
    definition['datasets'][0]['fields'] = [{'field':'unknown'}]
    with pytest.raises(ValueError, match='not defined'):
        spec.specification('test')
    definition['datasets'] = [{'dataset':'missing'}]
    with pytest.raises(ValueError, match='unknown dataset'):
        spec.specification('test')
