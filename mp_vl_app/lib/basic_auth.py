# -*- coding: utf-8 -*-

import base64, logging, pprint
from mp_vl_app import settings_app


log = logging.getLogger(__name__)


def check_basic_auth( request ) -> bool:
    """ Checks for any, and correct, http-basic-auth info, returns boolean.
        Called by views.try_again() """
    log.debug( 'request.__dict__, ```%s```' % pprint.pformat(request.__dict__) )
    basic_auth_ok = False
    auth_info = request.META.get( 'HTTP_AUTHORIZATION', None )
    log.debug( 'type(auth_info), `%s`; auth_info, ```%s```' % (type(auth_info), auth_info) )

    user_agent = request.META.get( 'HTTP_USER_AGENT', 'unavailable' )
    if user_agent in settings_app.BASIC_AUTH_DICT.keys():
        log.debug( 'user_agent ok' )

        if ( auth_info and auth_info.startswith('Basic ') ):
            basic_info = auth_info.lstrip( 'Basic ' )
            decoded_basic_bytes = base64.b64decode( basic_info )
            log.debug( 'type(decoded_basic_bytes), `%s`; decoded_basic_bytes, ```%s```' % (type(decoded_basic_bytes), decoded_basic_bytes) )
            decoded_basic_str = decoded_basic_bytes.decode( 'utf-8' )
            ( received_identity, received_password ) = decoded_basic_str.rsplit( ':', 1 )   # cool; 'rsplit-1' solves problem if 'username' contains one or more colons
            log.debug( 'received_identity, ```%s```; received_password, ```%s`' % (received_identity, received_password) )
            # if received_identity == settings_app.BASIC_AUTH_USER and received_password == settings_app.BASIC_AUTH_PASSWORD:
            if received_identity == settings_app.BASIC_AUTH_USER and received_password == settings_app.BASIC_AUTH_PASSWORD:

                basic_auth_ok = True
    log.debug( 'basic_auth_ok, `%s`' % basic_auth_ok )
    return basic_auth_ok


# def check_basic_auth( request ):
#     """ Checks for any, and correct, http-basic-auth info, returns boolean.
#         Called by views.try_again() """
#     basic_auth_ok = False
#     auth_info = request.META.get( 'HTTP_AUTHORIZATION', None )
#     if ( auth_info and auth_info.startswith('Basic ') ):
#         basic_info = auth_info.lstrip( 'Basic ' )
#         decoded_basic_bytes = base64.b64decode( basic_info )  # yes, bytes not str
#         decoded_basic_str = decoded_basic_bytes.decode( 'utf-8' )
#         ( received_username, received_password ) = decoded_basic_str.rsplit( ':', 1 )   # cool; 'rsplit-1' solves problem if 'username' contains one or more colons
#         if received_username == settings_app.BASIC_AUTH_USER and received_password == settings_app.BASIC_AUTH_PASSWORD:
#             basic_auth_ok = True
#     log.debug( 'basic_auth_ok, `%s`' % basic_auth_ok )
#     return basic_auth_ok


def display_prompt():
    """ Builds http-basic-auth response which brings up username/password dialog box.
        Not used -- for example usage, see easyscan_app.views.try_again() """
    response = HttpResponse()
    response.status_code = 401
    response['WWW-Authenticate'] = 'Basic realm="brown-illiad-api"'
    return response
