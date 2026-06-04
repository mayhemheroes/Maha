FROM python:3.11-slim

RUN apt-get update && apt-get install -y clang gcc curl && rm -rf /var/lib/apt/lists/*
RUN CLANG_BIN=$(which clang) python3 -m pip install atheris
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY . /maha
WORKDIR /maha
ENV PATH="/root/.local/bin:$PATH"
RUN poetry build && python3 -m pip install dist/*.whl && chmod +x fuzz/fuzz_parser.py
