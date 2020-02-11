# 自动更新证书过期时间

## 配置文件

在 dtable-haiwen-extensions 项目根目录中创建 config 文件夹，在 config 文件夹中创建 `update_certificate_expiration.json` 文件，内容如下：

```
{
    "server_url": "https://dev.seafile.com/dtable-web/",
    "api_token": "ee0e91aa98efaf21c2a2f13295b379f50fbada7b",
    "table_name": "云端服务",
    "ignored_domains": ["archive.seafile.com","Windows-OfficeOnline"],
    "row_name_to_be_updated": "证书过期时间"
}
```

参数说明：

1. server_url: seatable server url。
1. api_token: *云服务器管理* 的具有可读写权限的 api token。
1. table_name: 表名。
1. ignored_domains: 不需检查证书过期时间的域名。
1. row_name_to_be_updated: 证书过期时间列名。

## 定时任务部署命令

每周一上午 09:30 执行定时任务。

```
crontab -e

30 9 * * 1 python3 /home/ubuntu/pro/dtable-haiwen-extensions/python/update_certificate_expiration/update_certificate_expiration.py 2>&1 >> /home/ubuntu/pro/dtable-haiwen-extensions/logs/update-certificate-expiration.log &
```
