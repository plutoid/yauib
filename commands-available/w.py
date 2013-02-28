#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import os
import subprocess

'''

create:Thu Feb 28 21:56:53 CST 2013
http://www.cnblogs.com/henq/archive/2012/02/28/2371503.html
'''
     

city_name = sys.argv[1]
p = subprocess.Popen("""grep %s /home/pluto/yauib/commands-available/city.txt | awk '{print $2}' """ % city_name , shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
city_id = '101020500'
for city_id in p.stdout.readlines():
    if city_id[-1] == '\n':
        city_id = city_id[0:-1]

weather_info = ""
p = subprocess.Popen('curl http://m.weather.com.cn/data/%s.html ' % city_id, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    weather_info = line

s=json.loads(weather_info)
ss = s["weatherinfo"]["city"] +',' + s["weatherinfo"]["date_y"] +',' + s["weatherinfo"]["week"] +',' + s["weatherinfo"]["temp1"] +',' + s["weatherinfo"]["weather1"] +',' + s["weatherinfo"]["wind1"] +',' +s["weatherinfo"]["index_d"]
print ss.encode("UTF-8")



