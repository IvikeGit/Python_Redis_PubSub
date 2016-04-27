import redis
import threading
import logging
import settings

class Listener(threading.Thread):

    #redis db
    _rdb = None
    #pubsub object
    _pubsub = None
    
    def __init__(self, channels):
        # setup the logging    
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

        # initiate db
        self._rdb = redis.StrictRedis(host = settings.SERVER_HOST, port = settings.SERVER_PORT, password = settings.SERVER_PASSWORD, db=0)

        #start new thread on one's copy 
        threading.Thread.__init__(self)

        #creating pubsub object and subscribe on the channels
        self._pubsub = self._rdb.pubsub()
        self._pubsub.subscribe(channels)

    def work(self, item):
        print item['channel'], ":", item['data']

    def run(self):
        for item in self._pubsub.listen():
            if item['data'] == "KILL":
                self.pubsub.unsubscribe()
                logging.info('Listener unsubscribed from {0}'.format(item['data']))
                break
            else:
                self.work(item)


if __name__ == '__main__':
    client = Listener(['TestChannel1','TestChannel2','TestChannel3' ])
    client.start()