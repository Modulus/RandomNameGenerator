# How
pip install -r requirements.txt

python main.py


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