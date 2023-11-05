FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8080

CMD python manage.py makemigrations
CMD python manage.py makemigrations restserver

CMD python manage.py migrate
CMD python manage.py migrate restserver

CMD python manage.py runserver 0.0.0.0:8080
