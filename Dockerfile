FROM tiangolo/meinheld-gunicorn:python3.7

COPY ./datanator_rest_api /datanator_rest_api
WORKDIR /datanator_rest_api
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile