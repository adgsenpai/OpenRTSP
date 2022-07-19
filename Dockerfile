FROM ubuntu:20.04

LABEL Maintainer="adgsenpai"

EXPOSE 5000

RUN apt-get update

COPY . . 

RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" , "server.py" ]
