#!/usr/bin/env python
# -*- coding: utf-8 -*-
from weibo import *
import urllib,httplib

import json
import sys
import os
import subprocess

'''

create:Thu Feb 28 21:56:53 CST 2013
http://www.cnblogs.com/henq/archive/2012/02/28/2371503.html
'''
     



def get_code(APP_KEY,APP_SECRET,ACCOUNT,PASSWORD,CALLBACK_URL):
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    #print 'url = ', url
    conn = httplib.HTTPSConnection('api.weibo.com')
    postdata = urllib.urlencode     ({'client_id':APP_KEY,'response_type':'code','redirect_uri':CALLBACK_URL,'action':'submit','userId':ACCOUNT,'passwd':PASSWORD,'isLoginSina':0,'from':'','regCallback':'','state':'','ticket':'','withOfficalFlag':0})
    conn.request('POST','/oauth2/authorize',postdata,{'Referer':url,'Content-Type': 'application/x-www-form-urlencoded'})
    res = conn.getresponse()
    #print 'headers===========',res.getheaders()
    #print 'msg===========',res.msg
    #print 'status===========',res.status
    #print 'reason===========',res.reason
    #print 'version===========',res.version
    location = res.getheader('location')
    #print location
    code = location.split('=')[1]
    conn.close()
    return code
 

def testwb():
    APP_KEY = '3485752200'            # app key
    APP_SECRET = '576849f0f803915e5132b99eea3b4354'      # app secret
    CALLBACK_URL = 'http://pluto.me'  # callback url
    ACCOUNT = 'linuxfire4irc@qq.com'
    PASSWORD = 'pass'
    code = get_code( APP_KEY,APP_SECRET,ACCOUNT,PASSWORD, CALLBACK_URL)
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
                   redirect_uri= CALLBACK_URL)
    url = client.get_authorize_url()    # redirect the user to `url'
    r = client.request_access_token(code)

    access_token = r.access_token  # access token，e.g., abc123xyz456
    expires_in = r.expires_in      # token expires in
    client.set_access_token(access_token, expires_in)

    client.statuses.user_timeline.get()
    loginfo = sys.argv[1].decode("GBK") 
    client.statuses.update.post(status=loginfo.encode("UTF-8"))

if __name__=='__main__':
    import doctest
    doctest.testmod()
    testwb()

