FROM python:3.7-slim-buster

WORKDIR /ecs

COPY ./nginx/install-nginx.sh .

RUN bash install-nginx.sh

COPY ./nginx/default.conf /etc/nginx/nginx.conf
RUN rm -rf /etc/nginx/conf.d

# -- Adding Pipfiles
COPY Pipfile ./
COPY Pipfile.lock ./

# -- Install dependencies:
RUN pip install pipenv \
    && set -ex && pipenv install --deploy --system

COPY . ./
RUN pip install -e .

ENV  PORT=80
ENV  PRODUCTION=$PRODUCTION
ENV  MONGO_USERNAME=$MONGO_USERNAME
ENV  MONGO_PASSWORD=$MONGO_PASSWORD
ENV  MONGO_DATANATOR_SERVER=$MONGO_DATANATOR_SERVER
ENV  MONGO_AUTHDB=$MONGO_AUTHDB
ENV  REST_FTX_AWS_PROFILE=$REST_FTX_AWS_PROFILE
ENV  REST_FTX_ENDPOINT=$REST_FTX_ENDPOINT
ENV  REST_FTX_AWS_ACCESS_KEY_ID=$REST_FTX_AWS_ACCESS_KEY_ID
ENV  REST_FTX_AWS_SECRET_ACCESS_KEY=$REST_FTX_AWS_SECRET_ACCESS_KEY
ENV  REST_FTX_AWS_DEFAULT_REGION=$REST_FTX_AWS_DEFAULT_REGION

EXPOSE 80/tcp
EXPOSE 8080/tcp

CMD gunicorn --bind 127.0.0.1:8080 "datanator_rest_api.core:application" --daemon \
    && sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/nginx.conf \
    && nginx -g 'daemon off;'