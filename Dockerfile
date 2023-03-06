# backend/web-back/Dockerfile
# set base image
FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /code

# install dependencies
COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

# Copy project
COPY . ./

# Expose application port
EXPOSE 8000

# docker-compose run --rm web-back sh -c "python manage.py makemigrations"
# docker-compose run --rm web-back sh -c "python manage.py migrate"
