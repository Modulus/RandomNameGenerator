FROM node:8.15-jessie as builder

COPY . .

RUN  mkdir -p /usr/local/lib/node_modules/create-elm-app/node_modules/elmi-to-json/unpacked_bin && npm install -g elm -unsafe-perm=true

RUN elm make src/Main.elm --output js/main.js


FROM nginx:1.15-alpine

RUN mkdir /usr/share/nginx/html/js

COPY public/ /usr/share/nginx/html

COPY --from=builder js/main.js /usr/share/nginx/html/js

COPY --from=builder node_modules/bootstrap/dist /usr/share/nginx/html/node_modules/bootstrap/dist

EXPOSE 80 443