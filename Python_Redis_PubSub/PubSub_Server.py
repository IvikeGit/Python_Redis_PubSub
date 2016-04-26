import redis
import logging
import json
import settings
import time

class ChannelService:

    ##redis db
    _rdb = None
    
    def __init__(self):
        self._rdb = redis.StrictRedis(host = settings.SERVER_HOST, port = settings.SERVER_PORT, password = settings.SERVER_PASSWORD, db=0)

    def runChannel(self):
         try:
            counter = 0

            while True:
                time.sleep(0.5)
                counter +=1
                message = format('{0} published on "test" channel', counter)
                self._rdb.publish('test', message);
                if settings.DEBUG: print message

            self._rdb.publish('test', 'KILL');

         except Exception:
            logging.warning('Error!', exc_info=True)


if __name__ == '__main__':
    ChannelService().runChannel()
