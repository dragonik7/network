FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PUTHONDONTWRITEBYTECODE 1

WORKDIR /django

COPY ./requirements.txt /django/requirements.txt
RUN pip install --upgrade pip && pip install -r /django/requirements.txt


EXPOSE 8000