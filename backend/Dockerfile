# Using lightweight alpine image
FROM python:3.10-alpine

WORKDIR /usr/src/app

# Installing packages
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY courses ./courses

# Install API dependencies
RUN pipenv install --skip-lock --system

# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]