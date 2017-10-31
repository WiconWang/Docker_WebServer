FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

EXPOSE 8060

COPY ./requirements.txt ./

RUN pip install -r requirements.txt --no-cache-dir --disable-pip-version-check

COPY . /app
