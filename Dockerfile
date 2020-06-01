FROM tiangolo/meinheld-gunicorn:python3.7

RUN pip install pipenv

COPY . /datanator_rest_api
WORKDIR /datanator_rest_api

# -- Adding Pipfiles
ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
ONBUILD RUN set -ex && pipenv install --deploy --system