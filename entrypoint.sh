#!/bin/sh


if [ "$DATABASE" = "postgresql" ]
    then
    echo 'Check if database is running...'

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
        sleep 0.1
    done

    echo "The database is up and running :) "
fi


python manage.py collectstatic --no-input

python manage.py makemigrations
python manage.py migrate


exec "$@"