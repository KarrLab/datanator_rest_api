FROM tiangolo/meinheld-gunicorn:python3.7

RUN pip install pipenv

COPY . /datanator_rest_api
WORKDIR /datanator_rest_api

# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
RUN set -ex && pipenv install --deploy --system