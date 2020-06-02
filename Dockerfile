FROM python:3.7

RUN pip install pipenv

COPY . /datanator_rest_api
WORKDIR /datanator_rest_api

# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
RUN set -ex && pipenv install --deploy --system \
    && pip install -e /datanator_rest_api 

CMD gunicorn --bind 0.0.0.0:8080 "datanator_rest_api.core:application"