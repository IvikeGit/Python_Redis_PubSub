import json
from os import environ

DEBUG = False

SERVER_HOST = '10.201.11.14'
SERVER_PORT = 6379
SERVER_PASSWORD = 'Valami123456'

if not DEBUG:
    sys_json = json.loads(environ.get('VCAP_SERVICES'))
    SERVER_HOST = sys_json['redis-1'][0]['credentials']['host']
    SERVER_PORT = sys_json['redis-1'][0]['credentials']['port']
    SERVER_PASSWORD = sys_json['redis-1'][0]['credentials']['password']  




