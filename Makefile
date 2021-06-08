all: mutants

module = stellar_occultations
codecov_token = 44c9b437-8178-48cd-995e-b4b09f348ae5

.PHONY: all clean coverage format install mutants tests

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
	rm --force coverage.xml
	rm --force .coverage
	rm --force .mutmut-cache

coverage: install
	pytest --cov=${module} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}

