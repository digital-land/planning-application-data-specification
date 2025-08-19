# current git branch
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

init::
	python -m pip install --upgrade pip
	python -m pip install pip-tools
	python -m piptools compile explorer/requirements/dev-requirements.in
	python -m piptools compile explorer/requirements/requirements.in
	python -m piptools sync explorer/requirements/dev-requirements.txt explorer/requirements/requirements.txt


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


clean::
	rm -r generated


build: clean
	mkdir -p generated
	python3 bin/build.py


status:
	git status --ignored


commit-issue-tracking::
	git add .
	git diff --quiet && git diff --staged --quiet || (git commit -m "Latest issue tracking updates $(shell date +%F)"; git push origin $(BRANCH))
