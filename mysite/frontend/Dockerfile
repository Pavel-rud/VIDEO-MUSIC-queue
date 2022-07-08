FROM node:lts-alpine as build-stage

RUN npm install --location=global http-server

WORKDIR /app

COPY package*.json ./

RUN npm install \
    npm install router

COPY . .

RUN npm run build

FROM nginx as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html