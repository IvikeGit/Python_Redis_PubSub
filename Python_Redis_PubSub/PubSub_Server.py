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

    def runChannel(self, startVal, endVal):
         try:

            for num in range(startVal, endVal):
                time.sleep(0.5)
                self._rdb.publish('test', num);
                if settings.DEBUG: print '"test" channel raised {0}'.format(num)

            self._rdb.publish('test', 'KILL');

         except Exception:
            logging.warning('Error!', exc_info=True)


if __name__ == '__main__':
    ChannelService().runChannel(1, 100)
