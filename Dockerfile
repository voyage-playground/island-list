FROM jwilder/dockerize as dockerize

FROM voyageapp/node:17.6-alpine as node
WORKDIR /app
COPY package*.json ./
RUN npm ci

COPY . .

RUN npm run css

FROM python:3.8-alpine

ENV FLASK_ENV=development

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

COPY --from=dockerize /usr/local/bin/dockerize /usr/local/bin/dockerize
COPY --from=node /app ./

CMD [ "sh", "./scripts/run_app.sh"]
