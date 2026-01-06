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
	python -m piptools compile --resolver=backtracking requirements/dev-requirements.in
	python -m piptools compile --resolver=backtracking requirements/requirements.in

	# Sync the environment to the compiled lock files
	python -m piptools sync requirements/dev-requirements.txt requirements/requirements.txt


checks:
	python3 bin/check.py


codelists:
	python3 bin/build_codelists.py


issue-tracking-data:
	python3 bin/issue_tracking.py


issue-tracking-reports:
	python3 bin/issue_tracking_output.py


declarative-progress:
	python3 bin/declarative_tracking.py


specification::
	python3 bin/specification_data.py


spreadsheets::
	python3 bin/generate_spec_spreadsheet.py

jsonschema::
	python3 bin/generate_json_schema.py

clean::
	rm -rf generated
	mkdir -p generated

copy-output-docs: 
	cp docs/generating-outputs-from-model.md generated/README.md

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
