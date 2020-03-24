# Welcome to FastAPI

Not to be confused with [FastAPI framework](https://fastapi.tiangolo.com/)!

This is a toy-project to showcase how to use Sanic and PonyORM together.

## Dependencies

### Sanic

[Sanic](https://sanic.readthedocs.io/) is one of the fastest microframeworks for Python.
It utilizes async/await syntax.

### PonyORM

[Pony](https://ponyorm.org/) is the most pythonic ORM. It translates generators
and lambdas to optimized SQL. It still needs some features to be production-ready
(e.g. migrations) but it's very convenient and fast. Unfortunately it also
doesn't support async/await syntax yet.

### Poetry

[Poetry](https://python-poetry.org/) is the smartest Python manager for packages
and virtualenvs.

## Development

You'll need poetry:

    pip install poetry
    
Then clone this repository and enter created directory. Inside it run:

    poetry install
    
Poetry will create a virtualenv and install all dependencies.
Now you can activate the virtualenv:

    poetry shell
    
Please refer to [Poetry documentation](https://python-poetry.org/docs/)
for further reading.

## Running

Example project uses docker-compose.

    docker-compose up --build

The server should run on http://localhost:8000/

Automatic API documentation (swagger) is available at http://localhost:8000/docs

## Testing

You'll need the Development set up as described above. 
Start the database

    docker-compose up -d postgres

Then you can run tests:

    poetry run pytest

Remember to turn database off after testing:
    
    docker-compose down


