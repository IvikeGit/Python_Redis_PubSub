import redis
import threading

class Listener(threading.Thread):

    #redis db
    _rdb = None
    #pubsub object
    _pubsub = None
    
    def __init__(self):
        # setup the logging    
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

        # initiate db
        self._rdb = redis.StrictRedis(host = settings.SERVER_HOST, port = settings.SERVER_PORT, password = settings.SERVER_PASSWORD, db=0)

        #start new thread on one's copy 
        threading.Thread.__init__(self)

        #creating pubsub object
        self._pubsub = _rdb.pubsub()


if __name__ == '__main__':