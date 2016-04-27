import os
#testdata = {
# "VCAP_SERVICES": {
#  "redis-1": [
#   {
#    "credentials": {
#     "host": "10.72.6.22",
#     "password": "4d4a1000-f1c5-446c-b730-45a44edd3e6d",
#     "port": 46415
#    },
#    "label": "redis-1",
#    "name": "redis_test",
#    "plan": "shared-vm",
#    "provider": 'null',
#    "syslog_drain_url": 'null',
#    "tags": [
#     "pivotal",
#     "redis"
#    ]
#   }
#  ]
# }
#}

#{
# "VCAP_APPLICATION": {
#  "application_id": "1d621f3b-bd79-4cf1-a7be-96783d207733",
#  "application_name": "TESTREDIS",
#  "application_uris": [
#   "testredis.run.aws-usw02-pr.ice.predix.io"
#  ],
#  "application_version": "8d154578-4ac5-4346-81c6-1f17275e5aa5",
#  "limits": {
#   "disk": 1024,
#   "fds": 16384,
#   "mem": 128
#  },
#  "name": "TESTREDIS",
#  "space_id": "d2a67522-a6f9-4d6e-8c8e-56a9ee23ef96",
#  "space_name": "ivi",
#  "uris": [
#   "testredis.run.aws-usw02-pr.ice.predix.io"
#  ],
#  "users": 'null',
#  "version": "8d154578-4ac5-4346-81c6-1f17275e5aa5"
# }
#}

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




