FROM python:3.7

WORKDIR /app

# -- Adding Pipfiles
COPY Pipfile ./
COPY Pipfile.lock ./

# -- Install dependencies:
RUN pip install pipenv \
    && set -ex && pipenv install --deploy --system

COPY . ./
RUN pip install -e .

ENV PORT=80

# CMD gunicorn --bind 0.0.0.0:8080 "datanator_rest_api.core:application"
ENTRYPOINT bash