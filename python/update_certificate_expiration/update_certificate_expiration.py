import os
import ssl
import json
import OpenSSL
from datetime import datetime
from seatable_api import SeaTableAPI

def get_conf_dict():
    conf_file = os.path.join(os.path.dirname(__file__),
            '../../config/update_certificate_expiration.json')
    with open(conf_file) as f:
        return json.load(f)

def get_cert_expiration(domain):
    cert = ssl.get_server_certificate((domain, 443))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    expiration = datetime.strptime(x509.get_notAfter().decode("utf-8"),"%Y%m%d%H%M%SZ")
    return str(expiration)

if __name__ == '__main__':

    conf_dict = get_conf_dict()

    seatable = SeaTableAPI(conf_dict['api_token'], conf_dict['server_url'])
    seatable.auth()

    rows = seatable.list_rows(conf_dict['table_name'])
    for row in rows:

        domain = row['Name']
        if domain in conf_dict['ignored_domains']:
            continue

        expiration = get_cert_expiration(domain)
        row[conf_dict['row_name_to_be_updated']] = expiration
        seatable.update_row(conf_dict['table_name'], row['_id'], row)
        print("%s's cert expiration is %s" % (domain, expiration))
