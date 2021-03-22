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
## 2) Install InfluxDB
```
$ sudo apt install influxdb
```
### Verify Installation
Start the influxdb.service
```
$ sudo service influxdb start
```
Check the status, if it's enabled or not
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

Nov 01 17:16:53 manshi influxd[1024]: [meta] 2020/11/01 17:16:53 127.0.0.1 - - [01/Nov/2020:17:16:53 +0545] POST /execute HTTP/1.1 200 28 - Go-http-client/1.1 d764f22d-1c35-11eb-8005-000000000000 1.993164
Nov 01 17:16:53 manshi influxd[1024]: [meta] 2020/11/01 17:16:53 127.0.0.1 - - [01/Nov/2020:17:16:53 +0545] GET /?index=17 HTTP/1.1 200 193 - Go-http-client/1.1 d764ee48-1c35-11eb-8004-000000000000 2.2767
Nov 01 17:46:44 manshi influxd[1024]: [retention] 2020/11/01 17:46:44 retention policy shard deletion check commencing
Nov 01 18:16:44 manshi influxd[1024]: [retention] 2020/11/01 18:16:44 retention policy shard deletion check commencing
Nov 01 18:46:44 manshi influxd[1024]: [retention] 2020/11/01 18:46:44 retention policy shard deletion check commencing
Nov 01 19:16:44 manshi influxd[1024]: [retention] 2020/11/01 19:16:44 retention policy shard deletion check commencing
Nov 01 19:46:44 manshi influxd[1024]: [retention] 2020/11/01 19:46:44 retention policy shard deletion check commencing
Nov 01 21:04:50 manshi influxd[1024]: [retention] 2020/11/01 21:04:50 retention policy shard deletion check commencing
Nov 01 21:34:51 manshi influxd[1024]: [retention] 2020/11/01 21:34:51 retention policy shard deletion check commencing
Nov 01 22:04:51 manshi influxd[1024]: [retention] 2020/11/01 22:04:51 retention policy shard deletion check commencing
```
To stop the influxd, run command:
```
$ sudo service influxd stop
```

### Access InfluxDB
InfluxDB server runs on localhost, listening on port 8086.

It can be access at http://localhost:8086.

To access influxDB database, use http://localhost:8086/database-name

## 3) Install grafana
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

Nov 01 17:16:47 manshi grafana[1961]: Command lines overrides:
Nov 01 17:16:47 manshi grafana[1961]:   [0]: default.paths.data=/var/lib/grafana
Nov 01 17:16:47 manshi grafana[1961]:   [1]: default.paths.logs=/var/log/grafana
Nov 01 17:16:47 manshi grafana[1961]: Paths:
Nov 01 17:16:47 manshi grafana[1961]:   home: /usr/share/grafana
Nov 01 17:16:47 manshi grafana[1961]:   data: /var/lib/grafana
Nov 01 17:16:47 manshi grafana[1961]:   logs: /var/log/grafana
Nov 01 17:16:47 manshi grafana[1961]: 2020/11/01 17:16:47 [I] Database: sqlite3
Nov 01 17:16:47 manshi grafana[1961]: 2020/11/01 17:16:47 [I] Migrator: Starting DB migration
Nov 01 17:16:47 manshi grafana[1961]: 2020/11/01 17:16:47 [I] Listen: http://0.0.0.0:3000
```
To stop the grafana.service, run command:

```
$ sudo service grafana-server stop
```

### Run Loadtest script and upload the results to InfluxDB

```
$ k6 run --out influxdb=http://localhost:8086/myk6db script.js
```
myk6db is database name, if doesnot exist, k6 will create automatically

### Access the grafana on browser

Grafana server runs on localhost, listening to port 3000.

Grafana dashboard can be accessed on browser at http://localhost:3000
















