# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint, urllib.parse
import pymongo

from django.conf import settings as project_settings
from django.contrib.auth import logout as django_logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from mp_vl_app import settings_app
from mp_vl_app.lib import mongo_access
from mp_vl_app.lib import views_version_helper, views_info_helper, views_dblist_helper, views_api_entries_helper
from mp_vl_app.lib.shib_auth import shib_login  # decorator


log = logging.getLogger(__name__)


def info( request ):
    """ Displays home page. """
    log.debug( '\n\nstarting info()' )
    log.debug( f'session, ```{request.session.items()}```' )
    problem_message = None
    if 'problem_message' in request.session.keys():
        problem_message = request.session['problem_message']
        request.session.flush()
    data = views_info_helper.build_data( request.user, problem_message )
    if request.GET.get('format', '') == 'json':
        resp = HttpResponse( json.dumps(data, sort_keys=True, indent=2), content_type='application/javascript; charset=utf-8' )
    else:
        resp = render( request, 'mp_vl_app_templates/home.html', data )
    log.debug( 'returning resp' )
    return resp


@shib_login
def db_list( request ):
    """ Displays db-listing-summary. """
    log.debug( '\n\nstarting db_list()' )
    ( scheme, host ) = ( request.scheme, request.META.get('HTTP_HOST', '127.0.0.1') )
    context = views_dblist_helper.build_data( scheme, host, request.user )
    if request.GET.get('format', '') == 'json':
        resp = HttpResponse( json.dumps(context, sort_keys=True, indent=2), content_type='application/javascript; charset=utf-8' )
    else:
        resp = render( request, 'mp_vl_app_templates/db_list.html', context )
    log.debug( 'returning resp' )
    return resp


@shib_login
def login( request ):
    """ Handles authNZ, & redirects to admin.
        Called by click on login or admin link. """
    log.debug( '\n\nstarting login()' )
    next_url = request.GET.get( 'next', None )
    if not next_url:
        redirect_url = reverse( 'db_list_url' )
    else:
        redirect_url = request.GET['next']  # will often be same page
    log.debug( f'returning redirect response to, ```{redirect_url}```' )
    return HttpResponseRedirect( redirect_url )


def logout( request ):
    """ Logs _app_ out; shib logout not yet implemented.
        Called by click on Logout link in header-bar. """
    log.debug( '\n\nstarting logout()' )
    redirect_url = request.GET.get( 'next', None )
    if not redirect_url:
        redirect_url = reverse( 'info_url' )
    django_logout( request )
    log.debug( f'logout complete; returning redirect response to, ```{redirect_url}```' )
    return HttpResponseRedirect( redirect_url )


@shib_login
def api_entries( request ):
    """ Returns json for entries.
        Currently used by views.db_list() """
    log.debug( '\n\nstarting api_entries()' )
    # if project_settings.DEBUG == True and request.META.get('HTTP_HOST', '127.0.0.1')[0:9] == '127.0.0.1':
    #     connect_str = f'mongodb://{settings_app.DB_HOST}:{settings_app.DB_PORT}/'
    # else:
    #     username = urllib.parse.quote_plus( settings_app.DB_USER )
    #     password = urllib.parse.quote_plus( settings_app.DB_PASS )
    #     connect_str_init = f'mongodb://{username}:{password}@{settings_app.DB_HOST}:{settings_app.DB_PORT}/'
    #     log.debug( f'connect_str_init, ```{connect_str_init}```' )
    #     connect_str = f'{connect_str_init}?authSource={settings_app.DB_NAME}'
    connect_str = mongo_access.prep_connect_str( request )
    log.debug( f'connect_str, ```{connect_str}```' )
    try:
        m_client = pymongo.MongoClient( connect_str )
        m_db = m_client[settings_app.DB_NAME]
        m_collection = m_db[settings_app.DB_ENTRIES]
        # entries_jsn = m_collection.find_one()
        entries_q = m_collection.find( {} )
    except:
        message = 'problem accessing mongo'
        log.exception( message )
        raise Exception( message )
    try:
        entries = []
        for ( idx, doc ) in enumerate( entries_q ):
            doc = views_api_entries_helper.massage_doc_data( doc )
            entries.append( doc )
            # if idx > 10:
            #     break
        log.debug( f'entries-type, `{type(entries)}`; entries, ```{pprint.pformat(entries)}```' )
        entries_jsn = json.dumps( entries, sort_keys=True, indent=2 )
        # log.debug( f'entries_jsn, ```{pprint.pformat(entries_jsn)[0:1000]}```' )
    except:
        message = 'problem processing mongo data'
        log.exception( message )
        raise Exception( message )

    assert len(entries_jsn) > 10, len(entries_jsn)
    assert type(entries_jsn) == str, type(entries_jsn)
    log.debug( 'returning entries_jsn response' )
    return HttpResponse( entries_jsn, content_type='application/json; charset=utf-8' )


# @shib_login
# def api_entries( request ):
#     """ Returns json for entries.
#         Currently used by views.db_list() """
#     log.debug( '\n\nstarting api_entries()' )
#     if project_settings.DEBUG == True and request.META.get('HTTP_HOST', '127.0.0.1')[0:9] == '127.0.0.1':
#         connect_str = f'mongodb://{settings_app.DB_HOST}:{settings_app.DB_PORT}/'
#     else:
#         username = urllib.parse.quote_plus( settings_app.DB_USER )
#         password = urllib.parse.quote_plus( settings_app.DB_PASS )
#         connect_str_init = f'mongodb://{username}:{password}@{settings_app.DB_HOST}:{settings_app.DB_PORT}/'
#         log.debug( f'connect_str_init, ```{connect_str_init}```' )
#         connect_str = f'{connect_str_init}?authSource={settings_app.DB_NAME}'
#     log.debug( f'connect_str, ```{connect_str}```' )
#     try:
#         m_client = pymongo.MongoClient( connect_str )
#         m_db = m_client[settings_app.DB_NAME]
#         m_collection = m_db[settings_app.DB_ENTRIES]
#         # entries_jsn = m_collection.find_one()
#         entries_q = m_collection.find( {} )
#     except:
#         message = 'problem accessing mongo'
#         log.exception( message )
#         raise Exception( message )
#     try:
#         entries = []
#         for ( idx, doc ) in enumerate( entries_q ):
#             doc = entrs_hlpr.massage_doc_data( doc )
#             entries.append( doc )
#             if idx > 10:
#                 break
#         log.debug( f'entries-type, `{type(entries)}`; entries, ```{pprint.pformat(entries)}```' )
#         entries_jsn = json.dumps( entries, sort_keys=True, indent=2 )
#         # log.debug( f'entries_jsn, ```{pprint.pformat(entries_jsn)[0:1000]}```' )
#     except:
#         message = 'problem processing mongo data'
#         log.exception( message )
#         raise Exception( message )

#     assert len(entries_jsn) > 10, len(entries_jsn)
#     assert type(entries_jsn) == str, type(entries_jsn)
#     log.debug( 'returning entries_jsn response' )
#     return HttpResponse( entries_jsn, content_type='application/json; charset=utf-8' )


# ===========================
# for development convenience
# ===========================


def version( request ):
    """ Returns basic data including branch & commit. """
    # log.debug( 'request.__dict__, ```%s```' % pprint.pformat(request.__dict__) )
    rq_now = datetime.datetime.now()
    commit = views_version_helper.get_commit()
    branch = views_version_helper.get_branch()
    info_txt = commit.replace( 'commit', branch )
    resp_now = datetime.datetime.now()
    taken = resp_now - rq_now
    context_dct = views_version_helper.make_context( request, rq_now, info_txt, taken )
    output = json.dumps( context_dct, sort_keys=True, indent=2 )
    return HttpResponse( output, content_type='application/json; charset=utf-8' )


def error_check( request ):
    """ For an easy way to check that admins receive error-emails (in development).
        To view error-emails in runserver-development:
        - run, in another terminal window: `python -m smtpd -n -c DebuggingServer localhost:1026`,
        - (or substitue your own settings for localhost:1026)
    """
    if project_settings.DEBUG == True:
        1/0
    else:
        return HttpResponseNotFound( '<div>404 / Not Found</div>' )


# @shib_login
# def login( request ):
#     """ Handles authNZ, & redirects to admin.
#         Called by click on login or admin link. """
#     next_url = request.GET.get( 'next', None )
#     if not next_url:
#         redirect_url = reverse( settings_app.POST_LOGIN_ADMIN_REVERSE_URL )
#     else:
#         redirect_url = request.GET['next']  # will often be same page
#     log.debug( 'redirect_url, ```%s```' % redirect_url )
#     return HttpResponseRedirect( redirect_url )
