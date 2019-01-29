#!/usr/bin/env bash

echo "Migrating.."
docker-compose run --rm djangoapp /bin/bash -c "./manage.py migrate"
docker-compose run --rm djangoapp /bin/bash -c "./manage.py generate_test_data"
echo "Collecting static files.."
docker-compose run --rm djangoapp /bin/bash -c "./manage.py collectstatic"
