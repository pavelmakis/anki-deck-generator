VENV_BIN=.venv/bin

.PHONY: virtualenv
virtualenv:
	@python3 -m venv .venv --clear --upgrade-deps
	@echo
	@echo "Virtual environment installed into .venv/"
	@echo "Run 'source .venv/bin/activate' to activate it"

.PHONY: install
install:
	@$(VENV_BIN)/pip install -r requirements.txt

.PHONY: init
init: virtualenv install
