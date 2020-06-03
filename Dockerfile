FROM python:3.7-slim-buster

COPY ./nginx/install-nginx.sh .

RUN bash install-nginx.sh

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
EXPOSE 443
EXPOSE 8080

# -- Adding Pipfiles
COPY Pipfile ./
COPY Pipfile.lock ./

# -- Install dependencies:
RUN pip install pipenv \
    && set -ex && pipenv install --deploy --system

COPY . ./
RUN pip install -e .

# # Download public key for github.com
# RUN mkdir -m 700 /root/.ssh; \
#   touch -m 600 /root/.ssh/known_hosts; \
#   ssh-keyscan github.com > /root/.ssh/known_hosts

# # Clone private repository
# RUN --mount=type=ssh,id=github git clone git@github.com:KarrLab/karr_lab_build_config.git /.wc
ARG PORT=80
ENV  PORT=${PORT}
ENV  PRODUCTION=${PRODUCTION}
ENV  MONGO_USERNAME=${MONGO_USERNAME}
ENV  MONGO_PASSWORD=${MONGO_PASSWORD}
ENV  MONGO_DATANATOR_SERVER=${MONGO_DATANATOR_SERVER}
ENV  MONGO_AUTHDB=${MONGO_AUTHDB}
ENV  REST_FTX_AWS_PROFILE=${REST_FTX_AWS_PROFILE}
ENV  REST_FTX_ENDPOINT=${REST_FTX_ENDPOINT}
ENV  REST_FTX_AWS_ACCESS_KEY_ID=${REST_FTX_AWS_ACCESS_KEY_ID}
ENV  REST_FTX_AWS_SECRET_ACCESS_KEY=${REST_FTX_AWS_SECRET_ACCESS_KEY}
ENV  REST_FTX_AWS_DEFAULT_REGION=${REST_FTX_AWS_DEFAULT_REGION}

CMD gunicorn --bind 0.0.0.0:8080 "datanator_rest_api.core:application" --daemon  && \
    sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf && \
    nginx -g 'daemon off;'