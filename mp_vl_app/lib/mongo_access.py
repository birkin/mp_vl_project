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

# connect_str_2 = f'{connect_str}?authSource={DB_NAME}&authMechanism=SCRAM-SHA-256'
# log.debug( f'connect_str, ```{connect_str}```' )

client = MongoClient( connect_str )
print( f'client, ```{client}```' )

print( f'client, ```{pprint.pformat(client.__dict__)}```' )


# ----------------------------------
# working dev-server demo-code below
# ----------------------------------

# import os, urllib.parse
# import pymongo

# M_HOST = os.environ['MV_DJ__MONGO_HOST']
# M_PORT = os.environ['MV_DJ__MONGO_PORT']
# M_DB = os.environ['MV_DJ__MONGO_DATABASE_NAME']
# M_COLL = os.environ['MV_DJ__MONGO_COLLECTION_NAME']
# M_USER =  os.environ['MV_DJ__MONGO_USERNAME']
# M_PASS =  os.environ['MV_DJ__MONGO_PASSWORD']

# username = urllib.parse.quote_plus( M_USER )
# password = urllib.parse.quote_plus( M_PASS )

# connect_str_1 = f'mongodb://{username}:{password}@{M_HOST}:{M_PORT}/'
# print( f'connect_str_1, ```{connect_str_1}```' )

# connect_str_2 = f'{connect_str_1}?authSource={M_DB}'
# print( f'connect_str_2, ```{connect_str_2}```' )

# m_client = pymongo.MongoClient( connect_str_2 )
# m_db = m_client[M_DB]
# m_collection = m_db[M_COLL]

# x = m_collection.find_one()

# print( x )


# --------------------------------
# working localdev demo-code below
# --------------------------------

# import os
# import pymongo

# M_HOST = os.environ['MV_DJ__MONGO_HOST']
# M_PORT = os.environ['MV_DJ__MONGO_PORT']
# M_DB = os.environ['MV_DJ__MONGO_DATABASE_NAME']
# M_COLL = os.environ['MV_DJ__MONGO_COLLECTION_NAME']

# connect_str = f'mongodb://{M_HOST}:{M_PORT}/'

# m_client = pymongo.MongoClient( connect_str )
# m_db = m_client[M_DB]
# m_collection = m_db[M_COLL]

# x = m_collection.find_one()

# print( x )
