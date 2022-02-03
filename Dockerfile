FROM python:3.10.0

RUN apt-get update

RUN pip3 install --upgrade pip

COPY ./ ./

RUN pip3 install -r requirements.txt