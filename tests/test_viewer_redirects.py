from pathlib import Path

import pytest

from bin.inject_viewer_redirects import DESTINATION, inject, inject_site

PAGE = '<!doctype html><html><head><title>Old page</title></head><body class="old"><main>Original content</main></body></html>'


@pytest.mark.parametrize('path,route', [('index.html', ''), ('dataset/site/index.html', 'dataset/site/'), ('other.html', 'other.html')])
def test_redirect_destination_and_fallback(path, route):
    result = inject(PAGE, path)
    assert f'rel="canonical" href="{DESTINATION}{route}"' in result
    assert f'content="0; url={DESTINATION}{route}"' in result
    assert 'window.location.search + window.location.hash' in result
    assert 'window.location.replace(' in result
    assert 'Do not delete this page' in result
    assert '<main>Original content</main>' in result
    assert 'This page has moved' in result


def test_repeated_injection_is_unchanged():
    result = inject(PAGE, 'index.html')
    assert inject(result, 'index.html') == result


def test_site_keeps_downloads_and_validates_before_writing(tmp_path):
    page = tmp_path / 'index.html'
    page.write_text(PAGE)
    download = tmp_path / 'data.json'
    download.write_bytes(b'{"example": true}')
    bad = tmp_path / 'bad.html'
    bad.write_text('invalid')
    with pytest.raises(ValueError, match='Missing head or body'):
        inject_site(tmp_path)
    assert page.read_text() == PAGE
    bad.unlink()
    assert inject_site(tmp_path) == 1
    assert download.read_bytes() == b'{"example": true}'


def test_rejects_conflicting_canonical():
    with pytest.raises(ValueError, match='Existing canonical'):
        inject(PAGE.replace('</head>', '<link rel="canonical" href="other"></head>'), 'index.html')
