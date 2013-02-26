#!/usr/bin/env python
# coding: utf-8
# Fri Feb 22 18:48:14 CST 2013
# by regal2u@gmail.com

import subprocess
import re
import sys
import os
from BeautifulSoup import BeautifulSoup

'''
Thanks to
http://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
http://stackoverflow.com/questions/3651589/regexp-python-with-parsing-html-page
http://stackoverflow.com/questions/55391/python-regular-expression-for-html-parsing-beautifulsoup
'''

p = subprocess.Popen('curl %s  2>/dev/null'% sys.argv[1], shell=True, stdout=subprocess.PIPE )

htmllist =  p.stdout.readlines()
html = ''.join(map(str, htmllist))
#html = ''.join(str(e) for e in htmllist)

soup = BeautifulSoup(html)
for each in soup.find(name = 'title'):
    print each


