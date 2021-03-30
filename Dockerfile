FROM python:3.8

RUN pip install \
    black \
    numpy \
    pandas \
    pytest==5.0.1 \
    matplotlib \
    ipykernel

WORKDIR /workdir
