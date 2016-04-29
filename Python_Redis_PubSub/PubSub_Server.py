import redis
import logging
import json
import settings
from datetime import datetime
import time

class ChannelService:

    ##redis db
    _rdb = None
    
    def __init__(self):
        # setup the logging
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

        # initiate db
        logging.info('Running redis service on port :%s host: %s pw: %s', settings.SERVER_HOST, settings.SERVER_PORT, settings.SERVER_PASSWORD)
        self._rdb = redis.StrictRedis(host = settings.SERVER_HOST, port = settings.SERVER_PORT, password = settings.SERVER_PASSWORD, db=0)

        
    def runChannel(self):
         try:
            cnumber = 1

            #start publishing
            while True:
                time.sleep(1)
                #creating channel and message
                channel = 'TestChannel' + str(cnumber)
                message = 'Sample message raised at ' + str(time.strftime('%H:%M:%S'))
                #publishing
                self._rdb.publish(channel, message)

                logging.info(message)
                cnumber = 1 if cnumber == 3 else cnumber + 1

            #kill channels
            self._rdb.publish('test1', 'KILL')
            self._rdb.publish('test2', 'KILL')
            self._rdb.publish('test3', 'KILL')

         except Exception:
            logging.warning('Error!', exc_info=True)


if __name__ == '__main__':
    ChannelService().runChannel()

