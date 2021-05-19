FROM python:3
COPY . .
RUN pip install --upgrade pip && pip install \
    black \
    numpy \
    pandas \
    pytest==5.0.1 \
    matplotlib \
    ipykernel \
    mutmut \
    rope


