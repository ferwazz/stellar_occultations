FROM python:3.9
COPY . .
RUN pip install --upgrade pip && pip install \
    autopep8 \
    black \
    codecov \
    flake8 \
    ipykernel \
    matplotlib \
    mutmut \
    numpy \
    pandas \
    pylint \
    pytest-cov \
    pytest \
    rope
