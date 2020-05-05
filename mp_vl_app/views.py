# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint, urllib.parse

import django, pymongo
from django.conf import settings as project_settings
from django.contrib.auth import logout as django_logout
from django.core.handlers import wsgi  # just for type-annotation
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse  # was `from django.core.urlresolvers import reverse` -- deprecated
from mp_vl_app import settings_app
from mp_vl_app.lib import mongo_access
from mp_vl_app.lib import views_dblist_helper, views_api_entries_helper
from mp_vl_app.lib import views_entry_helper
from mp_vl_app.lib import views_version_helper, views_info_helper
from mp_vl_app.lib.shib_auth import shib_login  # decorator


log = logging.getLogger(__name__)


def info( request: wsgi.WSGIRequest ):  # type-annotation just for reference
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
    ( scheme, host, start_time ) = (
        request.scheme, request.META.get('HTTP_HOST', '127.0.0.1'), datetime.datetime.now() )  # scheme: str, host: str, start_time: datetime.datetime
    context: dict = views_dblist_helper.build_data( scheme, host, request.user, start_time )  # request.user: django.utils.functional.SimpleLazyObject<django.contrib.auth.models.User>
    if request.GET.get('format', '') == 'json':
        resp = HttpResponse( json.dumps(context, sort_keys=True, indent=2), content_type='application/javascript; charset=utf-8' )
    else:
        resp = render( request, 'mp_vl_app_templates/db_list.html', context )
    log.debug( 'returning resp' )
    return resp


@shib_login
def entry( request, id: str ):
    """ Displays db-listing-summary. """
    log.debug( '\n\nstarting entry()' )
    # return HttpResponse( '<p>entry info coming</p>' )
    ( scheme, host, start_time ) = (
        request.scheme, request.META.get('HTTP_HOST', '127.0.0.1'), datetime.datetime.now() )  # scheme: str, host: str, start_time: datetime.datetime
    context: dict = views_entry_helper.build_get_data( id, scheme, host, request.user, start_time )  # request.user: django.utils.functional.SimpleLazyObject<django.contrib.auth.models.User>
    if request.GET.get('format', '') == 'json':
        resp = HttpResponse( json.dumps(context, sort_keys=True, indent=2), content_type='application/javascript; charset=utf-8' )
    else:
        resp = render( request, 'mp_vl_app_templates/entry.html', context )
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


# ===========================
# api urls
# ===========================


@shib_login
def api_entries( request ):
    """ Returns json for entries.
        Currently used by views.db_list() """
    log.debug( '\n\nstarting api_entries()' )
    connect_str = mongo_access.prep_connect_str( request )
    entries_query = mongo_access.query_entries( connect_str )  # probable TODO: instantiate the helper and save the connect-string as an instance-attribute.
    entries_jsn = views_api_entries_helper.massage_docs( entries_query )
    log.debug( 'returning entries_jsn response' )
    return HttpResponse( entries_jsn, content_type='application/json; charset=utf-8' )


@shib_login
def api_entry( request, id ):
    """ Returns json for given entry.
        Called by views.entry() """
    try:
        log.debug( '\n\nstarting api_entry()' )
        doc: dict = mongo_access.query_entry( id, request )
        massaged_doc: dict = views_api_entries_helper.massage_doc_data( doc )
        log.debug( f'massaged_doc, ```{pprint.pformat(massaged_doc)}```' )
        entry_jsn = json.dumps( massaged_doc, sort_keys=True, indent=2 )
        # log.debug( 'returning entry_jsn response' )
        log.debug( f'entry_jsn, ```{entry_jsn}```' )
    except:
        log.exception( 'problem with api_entry()' )
    return HttpResponse( entry_jsn, content_type='application/json; charset=utf-8' )


# @shib_login
# def api_entry( request, id ):
#     """ Returns json for given entry.
#         Called by views.entry() """
#     log.debug( '\n\nstarting api_entry()' )
#     entry_query = mongo_access.query_entry( id, request )
#     entry_jsn = views_api_entry_helper.massage_doc( entry_query )
#     # entry_jsn = json.dumps( { 'foo': 'bar' } )
#     log.debug( 'returning entry_jsn response' )
#     return HttpResponse( entry_jsn, content_type='application/json; charset=utf-8' )


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


# ===========================
# react experimentation
# ===========================

def exp_01( request ):
    log.debug( '\n\nstarting exp_01()' )
    context = { 'name_value': request.GET.get( 'name', None ) }
    resp = render( request, 'mp_vl_app_templates/exp_01.html', context )
    return resp

def exp_02( request ):
    log.debug( '\n\nstarting exp_02()' )
    context = {}
    resp = render( request, 'mp_vl_app_templates/exp_02.html', context )
    return resp

def exp_03( request ):
    log.debug( '\n\nstarting exp_03()' )
    context = {}
    resp = render( request, 'mp_vl_app_templates/exp_03.html', context )
    return resp

def exp_04( request ):
    log.debug( '\n\nstarting exp_04()' )
    context = {}
    resp = render( request, 'mp_vl_app_templates/exp_04.html', context )
    return resp

def exp_05( request ):
    log.debug( '\n\nstarting exp_05()' )
    context = {}
    resp = render( request, 'mp_vl_app_templates/exp_05.html', context )
    return resp

# ---------------------


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
