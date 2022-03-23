#!/bin/sh
set -e

APP_ENV="${APP_ENV:-local}"

echo "🚀 Wait for DB to start"
dockerize -wait "tcp://$DB_HOST:5432" -timeout 60s

echo "🚀 Migrate"
python3 -m flask commands migrate

echo "🚀 Seed"
python3 -m flask commands seed

echo "🚀 Run"
python3 -m flask run --host=0.0.0.0
