# Technical task project

Technical task project for Talkimakan C.I.G.   
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)


## Installation
- You need docker to run this project [docker install](https://docs.docker.com/engine/install/)
- docker-compose also needed  [docker-compose install](https://docs.docker.com/compose/install/)

Download to your project directory:

```shell script
git clone https://github.com/adil2604/django-task
```

## Usage

To run project locally in project root: 
```shell script
docker-compose up
```
To run in production in project root:
```shell script
docker-compose -f docker-compose.prod.yml up
```
Apply project migrations:
```shell script
docker-compose exec web python manage.py migrate
```
Collect project static files:
```shell script
docker-compose exec web python manage.py collectstatic --noinput
``` 
Stop project:
```shell script
docker-compose down
```

