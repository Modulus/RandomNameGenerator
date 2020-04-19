# How
pipenv install


pipenv run gunicorn -b :5000 app:app


# Alternative
docker build -t demo .

docker run -d -p 5000:5000 --name demo demo

curl localhost:5000 
curl localhost:5000/json

# Docker images
docker pull coderpews/name-generator
docker run -d -p 5000:5000 --name generator coderpews/name-generator:1.0

curl localhost:5000 
curl localhost:5000/json