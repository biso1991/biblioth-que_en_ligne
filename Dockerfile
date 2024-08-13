FROM python:3.8 as base_web 
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install libmagic1 libsndfile1 ffmpeg -y

RUN pip install --upgrade pip

RUN apt-get update

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt --ignore-installed nose-progressive

    
FROM base_web as web 
# Adds our application code to the image
COPY . code
WORKDIR code

EXPOSE 8000
