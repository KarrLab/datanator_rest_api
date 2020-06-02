# syntax=docker/dockerfile:experimental
FROM python:3.7-slim-buster


COPY ./nginx/install-nginx.sh .

RUN bash install-nginx.sh

EXPOSE 80

# Expose 443, in case of LTS / HTTPS
EXPOSE 443

# -- Adding Pipfiles
COPY Pipfile ./
COPY Pipfile.lock ./

# -- Install dependencies:
RUN ls -l . \
    && pip install pipenv \
    && set -ex && pipenv install --deploy --system

COPY . ./
RUN pip install -e .

ENV PORT=80

# Download public key for github.com
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts \
    && ls -l ~/.ssh

# Clone private repository
RUN --mount=type=ssh git clone git@github.com:KarrLab/karr_lab_build_config.git /.wc \
    && ls -l /

CMD gunicorn --bind 0.0.0.0:8080 "datanator_rest_api.core:application"
