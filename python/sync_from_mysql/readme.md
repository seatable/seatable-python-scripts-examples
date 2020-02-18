# Auto sync orders from mysql

## Update configuration file

Update `sync_orders_settings.py` file in *config* folder：

``` python
server_url = 'http{s}://your.seatable.server.url/',
api_token = 'api token with read-write permission',

host = 'mysql host'
user = 'mysql user'
password = 'mysql password'
db = 'mysql db'
```

## Create a cron job

Run script at 01:00 every day.

``` 
crontab -e

0 1 * * * python3 /path/to/seatable-scripts-examples/python/sync_from_mysql/sync_orders.py &>> /path/to/seatable-scripts-examples/logs/sync_orders.log
```

