FROM python:3

WORKDIR /code

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt --no-cache-dir

COPY . .
