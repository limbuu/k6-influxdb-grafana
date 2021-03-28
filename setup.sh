#! /bin/bash

echo "--------Installing tools for loadtesting-----------"

## Install K6 (debian/ubuntu)
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 379CE192D401AB61
echo "deb https://dl.bintray.com/loadimpact/deb stable main" | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get install k6
echo "------------K6 sucessfully completed-------------"
## Install Infuxdb
echo "--------Installing Influxdb---------------------"
sudo apt install influxdb
echo "----------Influxdb successfully completed---------------"
## Install Grafana
echo "-----------Installing Grafana-----------------------"
sudo apt-get install -y apt-transport-https
sudo apt-get install -y software-properties-common wget
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install grafana
echo "--------Grafana Server successfully completed-----------"
## Start Grafana Server
echo "--------Starting Grafana Server---------"
sudo systemctl daemon-reload
sudo systemctl start grafana-server
echo "--------Grafana Server successfully started--------"

echo "----------Installation Completed------------"
