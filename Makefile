.PHONY: start_virtual_env run flake8

start_virtual_env:
	pipenv shell

run:
	python -m titanic

flake8:
	pipenv run flake8
