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

## Server usage

Run it on a server

```bash
sudo crontab -e

# Paste the following or similar

# Eugenebot Java
@reboot cd /srv/eugenebot-java/cleverbot; python3 server.py >> /tmp/eugenebot-cleverbot.log 2>&1
@reboot cd /srv/eugenebot-java/jbot/jbot-example/target; java -jar jbot-example-4.1.2-rc.3-SNAPSHOT.jar >> /tmp/eugenebot-jbot.log 2>&1
@reboot cd /srv/eugenebot-java/jbot/jbot-example; mvn spring-boot:run >> /tmp/eugenebot-jbot.log 2>&1
```
