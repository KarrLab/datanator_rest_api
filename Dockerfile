FROM python:3.7-slim-buster

WORKDIR /ecs

COPY ./nginx/install-nginx.sh .

RUN bash install-nginx.sh

# RUN apt-get update \
#     && apt-get install --no-install-recommends --no-install-suggests -y gnupg1 ca-certificates git

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
ENV  READ_PREFERENCE=$READ_PREFERENCE
ENV  MONGO_ATLAS_SERVER=$MONGO_ATLAS_SERVER
ENV  MONGO_ATLAS_PORT=$MONGO_ATLAS_PORT
ENV  MONGO_ATLAS_REPL=$MONGO_ATLAS_REPL
ENV  MONGO_ATLAS_READPREFERENCE=$MONGO_ATLAS_READPREFERENCE
ENV  MONGO_ATLAS_AUTHDB=$MONGO_ATLAS_AUTHDB

EXPOSE 80/tcp

# clean up
RUN  apt-get purge -y --autoremove git \
     && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/nginx.list \
     && if [ -n "$tempDir" ]; then \
        apt-get purge -y --auto-remove \
        && rm -rf "$tempDir" /etc/apt/sources.list.d/temp.list; \
     fi 

CMD gunicorn --bind 127.0.0.1:8001 --graceful-timeout 30 --timeout 60 "datanator_rest_api.core:application" --daemon \
    && sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/nginx.conf \
    && nginx -g 'daemon off;'