

test t:
	pytest --cov-report term --cov-report html --cov=ds

test-watch tw:
	ls ds.rb test/*.py | entr -s 'clear && pytest'
