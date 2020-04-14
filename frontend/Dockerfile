FROM node:12-alpine as builder

COPY . .


RUN  apk add git && mkdir -p /usr/local/lib/node_modules/create-elm-app/node_modules/elmi-to-json/unpacked_bin && npm install -g create-elm-app -unsafe-perm=true && npm install

RUN API_URL="http://snadder.io/api" elm-app build
RUN ls -la build/static
# --output js/main.js



FROM nginx:1.17-alpine

RUN mkdir /usr/share/nginx/html/js

COPY --from=builder build /usr/share/nginx/html

RUN ls -la /usr/share/nginx/html/static


EXPOSE 80 443