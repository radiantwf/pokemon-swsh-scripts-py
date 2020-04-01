#!/bin/ash
sudo mkdir -p /mosquitto/config
sudo mkdir -p /mosquitto/data
sudo mkdir -p /mosquitto/log

tee /etc/docker/daemon.json <<-'EOF'
persistence true
persistence_location /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log
EOF

sudo chmod  a+rwx /mosquitto -R
docker run -d -p 1883:1883 -p 9001:9001 -v /mosquitto/config:/mosquitto/config -v /mosquitto/data:/mosquitto/data -v /mosquitto/log:/mosquitto/log arm32v6/eclipse-mosquitto
