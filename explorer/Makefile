init::
	python -m pip install --upgrade pip
	python -m pip install pip-tools
	python -m piptools compile requirements/dev-requirements.in
	python -m piptools compile requirements/requirements.in
	python -m piptools sync requirements/dev-requirements.txt requirements/requirements.txt


specifications:
	python pacli.py app-type --generate-specification-index  
	python pacli.py app-type --all --generate-application
