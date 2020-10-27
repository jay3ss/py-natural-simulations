help:
	@echo "make init"
	@echo "		initialize the project"
	@echo "make init-dev"
	@echo "		intialize the project for development"

init:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

init-dev:
	make init
	python -m pip install -r dev-requirements.txt

test:
	python -m unittest discover
