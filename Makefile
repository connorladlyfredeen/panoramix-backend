init:
	virtualenv -p python3 venv; . venv/bin/activate; pip install -r requirements.txt;
test:
	export PYTHONPATH='.'; . venv/bin/activate; pytest;
travis-test:
	export PYTHONPATH='.'; pytest;
