FROM python:3.11.3-slim-buster as base

# environment variables
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE="false" \
    PIP_NO_CACHE_DIR="false" \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYSETUP_PATH="/opt/pysetup"

ENV PATH="$POETRY_HOME/bin:$PATH"

# apt
RUN apt update && \
    apt upgrade && \
    apt install -y curl libpq-dev build-essential && \
    apt clean

# install poetry
RUN curl -sSL https://install.python-poetry.org | python -

# create app directory
RUN mkdir /app
WORKDIR /app

# copy pyproject.toml and poetry.lock
COPY ./poetry.lock ./pyproject.toml /app/
RUN poetry install --no-root

FROM base as dev
RUN poetry install --no-root
RUN apt install -y git && apt clean

FROM base as prod
RUN poetry install --only main --no-root
COPY . /app
COPY ./docker/entrypoint.sh /app/entrypoint.sh
RUN chmod 755 entrypoint.sh