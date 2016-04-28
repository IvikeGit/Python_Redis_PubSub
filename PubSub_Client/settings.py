import os
import logging

DEBUG = True

SERVER_HOST = '10.201.11.14'
SERVER_PORT = 6379
SERVER_PASSWORD = 'Valami123456'

if not DEBUG:
    SERVER_HOST = '10.72.6.22'
    SERVER_PORT = 46415
    SERVER_PASSWORD = '4d4a1000-f1c5-446c-b730-45a44edd3e6d'
    #sys_json = os.getenv('VCAP_SERVICES')
    #SERVER_HOST = sys_json['redis-1'][0]['credentials']['host']
    #SERVER_PORT = sys_json['redis-1'][0]['credentials']['port']
    #SERVER_PASSWORD = sys_json['redis-1'][0]['credentials']['password']




