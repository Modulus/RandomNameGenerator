FROM node:12-alpine as builder

COPY . .



#RUN API_URL="http://snadder.io/api" 
RUN npm run build

RUN ls -la dist
# --output js/main.js



FROM nginx:1.17-alpine

RUN mkdir /usr/share/nginx/html/js

COPY --from=builder dist /usr/share/nginx/html

RUN ls /usr/share/nginx/html



EXPOSE 80 443
