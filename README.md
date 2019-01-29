# Django-introduction

Hello, this is my training Django-project represents web-service provides user 
an opportunity to buy train tickets. For now you can register, login, pick rides
for specific date and departure and arrival station. Then you can buy a ticket
for ride you want and check your tickets by "Cart" button clicking.

### Requirements

- Git
- Docker
- Docker-compose

### Run

```ch
$ git clone [https://github.com/BondarenkoDaniil/Django-introduction]
$ git checkout feature/docker_gunicorn_nginx
$ docker-compose build
$ docker-compose run --rm djangoapp /bin/bash -c "./manage.py migrate"
$ docker-compose run --rm djangoapp /bin/bash -c "./manage.py generate_test_data"
$ docker-compose run --rm djangoapp /bin/bash -c "./manage.py collectstatic"
$ docker-compose run --rm djangoapp /bin/bash -c "./manage.py createsuperuser"
$ docker-compose up
```

### Stop

Press ***Ctrl+C*** to stop containers running 


### Basic Workflow

1. open [localhost:8000]
2. go to **Register** page and fill the form
3. if success wait while you are redirected
4. **Login**
5. Fill main form with **Brest - Minsk - 01.15.2019** data
6. Buy a few **tickets** for yourself
7. Check your tickets by **Cart** button clicking

### Todos

- ***IMPROVE UI URGENTLY!!!***


