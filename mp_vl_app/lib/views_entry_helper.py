# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint
# from typing import List

import django, requests
from mp_vl_app import settings_app
from django.conf import settings
from django.core.urlresolvers import reverse


log = logging.getLogger(__name__)


def build_get_data( id: str, scheme: str, host: str, user: django.utils.functional.SimpleLazyObject, start_time: datetime.datetime ) -> dict:
    """ Builds and returns data-dct.
        Called by views.entry() """
    log.debug( f'host, `{host}`' )
    api_url = f'{scheme}://{host}{reverse( "api_entry_url", kwargs={"id":id} )}'
    log.debug( f'api_url, ```{api_url}```' )

    raw_data = {}
    credentials: dict = get_credentials()
    if credentials:
        r = requests.get( api_url, auth=(credentials['ba_identity'], credentials['ba_password']), verify=True, timeout=10 )
        if r.status_code == 200:
            raw_data: List(dict) = r.json()
    context = { 'data': raw_data }

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


def get_credentials() -> dict:
    """ Gets the ip-auth-key for the api call.
        Called by build_data() """
    credentials = {}
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname( hostname )
        log.debug( f'ip, ``{ip}``' )
        auth_key = f'ip_{ip}'
        credentials: dict = settings_app.BASIC_AUTH_DICT[ auth_key ]
    except:
        log.exception( 'problem determining credentials; returning empty {}' )
    log.debug( f'credentials, ``{credentials}``' )
    return credentials
