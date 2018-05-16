FROM ubuntu:17.10

# -- Install Pipenv:
RUN apt-get update \
  && apt-get install software-properties-common python-software-properties -y \
  && add-apt-repository ppa:pypa/ppa -y \
  && apt-get update \
  && apt-get install -y \
    git \
    libmysqlclient-dev \
    pipenv

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# -- Install Application into container:
RUN set -ex && mkdir /app

WORKDIR /app

COPY . /app

# -- Install dependencies:
RUN set -ex && pipenv install --deploy --system



CMD python3 scanAllCors.py