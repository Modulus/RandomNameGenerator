FROM python:3.7-slim

COPY . .

RUN  pip3 install pip --upgrade && pip3 install -r requirements.txt && pip3 install gunicorn

EXPOSE 5000
ENTRYPOINT ["/usr/local/bin/gunicorn","-b :5000", "--access-logfile", "-", "--error-logfile",  "-", "app:app"]