PROJECT_NAME := ks

init:
	pip install -r requirements.txt

run:
	pip install -e .
	python scripts/run.py &

help:
	@echo init
	@echo run
	@echo help

clean:
	pip uninstall $(PROJECT_NAME)

.PHONY: init run help clean