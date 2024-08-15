FROM python:3.8 as base_document

RUN apt-get update
RUN apt-get install libmagic1 libsndfile1 ffmpeg -y

RUN pip install --upgrade pip

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt 
FROM base_document as document
# Adds our application code to the image
RUN ls -l 
COPY . code
# RUN cd /document/docs
WORKDIR code 
# RUN ls -l 
RUN ls -l /code 
RUN pwd
# RUN mkdocs build
# RUN ls -l /document && ls -l / 
EXPOSE 8001
# ENTRYPOINT  [ "mkdocs", "build", "--dev-addr=0.0.0.0:8001" ]
# ENTRYPOINT ["mkdocs", "serve"]
