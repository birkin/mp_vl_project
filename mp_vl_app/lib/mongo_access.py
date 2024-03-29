import logging, os, pprint, urllib.parse

import bson, pymongo  # I think bson is installed when pymongo is installed; it does not show up in `pip freeze`.
from django.conf import settings as project_settings
from mp_vl_app import settings_app


log = logging.getLogger(__name__)


def prep_connect_str( request ) -> str:
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


def query_entries( connect_str: str ) -> pymongo.cursor.Cursor:  # or None
    """ Returns entries for full listing page.
        NB: Because `entries_query` is a pymongo-cursor, applying a slice would act as a filter to the variable itself, not to a copy, as may be expected.
        Called by views.api_entries(), which is accessed by views.db_list() """
    log.debug( 'starting query_entries()' )
    entries_query = None
    try:
        m_client: pymongo.mongo_client.MongoClient = pymongo.MongoClient( connect_str )
        m_db: pymongo.database.Database = m_client[settings_app.DB_NAME]
        m_collection: pymongo.collection.Collection = m_db[settings_app.DB_ENTRIES]
        entries_query: pymongo.cursor.Cursor = m_collection.find( {} )  # the cursor will return all entries when accessed
    except:
        log.exception( 'problem accessing mongo' )
        pass
    # log.debug( f'entries_query (first 10), ```{pprint.pformat(entries_query[0:10])}```...' )  # NB! - this would cause entries_query to only contain 10 items!
    log.debug( f'returning entries_query' )
    return entries_query


def query_entry( id: str, request ) -> dict:  # could be {}
    """ Returns entry.
        Called by views.api_entry(), accessed by views.entry() """
    log.debug( 'starting query_entry' )
    connect_str: str = prep_connect_str( request )
    doc = {}
    log.debug( 'starting try' )
    try:
        m_client: pymongo.mongo_client.MongoClient = pymongo.MongoClient( connect_str )
        m_db: pymongo.database.Database = m_client[settings_app.DB_NAME]
        m_collection: pymongo.collection.Collection = m_db[settings_app.DB_ENTRIES]
        q = { '_id': bson.ObjectId( id ) }
        entry_query: pymongo.cursor.Cursor = m_collection.find( q )  # the cursor will return all entries when accessed
        log.debug( 'about to start loop' )
        for entry in entry_query:
            log.debug( f'entry, ```{entry}```' )
            log.debug( f'type(entry), ``{type(entry)}``' )
            doc = entry
            break
    except:
        log.exception( 'problem accessing mongo' )
        raise Exception( 'failure' )
    log.debug( f'doc, ```{pprint.pformat(doc)}```' )
    return doc


# def query_entry( id: str, request ) -> pymongo.cursor.Cursor:  # or None
#     """ Returns entry.
#         Called by views.api_entry(), accessed by views.entry() """
#     log.debug( 'starting query_entry' )
#     connect_str: str = prep_connect_str( request )
#     entry_query = None
#     log.debug( 'starting try' )
#     try:
#         m_client: pymongo.mongo_client.MongoClient = pymongo.MongoClient( connect_str )
#         m_db: pymongo.database.Database = m_client[settings_app.DB_NAME]
#         m_collection: pymongo.collection.Collection = m_db[settings_app.DB_ENTRIES]
#         q = { '_id': ObjectId( id ) }
#         # q = { 'latitude': 26.492979 }
#         entry_query: pymongo.cursor.Cursor = m_collection.find( q )  # the cursor will return all entries when accessed
#         ## temp
#         log.debug( 'about to start loop' )
#         for doc in entry_query:
#             log.debug( f'doc, ```{doc}```' )
#     except:
#         log.exception( 'problem accessing mongo' )
#         raise Exception( 'failure' )
#     log.debug( f'entry_query, ```{pprint.pformat(entry_query.__dict__)}```' )
#     return entry_query


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
