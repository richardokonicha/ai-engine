.PHONY: virtualenv

VENV = venv

# Run a local web server
server: $(VENV)
	. $(VENV)/bin/activate; python main.py

run:
	python main.py
