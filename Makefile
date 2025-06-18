init::
	python -m pip install --upgrade pip
	python -m pip install pip-tools
	python -m piptools compile explorer/requirements/dev-requirements.in
	python -m piptools compile explorer/requirements/requirements.in
	python -m piptools sync explorer/requirements/dev-requirements.txt explorer/requirements/requirements.txt


checks:
	python3 bin/check.py
