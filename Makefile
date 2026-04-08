.PHONY: tests

# current git branch
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

# Pin versions known to work together
PINNED_PIP      := 25.2
PINNED_PIPTOOLS := 7.5.1

init::
	# Tooling (pin pip to avoid CI drift)
	python -m pip install --upgrade "pip==$(PINNED_PIP)" "setuptools>=68" "wheel>=0.42" "build>=1.0.0"
	python -m pip install "pip-tools==$(PINNED_PIPTOOLS)"

	# Compile from .in to .txt (use backtracking resolver for consistency)
	python -m piptools compile --resolver=backtracking requirements/requirements.in
	python -m piptools compile --resolver=backtracking requirements/dev-requirements.in

	# Sync the environment to the compiled lock files
	python -m piptools sync requirements/dev-requirements.txt requirements/requirements.txt


checks:
	python3 bin/check.py

tests:
	pytest -q


codelists:
	python3 bin/build_codelists.py


issue-tracking-data:
	python3 bin/extract_github_issues.py


declarative-progress:
	python spec.py summary --markdown > issue-tracking/declarative-model-progress.md


specification::
	python3 bin/specification_data.py


spreadsheets::
	python3 bin/generate_spec_spreadsheet.py

export-elements::
	python3 bin/export_elements.py

export-elements-xlsx::
	python3 bin/export_elements.py --xlsx data/element-index/elements.xlsx

jsonschema::
	python3 bin/generate_json_schema.py

clean-static-site::
	rm -rf docs
	mkdir -p docs

copy-assets::
	mkdir -p docs/static/{stylesheets,javascripts}
	cp -r bin/assets/javascripts docs/static/

render-local-site:: clean-static-site copy-assets
	python3 bin/render_static_site.py --output docs --base-url ""

render-github-pages:: clean-static-site copy-assets
	python3 bin/render_static_site.py --output docs

serve-github-pages::
	# Local preview: serve docs at root; URLs will use whatever base-url you rendered with
	python3 -m http.server 8000 --bind :: -d docs

clean::
	rm -rf generated
	mkdir -p generated

copy-output-docs: 
	cp documentation/generating-outputs-from-model.md generated/README.md

build: clean copy-output-docs
	python3 bin/build.py


status:
	git status --ignored


changelog:
	git-chglog -o CHANGELOG.md


commit-issue-tracking::
	git add .
	git diff --quiet && git diff --staged --quiet || (git commit -m "Latest issue tracking updates $(shell date +%F)"; git push origin $(BRANCH))


commit-outputs:
	git add generated/
	git diff --quiet && git diff --staged --quiet || (git commit -m "Latest generated outputs $(shell date +%F)"; git push origin $(BRANCH))
