# start from an official image
FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /django_introduction/src
WORKDIR /django_introduction/src

# copy our project code
COPY . /django_introduction/src

RUN pip3 install -r requirements.txt

EXPOSE 8000

# define the default command to run when starting the container
CMD ["gunicorn", "--bind", "0:8000", "django_introduction.wsgi:application"]