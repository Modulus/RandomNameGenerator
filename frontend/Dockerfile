FROM node:8.15-alpine as builder

COPY . .


RUN  mkdir -p /usr/local/lib/node_modules/create-elm-app/node_modules/elmi-to-json/unpacked_bin && npm install -g create-elm-app -unsafe-perm=true && npm install

RUN elm-app build
RUN ls -la build/static
# --output js/main.js



FROM nginx:1.15-alpine

RUN mkdir /usr/share/nginx/html/js

COPY public/ /usr/share/nginx/html

COPY --from=builder build /usr/share/nginx/html

COPY --from=builder node_modules/bootstrap/dist /usr/share/nginx/html/node_modules/bootstrap/dist


RUN ls -la /usr/share/nginx/html/static


EXPOSE 80 443