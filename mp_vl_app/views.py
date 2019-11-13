# -*- coding: utf-8 -*-

import datetime, json, logging, os, pprint
from mp_vl_app import settings_app
from mp_vl_app.lib import views_version_helper, views_info_helper, views_dblist_helper
from mp_vl_app.lib.shib_auth import shib_login  # decorator
from django.conf import settings as project_settings
from django.contrib.auth import logout as django_logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


log = logging.getLogger(__name__)


def info( request ):
    """ Displays home page. """
    data = views_info_helper.build_data( request.user )
    if request.GET.get('format', '') == 'json':
        resp = HttpResponse( json.dumps(data, sort_keys=True, indent=2), content_type='application/javascript; charset=utf-8' )
    else:
        resp = render( request, 'mp_vl_app_templates/home.html', data )
    return resp


@shib_login
def db_list( request ):
    """ Displays db-listing-summary. """
    data = views_dblist_helper.build_data( request.user )
    if request.GET.get('format', '') == 'json':
        resp = HttpResponse( json.dumps(data, sort_keys=True, indent=2), content_type='application/javascript; charset=utf-8' )
    else:
        resp = render( request, 'mp_vl_app_templates/db_list.html', data )
    return resp
    # return HttpResponse( 'db-listing-summary coming' )


@shib_login
def login( request ):
    """ Handles authNZ, & redirects to admin.
        Called by click on login or admin link. """
    next_url = request.GET.get( 'next', None )
    if not next_url:
        redirect_url = reverse( 'db_list_url' )
    else:
        redirect_url = request.GET['next']  # will often be same page
    return HttpResponseRedirect( redirect_url )


def logout( request ):
    """ Logs _app_ out; shib logout not yet implemented.
        Called by click on Logout link in header-bar. """
    redirect_url = request.GET.get( 'next', None )
    if not redirect_url:
        redirect_url = reverse( 'info_url' )
    django_logout( request )
    log.debug( 'redirect_url, ```%s```' % redirect_url )
    return HttpResponseRedirect( redirect_url )


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
