# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint

import requests
from mp_vl_app import settings_app
from django.conf import settings
from django.core.urlresolvers import reverse


log = logging.getLogger(__name__)


def build_data( scheme, host, user ):
    """ Builds and returns data-dct.
        Called by views.db_list()"""
    log.debug( f'host, `{host}`' )
    api_url = f'{scheme}://{host}{reverse("api_entries_url")}'
    log.debug( f'api_url, ```{api_url}```' )
    r = requests.get( api_url )
    data = r.json()
    updated_data = data.copy()
    for record in updated_data:
        log.debug( f'record, ```{pprint.pformat(record)}```' )
        dt_obj, dt_display = None, None
        try:
            date_dct = record['date']
            dt_obj = datetime.date( date_dct['year'], date_dct['month'], date_dct['day'] )
        except:
            pass
        if dt_obj:
            dt_display = dt_obj.strftime( '%Y %B %d' )
            if 'modifier' in date_dct.keys():
                mod_value = date_dct['modifier'].lower()
                dt_display = f'{dt_display} ({mod_value})'
        record['date_display'] = dt_display
    context = { 'data': updated_data }
    username = None
    if user.is_authenticated:
        username = user.first_name
        context['logged_in'] = True
    else:
        context['logged_in'] = False
    context['username'] = username
    log.debug( f'context.keys(), ```{pprint.pformat(context.keys())}```' )
    return context


# def make_context( request, rq_now, info_txt, taken ):
#     """ Builds and returns context.
#         Called by views.info() """
#     cntxt = {
#         'request': {
#             'url': '%s://%s%s' % ( request.scheme,
#                 request.META.get( 'HTTP_HOST', '127.0.0.1' ),  # HTTP_HOST doesn't exist for client-tests
#                 request.META.get('REQUEST_URI', request.META['PATH_INFO'])
#                 ),
#             'timestamp': str( rq_now )
#         },
#         'response': {
#             'documentation': settings_app.README_URL,
#             'version': info_txt,
#             'elapsed_time': str( taken )
#         }
#     }
#     return cntxt
