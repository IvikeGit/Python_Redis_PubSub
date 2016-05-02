import redis, logging, json, settings
import datetime, time
from pytz import timezone

class ChannelService:
    #redis db
    _rdb = None

    #datetime format
    _fmt = "%Y-%m-%d %H:%M:%S"
    #local time zone
    _tz = 'Europe/Budapest'
    
    def __init__(self):
        # setup the logging
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

        # initiate db
        logging.info('Running redis service on port :%s host: %s pw: %s', settings.SERVER_HOST, settings.SERVER_PORT, settings.SERVER_PASSWORD)
        self._rdb = redis.StrictRedis(host = settings.SERVER_HOST, port = settings.SERVER_PORT, password = settings.SERVER_PASSWORD, db=0)

    #converts UTC date time to the local one
    def getLocalTime(self):
        tz_utc = datetime.datetime.now(timezone('UTC'))
        tz_local = tz_utc.astimezone(timezone(self._tz))
        return tz_local.strftime(self._fmt)

    def runChannel(self):
         try:
            cnumber = 1

            #start publishing
            while True:
                time.sleep(1)
                #creating channel and message
                channel = 'TestChannel' + str(cnumber)
                message = 'Sample message raised at ' + self.getLocalTime()
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

