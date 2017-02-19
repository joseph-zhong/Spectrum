FROM ubuntu:latest
ENV PYTHON_VERSION 2.7.13
RUN apt-get update -y
RUN apt-get install python2.7 -y
RUN apt-get install -y python-pip python-dev build-essential
COPY ./learn /app
WORKDIR /app
RUN apt-get install libxml2-dev libxslt-dev -y
RUN apt-get install libjpeg-dev zlib1g-dev libpng12-dev -y
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install newspaper
RUN pip install numpy sklearn
RUN pip install scipy networkx
RUN pip install --upgrade watson-developer-cloud
RUN pip install summa
RUN pip install flask
RUN python forest.py
