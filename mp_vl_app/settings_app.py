# -*- coding: utf-8 -*-

import json, os


README_URL = os.environ['MV_DJ__README_URL']

## auth
SUPER_USERS = json.loads( os.environ['MV_DJ__SUPER_USERS_JSON'] )
STAFF_USERS = json.loads( os.environ['MV_DJ__STAFF_USERS_JSON'] )  # users permitted access to admin
STAFF_GROUP = os.environ['MV_DJ__STAFF_GROUP']  # not grouper-group; rather, name of django-admin group for permissions
TEST_META_DCT = json.loads( os.environ['MV_DJ__TEST_META_DCT_JSON'] )
# POST_LOGIN_ADMIN_REVERSE_URL = os.environ['MV_DJ__POST_LOGIN_ADMIN_REVERSE_URL']  # tricky; for a direct-view of a model, the string would be in the form of: `admin:APP-NAME_MODEL-NAME_changelist`

## mongo
DB_HOST = os.environ['MV_DJ__MONGO_HOST']
DB_PORT =  os.environ['MV_DJ__MONGO_PORT']
DB_NAME = os.environ['MV_DJ__MONGO_DATABASE_NAME']
DB_ENTRIES = os.environ['MV_DJ__MONGO_ENTRIES_COLLECTION_NAME']
DB_USER =  os.environ['MV_DJ__MONGO_USERNAME']
DB_PASS =  os.environ['MV_DJ__MONGO_PASSWORD']
