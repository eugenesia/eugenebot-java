# eugenebot-java
A Cleverbot-based Slack bot in Java

## Installation

On Ubuntu, install `firefox-geckodriver`
Install `cleverbotfree` in pip3

Add your Slackbot token in jbot-example's application.properties

## Usage
```bash
cd cleverbot
python3 server.py &

cd ../jbot
mvn clean install
cd jbot-example
mvn spring-boot:run &
```