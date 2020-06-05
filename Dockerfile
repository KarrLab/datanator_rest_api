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

EXPOSE 80/tcp

# clean up
RUN  apt-get purge -y --autoremove git ca-certificates \
     && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/nginx.list \
     && if [ -n "$tempDir" ]; then \
        apt-get purge -y --auto-remove \
        && rm -rf "$tempDir" /etc/apt/sources.list.d/temp.list; \
     fi 

CMD gunicorn --bind 127.0.0.1:80 "datanator_rest_api.core:application" 
    # && sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/nginx.conf \
    # && nginx -g 'daemon off;'