

test t:
	pytest --cov-report term --cov-report html --cov=ds

test-watch tw:
	ls ds.py test/*.py | entr -s 'clear && pytest'
