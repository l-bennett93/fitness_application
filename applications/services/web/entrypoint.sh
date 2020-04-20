#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then 
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL starter"
fi

if ["$FLASK_ENV" == "development"]
then 
    echo "creating database tables..."
    python manage.py create_db
    echo "Tables created"
fi

exec "$@"
