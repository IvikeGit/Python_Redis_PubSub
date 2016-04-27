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
            seconds = 6000
            cnumber = 1
            logging.info('Running redis service on port :%s host: %s', settings.SERVER_HOST, settings.SERVER_PORT)

            #start publishing
            while seconds > 0 :
                time.sleep(1)
                #creating channel and message
                channel = 'TestChannel' + str(cnumber)
                message = 'Message on [{0}]'.format(channel)
                #publishing
                self._rdb.publish(channel, message)

                logging.info(message)
                seconds -= 1
                cnumber = 1 if cnumber == 3 else cnumber + 1

            #kill channels
            self._rdb.publish('test1', 'KILL')
            self._rdb.publish('test2', 'KILL')
            self._rdb.publish('test3', 'KILL')

         except Exception:
            logging.warning('Error!', exc_info=True)


if __name__ == '__main__':
    ChannelService().runChannel()
