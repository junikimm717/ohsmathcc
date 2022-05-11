FROM fnndsc/python-poetry

WORKDIR /app/

# plz install everything globally in docker
RUN poetry config virtualenvs.create false

# install the dependencies first
COPY pyproject.toml poetry.lock /app/

RUN poetry install

COPY . /app/

