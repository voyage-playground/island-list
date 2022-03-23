FROM voyageapp/node:17.6-alpine as node
WORKDIR /app
COPY package*.json ./
RUN npm ci

COPY . .

RUN npm run css

FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

COPY --from=node /usr/local/bin/dockerize /usr/local/bin/dockerize
COPY --from=node /app/lib/static/dist ./lib/static/dist

ENV FLASK_ENV=development

CMD dockerize -wait "tcp://$DB_HOST:5432" -timeout 60s ; python3 app.py
