# Welcome to FastAPI

This project is a simple example how to write
fast RESTful APIs using Sanic and PonyORM.

## Dependencies

### Sanic

Sanic is one of the fastest microframeworks for Python.
It utilizes async/await syntax.

### PonyORM

Pony is the most pythonic ORM. It translates generators and lambdas
to optimized SQL. It still needs some features to be production-ready
(e.g. migrations) but it's very convenient and fast.

### Poetry

Poetry is the smartest Python package and virtualenv manager.

## Running

Make sure you have poetry installed:

    pip install poetry

Then clone this repo and run this in the directory:

    poetry install

It will install all the dependencies.

Launch database:

    docker-compose up

Launch application:

    poetry run python fast_api/main.py

The server should run on http://localhost:8888/

## Testing

You need to have the db running:

    docker-compose up

Then you can run tests:

    poetry run pytest



