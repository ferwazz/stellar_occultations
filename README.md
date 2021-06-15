[![codecov](https://codecov.io/gh/ferwazz/stellar_occultations/branch/develop/graph/badge.svg?token=8NOM5AFH66)](https://codecov.io/gh/ferwazz/stellar_occultations)
![tests](https://github.com/ferwazz/stellar_occultations/actions/workflows/tests.yml/badge.svg)
![mutants](https://github.com/ferwazz/stellar_occultations/actions/workflows/mutants.yml/badge.svg)

# Python package `stellar-occultations`

## To install use:

```
pip install git+https://github.com/ferwazz/stellar_occultations.git
```


### Demo with Docker

```Makefile
build_demo:
	docker build --file Dockerfile.demo --tag=stellar_occultations/demo .

run_demo:
	docker run --publish 8080:8888 --rm stellar_occultations/demo
