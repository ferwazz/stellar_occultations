mutants:
	mutmut run \
		--paths-to-mutate stellar_occultations

.PHONY: clean install mutants tests

install:
	pip install --editable .

format:
	black -l 100 stellar_occultations
	black -l 100 tests

tests: install
	pytest --verbose

clean:
	rm --recursive --force .pytest_cache
	rm --recursive --force tests/__pycache__
	rm --recursive --force stellar_occultations/__pycache__
	rm --recursive --force stellar_occultations.egg-info
	rm --force .mutmut-cache