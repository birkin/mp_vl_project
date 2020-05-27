# -*- coding: utf-8 -*-

import base64, logging, pprint
from mp_vl_app import settings_app


log = logging.getLogger(__name__)


def check_basic_auth( request ) -> bool:
    """ Checks for any, and correct, http-basic-auth info, returns boolean.
        Called by views.try_again() """
    # log.debug( 'request.__dict__, ```%s```' % pprint.pformat(request.__dict__) )
    basic_auth_ok = False
    auth_info = request.META.get( 'HTTP_AUTHORIZATION', None )
    log.debug( 'type(auth_info), `%s`; auth_info, ```%s```' % (type(auth_info), auth_info) )

    # user_agent = request.META.get( 'HTTP_USER_AGENT', 'unavailable' )

    if ( auth_info and auth_info.startswith('Basic ') ):
        basic_info = auth_info.lstrip( 'Basic ' )
        decoded_basic_bytes = base64.b64decode( basic_info )
        log.debug( 'type(decoded_basic_bytes), `%s`; decoded_basic_bytes, ```%s```' % (type(decoded_basic_bytes), decoded_basic_bytes) )
        decoded_basic_str = decoded_basic_bytes.decode( 'utf-8' )
        ( received_identity, received_password ) = decoded_basic_str.rsplit( ':', 1 )   # cool; 'rsplit-1' solves problem if 'username' contains one or more colons
        log.debug( 'received_identity, ```%s```; received_password, ```%s`' % (received_identity, received_password) )
        dct_key = 'ip_%s' % request.META.get('REMOTE_ADDR', None)
        if dct_key in settings_app.BASIC_AUTH_DICT.keys():
            legit_credentials: dict = settings_app.BASIC_AUTH_DICT[ dct_key ]
            if received_identity == legit_credentials['ba_identity'] and received_password == legit_credentials['ba_password']:
                basic_auth_ok = True
        else:
            log.warning( 'dct_key, ``{}`` not found in settings_app.BASIC_AUTH_DICT' )
    log.debug( 'basic_auth_ok, `%s`' % basic_auth_ok )
    return basic_auth_ok


def display_prompt():
    """ Builds http-basic-auth response which brings up username/password dialog box.
        Not used -- for example usage, see easyscan_app.views.try_again() """
    response = HttpResponse()
    response.status_code = 401
    response['WWW-Authenticate'] = 'Basic realm="brown-illiad-api"'
    return response
