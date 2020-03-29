FROM ubuntu:16.04

COPY server/ /intruder-notificator/server/

ENV BROKER_ADDRESS "" 
ENV BROKER_PORT ""
ENV MQTT_TOPIC ""
ENV BOT_API_KEY ""
ENV TELEGRAM_CHAT_ID ""

RUN apt-get update
RUN apt-get -y install git python3 python3-pip
RUN pip3 install -r ./intruder-notificator/server/requirements.txt

CMD ["python3","./intruder-notificator/server/server.py"]