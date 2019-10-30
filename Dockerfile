FROM python:3.7-alpine

RUN apk add --no-cache --virtual build-dependencies build-base python3-dev
RUN apk add --no-cache libstdc++
RUN pip3 install pipenv

WORKDIR /app
COPY Pipfile.lock .
COPY Pipfile .

# RUN pipenv install --system --deploy
RUN apk del build-dependencies

COPY . .

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8080

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --reload main:app