ARG PYTHON_VERSION=3.8-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY . /code

ARG DJANGO_SU_NAME 
ARG DJANGO_SUPERUSER_EMAIL 
ARG DJANGO_SUPERUSER_PASSWORD 


RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations && python manage.py migrate
RUN python manage.py createsuperuser --no-input --username=$DJANGO_SU_NAME --email=$DJANGO_SUPERUSER_EMAIL
EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "school.wsgi"]
