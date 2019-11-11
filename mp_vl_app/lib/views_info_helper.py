# -*- coding: utf-8 -*-

import datetime, json, logging, os
from mp_vl_app import settings_app
from django.conf import settings
# from django.core.urlresolvers import reverse


log = logging.getLogger(__name__)


def build_data( request ):
    """ Builds and returns data-dct.
        Called by views.info()"""
    return {}


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
