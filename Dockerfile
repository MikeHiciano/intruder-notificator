FROM ubuntu:16.04

ENV BROKER_ADDRESS "" 
ENV BROKER_PORT ""
ENV MQTT_TOPIC ""
ENV BOT_API_KEY ""
ENV TELEGRAM_CHAT_ID ""

RUN apt-get update
RUN apt-get -y install git python3 python3-pip
RUN git clone https://github.com/MikeHiciano/intruder-notificator.git
RUN pip3 install -r ./intruder-notificator/requirements.txt

CMD ["bin","bash"]