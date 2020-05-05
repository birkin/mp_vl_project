# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint
# from typing import List

import django, requests
from mp_vl_app import settings_app
from django.conf import settings
from django.core.urlresolvers import reverse


log = logging.getLogger(__name__)


# def build_get_data( id: str, scheme: str, host: str, user: django.utils.functional.SimpleLazyObject, start_time: datetime.datetime ) -> dict:
#     """ Builds and returns data-dct.
#         Called by views.entry() """
#     log.debug( f'host, `{host}`' )
#     api_url = f'{scheme}://{host}{reverse( "api_entry_url", kwargs={"id":id} )}'
#     log.debug( f'api_url, ```{api_url}```' )
#     r = requests.get( api_url )
#     data: List(dict) = r.json()
#     context = { 'data': data }
#     username = None
#     if user.is_authenticated:  # `user` becomes `django.contrib.auth.models.User` or `...AnonymousUser`
#         username: str = user.first_name
#         context['logged_in'] = True
#         context['entry_url'] = settings_app.ENTRY_URL
#         context['entry_version_url'] = settings_app.ENTRY_VERSION_URL
#         context['new_entry_url'] = settings_app.NEW_ENTRY_URL
#     else:
#         context['logged_in'] = False
#     context['username'] = username
#     context['time_taken'] = str( datetime.datetime.now() - start_time )
#     log.debug( f'context.keys(), ```{pprint.pformat(context.keys())}```' )
#     return context


def build_get_data( id: str, scheme: str, host: str, user: django.utils.functional.SimpleLazyObject, start_time: datetime.datetime ) -> dict:
    """ Builds and returns data-dct.
        Called by views.entry() """
    log.debug( f'host, `{host}`' )
    api_url = f'{scheme}://{host}{reverse( "api_entry_url", kwargs={"id":id} )}'
    log.debug( f'api_url, ```{api_url}```' )
    r = requests.get( api_url )
    raw_data: List(dict) = r.json()
    context = { 'data': raw_data }
    # context = { 'db_data': raw_data, 'data': process_data(raw_data) }
    username = None
    if user.is_authenticated:  # `user` becomes `django.contrib.auth.models.User` or `...AnonymousUser`
        username: str = user.first_name
        context['logged_in'] = True
        context['entry_url'] = settings_app.ENTRY_URL
        context['entry_version_url'] = settings_app.ENTRY_VERSION_URL
        context['new_entry_url'] = settings_app.NEW_ENTRY_URL
    else:
        context['logged_in'] = False
    context['username'] = username
    context['time_taken'] = str( datetime.datetime.now() - start_time )
    log.debug( f'context.keys(), ```{pprint.pformat(context.keys())}```' )
    return context


# def process_data( raw_data: List(dict) ):
def process_data( raw_data: list ):
    """ Updates db data.
        Called by build_get_data() """
    log.debug( f'raw_data, ``{pprint.pformat(raw_data)}``' )
    data = raw_data.copy()
    log.debug( f'processed-data, ``{pprint.pformat(data)}``' )

    return data
