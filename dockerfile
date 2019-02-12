FROM ubuntu:16.04
MAINTAINER <Mike D'Itri >

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install Numpy
RUN pip3 install pandas 
ADD new_list_for_columns.py /
ADD housing.data.txt /
CMD ["python3", "./new_list_for_columns.py"]

