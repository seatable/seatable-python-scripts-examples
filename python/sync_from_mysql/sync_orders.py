import os
import sys
from datetime import datetime

import pymysql
from seatable_api import SeaTableAPI

# load config config/sync_orders_settings.py
conf_dir = os.path.join(os.path.dirname(__file__), '../../config')
sys.path.append(conf_dir)
from sync_orders_settings import api_token, server_url, \
    host, user, password, db


def sync_orders(seatable, mysql_connection):
    # seatable data
    table_name = 'Order'
    rows = seatable.list_rows(table_name)
    row_unique_keys = [row['ID'] for row in rows]

    # mysql data
    with mysql_connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM order LEFT JOIN user ON order.user_id=user.id"
        cursor.execute(sql)
        mysql_data = cursor.fetchall()

    print('[%s] Mysql table order total [%d], SeaTable Order total [%d]'
          % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), len(mysql_data), len(rows)))

    # sync
    count = 0
    for item in mysql_data:
        if item['id'] not in row_unique_keys:

            row_data = {
                'ID': item['id'],
                'User': item['username'],
                'Price': item['price'],
                'Created At': item['created_at'].strftime('%Y-%m-%d %H:%M'),
            }
            seatable.append_row(table_name, row_data)
            count += 1

    print('[%s] SeaTable Order appended [%d]'
          % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), count))


if __name__ == '__main__':

    seatable = SeaTableAPI(api_token, server_url)
    seatable.auth()

    mysql_connection = pymysql.connect(host=host, user=user, password=password, db=db)

    sync_orders(seatable, mysql_connection)
