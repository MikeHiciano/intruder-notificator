FROM ubuntu:16.04

COPY ../../intruder-notificator /

RUN apt-get update
RUN apt-get install python3 python3-pip
RUN pip install -r ../requirements.txt

CMD ['bin','bash']