# Running the project
FROM python:3.10-alpine

WORKDIR /portifolio-app

COPY pyproject.toml poetry.lock /portifolio-app/

RUN apk update && \
    pip install --upgrade pip && \
    pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install && \
    poetry add gunicorn

COPY . /portifolio-app/

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "portifoliov1:create_app()"]