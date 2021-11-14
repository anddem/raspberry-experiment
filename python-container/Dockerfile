FROM python:3.10-alpine3.14

WORKDIR /usr/src/app

# RUN addgroup --system app && adduser --system app

# USER app

RUN apk add --no-cache python3-dev build-base linux-headers pcre-dev

COPY requirements.txt ./
RUN set -ex && \
    pip install -f ./.pkg_cache -r requirements.txt && \
    rm -rf ./.pkg_cache

COPY app.py .
COPY wsgi.ini .

CMD ["uwsgi", "wsgi.ini"]