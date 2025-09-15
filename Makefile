# current git branch
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

init::
	python -m pip install --upgrade pip
	python -m pip install pip-tools
	python -m piptools compile requirements/dev-requirements.in
	python -m piptools compile requirements/requirements.in
	python -m piptools sync requirements/dev-requirements.txt requirements/requirements.txt


checks:
	python3 bin/check.py


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


build: clean
	mkdir -p generated
	python3 bin/build.py


status:
	git status --ignored


commit-issue-tracking::
	git add .
	git diff --quiet && git diff --staged --quiet || (git commit -m "Latest issue tracking updates $(shell date +%F)"; git push origin $(BRANCH))


commit-outputs:
	git add generated/
	git diff --quiet && git diff --staged --quiet || (git commit -m "Latest generated outputs $(shell date +%F)"; git push origin $(BRANCH))
