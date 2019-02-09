FROM ubuntu:16.04
MAINTAINER <Mike D'Itri >

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install Numpy
RUN pip3 install pandas 


