FROM python:3.10-slim

RUN apt-get update \
&& apt-get install gcc python3-opencv python3-numpy -y \
&& apt-get clean

COPY requirements.txt /app/requirements.txt

WORKDIR app
# RUN pip install --user -r requirements.txt
RUN set -ex && \
    pip install -f ./.pkg_cache -r requirements.txt && \
    rm -rf ./.pkg_cache
COPY . /app


CMD ["uwsgi", "wsgi.ini"]