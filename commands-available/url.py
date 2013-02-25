#!/usr/bin/env python
# coding: utf-8
# Fri Feb 22 18:48:14 CST 2013
# by regal2u@gmail.com

import subprocess
import re
import sys
import os


p = subprocess.Popen('curl %s'% sys.argv[1], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    title = re.findall("<title.*?\/title>", line) 
    if len(title) == 1:
        print title[0]

