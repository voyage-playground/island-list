#!/bin/sh
set -e

APP_ENV="${APP_ENV:-local}"

echo "🚀 Wait for DB to start"
/usr/local/bin/dockerize -wait "tcp://$DB_HOST:5432" -timeout 60s

echo "🚀 Migrate"
python3 -m flask migrate

echo "🚀 Seed"
python3 -m flask seed

echo "🚀 Run"
python3 -m flask run --host=0.0.0.0
