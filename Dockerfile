FROM python:3.10.0 as python-base

ENV PYTHONDONTWRITEBYTECODE = 1 \
    PYTHONUNBUFFERED = 1

COPY . .
WORKDIR .

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root


