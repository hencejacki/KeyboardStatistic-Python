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
	@echo clean

clean:
	pip uninstall $(PROJECT_NAME)

exit:
	@kill -9 `cat ~/.ks/ks.pid`

test:
	python tests/test_monitor.py

.PHONY: init run help clean exit test