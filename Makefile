help:
	@echo "make init"
	@echo "		initialize the project"
	@echo "make init-dev"
	@echo "		intialize the project for development"
	@echo "make clean-pyc"
	@echo "		remove python artifacts"

init:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

init-dev:
	make init
	python -m pip install -r dev-requirements.txt

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +

test:
	python -m unittest discover
