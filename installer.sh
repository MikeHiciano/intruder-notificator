#!/bin/bash

locate_req(){
    local file="requirements.txt"
    if [ -e $file ]
    then
        pip3 install -r requirements.txt || echo -e
    
    else
        echo "File $file Not Found"
    fi
    return
}

is_installed(){
    if [ -z "$IS_INSTALLED" ]
    then
        echo "this program was installed!"
    
    else
        locate_req
        IS_INSTALLED="True"
    fi

    return
}

environment_variables(){

    local GREEN="\033[0;32m"
    local NC="\033[0m"    
    if [ -z "${BROKER_ADDRESS}"]
    then
        echo -e "BROKER ADDRESS: ${GREEN}ok${NC}"
    else
        read -p "Insert your mqtt broker address: " broker_address
    fi
    if [ -z "${BROKER_PORT}" ]
    then
        echo -e "BROKER PORT: ${GREEN}ok${NC}"
    else
        read -p "insert your mqtt broker port: " broker_port
    fi
        if [ -z "${MQTT_TOPIC}" ]
    then
        echo -e "BROKER TOPIC: ${GREEN}ok${NC}"
    else
        read -p "insert your mqtt topic: " mqtt_topic
    fi
        if [ -z "${BOT_API_KEY}" ]
    then
        echo -e "TELEGRAM BOT API KEY: ${GREEN}ok${NC}"
    else
        read -p "insert your Telegram bot api key: " bot_api_key
    fi
    if [ -z "${TELEGRAM_CHAT_ID}" ]
    then
        echo -e "TELEGRAM CHAT ID: ${GREEN}ok${NC}"
    else
        read -p "insert your telegram chat id: " telegram_chat_id
    fi

    BROKER_ADDRESS= $broker_address
    BROKER_PORT= $broker_port
    MQTT_TOPIC= $mqtt_topic
    BOT_API_KEY= $bot_api_key
    TELEGRAM_CHAT_ID= $telegram_chat_id
    
    return
}

is_installed

if [ -z $IS_INSTALLED ]
then
    environment_variables
else
    locate_req
    echo " "
    environment_variables
fi
