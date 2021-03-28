#! /bin/bash
echo "----------Checking the Status of k6-------"
k6
echo "----------Checking the status of influxdb----------"
sudo systemctl status influxdb
echo "----------Checking the status of grafana---------"
sudo systemctl status grafana-server
sudo systemctl daemon-reload
sudo systemctl start grafana-server
echo "----------Grafana Server started again!!!"