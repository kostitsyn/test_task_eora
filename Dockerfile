FROM python:3.10.0

RUN apt-get update

RUN pip3 install --upgrade pip

COPY ./ ./

RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations &&\
    python3 manage.py migrate &&\
    python3 manage.py create_superuser
CMD python3 manage.py runserver 0.0.0.0:9000
