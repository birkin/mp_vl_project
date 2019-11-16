# -*- coding: utf-8 -*-

""" By default, this module is not accessed.
    To use:
    - shib-protect the `/project/login/` url
    - enable the two login urls in urls.py
    - enable import and function in views.py
    - enable settings in settings_app.py """

import copy, json, logging, os, pprint

from django.conf import settings as project_settings
from django.contrib.auth import authenticate, get_backends, login
from django.contrib.auth.models import User, Group
from django.http import HttpResponseForbidden
from mp_vl_app import settings_app


log = logging.getLogger(__name__)


def shib_login(func):
    """ Decorator to create a user object for the Shib user, if necessary, and log the user into Django.
        Called by views.py decorators. """
    log.debug( 'starting shib_login() decorator' )
    def decorator(request, *args, **kwargs):
        log.debug( '\n\nstarting shib_login() decorator sub-function' )
        # log.debug( f'request.META, ```{pprint.pformat(request.META)}```' )
        log.debug( f'coming from, ```{request.META.get("HTTP_REFERER", "referrer_unknown")}```' )
        log.debug( f'heading to, ```{request.META["PATH_INFO"]}```' )
        log.debug( f'authenticated?, ```{request.user.is_authenticated}```' )
        # log.debug( f'request.META, ```{pprint.pformat(request.META)}```' )
        # log.debug( f'request.META["PATH_INFO"], `{request.META["PATH_INFO"]}`' )
        host = request.META.get( 'HTTP_HOST', '127.0.0.1' )
        log.debug( f'host, `{host}`' )
        if request.user.is_authenticated == True:
            log.debug( 'user already logged in; skipping authentication' )
            pass
        elif ( request.META.get( 'PATH_INFO', 'xxxxx' )[0:5] == '/api/' ) and ( host in project_settings.ALLOWED_HOSTS ):
            log.debug( 'internal api call; skipping authentication' )
            pass
        else:
            log.debug( 'user not logged in; proceed w/shib-check' )
            hlpr = LoginDecoratorHelper()
            cleaned_meta_dct = hlpr.prep_shib_dct( request.META, request.get_host() )
            user_obj = hlpr.manage_usr_obj( request, cleaned_meta_dct )
            if not user_obj:
                return HttpResponseForbidden( '403 / Forbidden' )
        return func(request, *args, **kwargs)
    return decorator


class LoginDecoratorHelper(object):
    """ Handles login decorator code. """

    def __init__( self ):
        pass

    def prep_shib_dct( self, request_meta_dct, host ):
        """ Returns dct from shib-info.
            Called by shib_login() """
        log.debug( 'starting prep_shib_dct()' )
        new_dct = copy.copy( request_meta_dct )
        for (key, val) in request_meta_dct.items():  # get rid of some dictionary items not serializable
            if 'passenger' in key:
                new_dct.pop( key )
            elif 'wsgi.' in key:
                new_dct.pop( key )
        if host == '127.0.0.1' or host == '127.0.0.1:8000':
            new_dct = settings_app.TEST_META_DCT
        # log.debug( 'new_dct, ```{}```'.format(pprint.pformat(new_dct)) )
        log.debug( f'new_dct, ```{new_dct}```' )
        return new_dct

    def manage_usr_obj( self, request, meta_dct ):
        """ Pull information for the Shib request and get/create and login Django User object.
            Called by shib_login() """
        ( username, netid, email ) = self.ensure_basics( meta_dct )
        if not username or not netid or not email:
            return
        usr = self.update_userobj( meta_dct )
        backend = get_backends()[0]
        usr.backend = '{module}.{classname}'.format( module=backend.__module__, classname=backend.__class__.__name__ )
        login( request, usr )  #Brute force login, see - http://djangosnippets.org/snippets/1552/
        log.debug( 'login complete' )
        return usr

    def ensure_basics( self, meta_dct ):
        """ Ensures essential elements exist.
            Called by manage_usr_obj() """
        # log.debug( 'meta_dct, ```%s```' % pprint.pformat(meta_dct) )
        log.debug( f'meta_dct, ```{meta_dct}```' )
        username = meta_dct.get( 'Shibboleth-eppn', None )
        netid = meta_dct.get( 'Shibboleth-brownNetId', None )
        email = meta_dct.get( 'Shibboleth-mail', None )
        log.debug( 'username, `{usr}`; netid, `{net}`'.format( usr=username, net=netid ) )
        return ( username, netid, email )

    def update_userobj( self, meta_dct ):
        """ Grabs user object, updates and saves it.
            Called by manage_usr_obj() """
        # log.debug( 'meta_dct, ```%s```' % pprint.pformat(meta_dct) )
        log.debug( f'meta_dct, ```{meta_dct}```' )
        usrnm = meta_dct['Shibboleth-eppn']
        log.debug( 'usrnm-b, `%s`' % usrnm )
        try:
            usr, created = User.objects.get_or_create( username=usrnm )
        except Exception as e:
            log.exception( 'problem getting or creating user' )
            # raise Exception( msg )
        netid = meta_dct['Shibboleth-brownNetId']
        if netid in settings_app.SUPER_USERS:
            usr.is_superuser = True
        if netid in settings_app.STAFF_USERS:
            usr.is_staff = True
        # usr.is_staff = True  # use this and comment out the two lines above if, say, you define a shib-group to be able to log-in
        try:
            usr = self.update_user( usr, meta_dct )
        except Exception as e:
            log.exception( 'problem updating user' )
            # raise Exception( msg )
        try:
            usr.save()
        except Exception as e:
            log.exception( 'problem saving user' )
            # raise Exception( msg )
        log.debug( 'user updated and saved' )
        log.debug( 'user-obj, ```%s```' % pprint.pformat(usr.__dict__) )
        return usr

    def update_user( self, usr, meta_dct ):
        """ Adds user to the default group.
            Called by update_userobj() """
        usr.first_name = meta_dct.get( 'Shibboleth-givenName', '' )
        usr.last_name = meta_dct.get( 'Shibboleth-sn', '' )
        usr.email = meta_dct['Shibboleth-mail']
        usr.set_unusable_password()
        usr.save()
        grp = Group.objects.get( name=settings_app.STAFF_GROUP )  # group must exist; TODO: autocreate if it doesn't
        grp.user_set.add( usr )
        log.debug( 'user updated' )
        return usr

    ## end class LoginDecoratorHelper()
