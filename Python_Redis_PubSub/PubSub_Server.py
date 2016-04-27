import redis
import logging
import json
import settings
import time

class ChannelService:

    ##redis db
    _rdb = None
    
    def __init__(self):
        # setup the logging    
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        # initaite db
        self._rdb = redis.StrictRedis(host = settings.SERVER_HOST, port = settings.SERVER_PORT, password = settings.SERVER_PASSWORD, db=0)

    def runChannel(self):
         try:
            counter = 0
            logging.debug('Running redis service on port :%s host: %s', settings.SERVER_HOST, settings.SERVER_PORT)

            while counter <= 60:
                time.sleep(1)
                counter +=1
                message = '{0} published on "test" channel'.format(counter)
                self._rdb.publish('test', message);
                logging.debug(message)

            self._rdb.publish('test', 'KILL');

         except Exception:
            logging.warning('Error!', exc_info=True)


if __name__ == '__main__':
    ChannelService().runChannel()
