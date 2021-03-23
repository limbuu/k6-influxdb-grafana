# k6-influxdb-grafana
We will use k6 as loadtesting tool, influxdb as time series database and grafana for visualization
# A. Local Setup 
## 1) Install K6 (Debian/Ubuntu)
```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 379CE192D401AB61
$ echo "deb https://dl.bintray.com/loadimpact/deb stable main" | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install k6
```

### Verify Installation
```
$ k6 version

k6 v0.28.0 (2020-09-24T14:33:59+0000/v0.28.0-0-gdee9c4ce, go1.14.9, linux/amd64)

```
## 2) Run Loadtest script 

Now to run a simple loadtest script, run the following command:
```
$ k6 run simple-script.js
```
To run with specfic `virtual users` for certain `duration`, run the following command:
```
$ k6 --vus 10 --duration 30s simple-script.js
```

## 3) Install InfluxDB(For Metrics Storage)
```
$ sudo apt install influxdb
```
### Verify Installation
Start the influxdb.service if not started by default:
```
$ sudo service influxdb start
```
Check the status, if it's enabled or not:
```
$ sudo service influxd status
● influxdb.service - InfluxDB is an open-source, distributed, time series database
   Loaded: loaded (/lib/systemd/system/influxdb.service; enabled; vendor preset: enabled)
   Active: active (running) since Sun 2020-11-01 17:16:41 +0545; 5h 6min ago
     Docs: man:influxd(1)
 Main PID: 1024 (influxd)
    Tasks: 19
   Memory: 28.1M
      CPU: 27.821s
   CGroup: /system.slice/influxdb.service
           └─1024 /usr/bin/influxd -config /etc/influxdb/influxdb.conf
```
To stop the influxd, run command:
```
$ sudo service influxd stop
```

### Access InfluxDB
InfluxDB server runs on localhost, listening on port `8086`.It can be access at `http://localhost:8086`.

To access influxDB database, use `http://localhost:8086/database-name`.


## 3) Install grafana(For Visualization)
```
# To install OSS release
$ sudo apt-get install -y apt-transport-https
$ sudo apt-get install -y software-properties-common wget
$ wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -

# Add this repository for stable releases
$ echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
$ sudo apt-get update
$ sudo apt-get install grafana

```

### Verify Installation
Start the grafana.service 
```
$ sudo service grafana-server start
```
Check the status, if its enabled or not
```
$ sudo service grafana-server status

● grafana.service - Starts and stops a single grafana instance on this system
   Loaded: loaded (/lib/systemd/system/grafana.service; enabled; vendor preset: enabled)
   Active: active (running) since Sun 2020-11-01 17:16:47 +0545; 4h 57min ago
     Docs: http://docs.grafana.org
 Main PID: 1961 (grafana)
    Tasks: 18
   Memory: 6.3M
      CPU: 1.514s
   CGroup: /system.slice/grafana.service
           └─1961 /usr/sbin/grafana --config=/etc/grafana/grafana.ini cfg:default.paths.logs=/var/log/grafana cfg:default.paths.data=/var/lib/grafana
```
To stop the grafana.service, run command:

```
$ sudo service grafana-server stop
```

### Access the grafana on browser

Grafana server runs on localhost, listening to port `3000`.
Grafana dashboard can be accessed on browser at `http://localhost:3000`.

Use `admin` or anything you like for userame and password.
![alt text](https://github.com/limbuu/k6-influxdb-grafana/blob/main/images/grafana-login.png)

#### - Add Grafana Dashboard
After successfully signing in grafana dashboard, import Grafana dashboard. 
We will import dashboard with id:`2587` for testing.
![alt text](https://github.com/limbuu/k6-influxdb-grafana/blob/main/images/grafana-setup1.png)

#### - Add InfluxDB as DataSource
Now, configure grafana dashboard to use `InfluxDB` as datasource.
![alt text](https://github.com/limbuu/k6-influxdb-grafana/blob/main/images/grafana-setup2.png)

And, add `http://localhost:8086` as influxdb url and `myk6db` as database name.  
![alt text](https://github.com/limbuu/k6-influxdb-grafana/blob/main/images/influxdb-setup.png)

## 4) Run Loadtest script with Visualization

We will run relatively advaced loadtest script with virtual users, rps and duration. 

```
$ k6 run --out influxdb=http://localhost:8086/myk6db advanced-script.js
```
myk6db is database name, if doesnot exist, k6 will create automatically

 
The output on grafana-dashboard looks like this:
![alt text](https://github.com/limbuu/k6-influxdb-grafana/blob/main/images/grafna-dashboard-output.png)

















