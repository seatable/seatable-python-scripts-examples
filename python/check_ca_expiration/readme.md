# Auto check ca expiration

## Update configuration file

Update `check_ca_expiration.json` file in *config* folder：

```
{
    "server_url": "http{s}://your.seatable.server.url/",
    "api_token": "api token with read-write permission",
    "table_name": "table name",
    "ignored_domains": ["domainA", "domainB"],
    "row_name_to_be_updated": "row name of ca expiration"
}
```

## Create a cron job

Run script at 09:30 every Monday.

```
crontab -e

30 9 * * 1 python3 /path/to/seatable-scripts-examples/python/check_ca_expiration/check_ca_expiration.py >> /path/to/seatable-scripts-examples/logs/check_ca_expiration.log
```

