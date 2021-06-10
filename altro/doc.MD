# INSTALL DOCKER

<li>requirements</li>
<li>requirements</li>
1. Write the docker file
2. Building the docker image
3. Running the movie review app

a. How to build a docker image?
docker build -t davidepiu_api .

b. Run the docker
docker run -p   8088(local):8088(container) davidepiu_api

# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

