FROM python:3.7-slim

COPY . .

RUN  pip3 install pipenv && pipenv install gunicorn



EXPOSE 5000
ENTRYPOINT ["pipenv", "run", "gunicorn","-b :5000", "--access-logfile", "-", "--error-logfile",  "-", "app:app"]
# ENTRYPOINT ["/usr/local/bin/gunicorn","-b :5000", "--access-logfile", "-", "--error-logfile",  "-", "app:app"]