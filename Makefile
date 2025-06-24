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


issue-tracking-report:
	python3 bin/issue_tracking_output.py


status:
	git status --ignored


commit-issue-tracking::
	git add .
	git diff --quiet && git diff --staged --quiet || (git commit -m "Latest issue tracking updates $(shell date +%F)"; git push origin $(BRANCH))
