import logging, os, pprint, urllib.parse

from django.conf import settings as project_settings
from mp_vl_app import settings_app
from pymongo import MongoClient


log = logging.getLogger(__name__)


def prep_connect_str( request ):
    """ Preps connect string for localdev and servers.
        Called by views.api_entries() """
    if project_settings.DEBUG == True and request.META.get('HTTP_HOST', '127.0.0.1')[0:9] == '127.0.0.1':
        connect_str = f'mongodb://{settings_app.DB_HOST}:{settings_app.DB_PORT}/'
    else:
        username = urllib.parse.quote_plus( settings_app.DB_USER )
        password = urllib.parse.quote_plus( settings_app.DB_PASS )
        connect_str_init = f'mongodb://{username}:{password}@{settings_app.DB_HOST}:{settings_app.DB_PORT}/'
        log.debug( f'connect_str_init, ```{connect_str_init}```' )
        connect_str = f'{connect_str_init}?authSource={settings_app.DB_NAME}'
    log.debug( f'prepared connect_str, ```{connect_str}```' )
    return connect_str


# ----------------------------------
# working dev-server demo-code below
# ----------------------------------

# import os, urllib.parse
# import pymongo

# M_HOST = os.environ['MV_DJ__MONGO_HOST']
# M_PORT = os.environ['MV_DJ__MONGO_PORT']
# M_DB = os.environ['MV_DJ__MONGO_DATABASE_NAME']
# M_COLL = os.environ['MV_DJ__MONGO_ENTRIES_COLLECTION_NAME']
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
# M_COLL = os.environ['MV_DJ__MONGO_ENTRIES_COLLECTION_NAME']

# connect_str = f'mongodb://{M_HOST}:{M_PORT}/'

# m_client = pymongo.MongoClient( connect_str )
# m_db = m_client[M_DB]
# m_collection = m_db[M_COLL]

# x = m_collection.find_one()

# print( x )
