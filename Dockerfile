FROM jwilder/dockerize as dockerize

FROM python:3.8-alpine

ENV FLASK_ENV=development

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

COPY --from=dockerize /usr/local/bin/dockerize /usr/local/bin/dockerize

CMD [ "sh", "./scripts/run_app.sh"]
