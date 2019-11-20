import logging, os, pprint, urllib.parse
from pymongo import MongoClient


log = logging.getLogger(__name__)


HOST = os.environ['MV_DJ__MONGO_HOST']
PORT =  os.environ['MV_DJ__MONGO_PORT']
DB_NAME = os.environ['MV_DJ__MONGO_DATABASE_NAME']
COLL_NAME = os.environ['MV_DJ__MONGO_COLLECTION_NAME']
USER =  os.environ['MV_DJ__MONGO_USERNAME']
PASS =  os.environ['MV_DJ__MONGO_PASSWORD']


username = urllib.parse.quote_plus( USER )
password = urllib.parse.quote_plus( PASS )

connect_str = f'mongodb://{username}:{password}@{HOST}:{PORT}/'
log.debug( f'connect_str, ```{connect_str}```' )

connect_str_2 = f'{connect_str}?authSource={DB_NAME}&authMechanism=SCRAM-SHA-256'
log.debug( f'connect_str, ```{connect_str}```' )

client = MongoClient( connect_str )
log.debug( f'client, ```{client}```' )
