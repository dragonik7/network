FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PUTHONDONTWRITEBYTECODE 1

RUN mkdir /django
WORKDIR /django
COPY ../app /django/
RUN pip install --upgrade pip && pip install -r /django/requirements.txt