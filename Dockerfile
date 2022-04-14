FROM ubuntu:latest

RUN apt-get update

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN pip install numpy

WORKDIR /random

COPY . .

CMD ["python3", "main.py"]
