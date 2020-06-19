# eugenebot
A conversational Slack bot made with Botkit in Node.js

## Installation

### Cbot connection

On Ubuntu, install `firefox-geckodriver` required to communicate with the
Cbot server
```bash
sudo apt install firefox-geckodriver
```

Install `cleverbotfree` in pip3
```bash
pip3 install cleverbotfree
```

### Botkit

Install Botkit dependencies
```bash
cd botkit
npm ci # Or npm install
```

Create _botkit/.env_ from the template file and fill in your Slack secrets.

## Usage

```bash
# Start the Cbot communication server
cd cleverbot
python3 server.py &

# 
cd ../botkit
npm start &
```

## Server usage

Run it on a server

```bash
sudo crontab -e

# Paste the following or similar

# Cbotfree breaks often - pull latest fixes
0 23 * * * pip3 install --upgrade cleverbotfree >> /tmp/cleverbotfree-upgrade.log 2>&1
# Cbot connection
@reboot cd /srv/eugenebot/cleverbot; python3 server.py >> /tmp/eugenebot-cleverbot.log 2>&1
# Wait for Cleverbot to start up and accept connections
@reboot sleep 30; cd /srv/eugenebot/botkit; npm start >> /tmp/eugenebot-botkit.log 2>&1
```

