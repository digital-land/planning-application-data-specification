# Do Not Remove or Delete

The specification viewer has moved to the [new specification viewer](https://digital-land.github.io/planning-application-specification-viewer/).

The pages in this folder occupy the old viewer URLs. Keep them so those URLs can redirect visitors to equivalent pages in the new viewer. Keep GitHub Pages serving `main` from `/docs` and do not delete, rename, clean or regenerate these pages. The files in `docs/static/` also preserve existing asset and download URLs.

The checked-in HTML does not currently contain the redirect blocks. The redirect maintenance tool is `bin/inject_viewer_redirects.py`; run it before relying on the old URLs to forward visitors. Use `make serve-github-pages` to preview the pages.
