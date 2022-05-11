FROM fnndsc/python-poetry

WORKDIR /app/

COPY pyproject.toml poetry.lock /app/

RUN poetry install

COPY . /app/