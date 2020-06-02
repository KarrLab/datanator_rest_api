# syntax=docker/dockerfile:experimental
FROM nginx:stable-alpine


RUN apk update && apk add --no-cache python3 &&\
    python3 -m ensurepip &&\
    rm -r /usr/lib/python*/ensurepip &&\
    pip3 install --upgrade pip setuptools &&\
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi &&\
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache
RUN apk update && apk add --no-cache gcc python3-dev musl-dev libffi-dev openssl-dev make git

WORKDIR /app

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
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts

# Clone private repository
RUN --mount=type=ssh git clone git@github.com:KarrLab/karr_lab_build_config.git /.wc \
    && ls -l /

CMD gunicorn --bind 0.0.0.0:8080 "datanator_rest_api.core:application"
