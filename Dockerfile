FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install libmagic1 libsndfile1 ffmpeg -y

RUN pip install --upgrade pip

RUN apt-get update




COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt 

RUN pip install -r requirements.txt --ignore-installed nose-progressive

# Install PDF converter
RUN wget --no-check-certificate https://dl.xpdfreader.com/xpdf-tools-linux-4.05.tar.gz  && \
    tar -xvf xpdf-tools-linux-4.05.tar.gz && cp xpdf-tools-linux-4.05/bin64/pdftotext /usr/local/bin
    

# Adds our application code to the image
COPY . code
WORKDIR code

EXPOSE 8000
