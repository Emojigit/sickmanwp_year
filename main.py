#!/usr/bin/env python3
import datetime, os, time, subprocess, sys
try:
    import pytz
except ModuleNotFoundError:
    print("Installing required depends: pytz")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pytz'])
    import pytz

try:
    import pandas
except ModuleNotFoundError:
    print("Installing required depends: pandas")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])
    import pandas

os.environ['TZ'] = 'UTC'
time.tzset()
fyear = datetime.datetime(2019,7,4,12,0)# 2019年7月4日下午12：00
nyear = pandas.Timestamp.max
oyear = datetime.timedelta(hours=12)
print("start:",fyear)
for a in pandas.date_range(fyear,nyear,freq='12h'):
    print("earth:",a,"SickManWP:",((a - fyear)/oyear))

now = pandas.to_datetime("now")
print("---------------")
# Requested by sunny00217wm, https://t.me/SickManWPfriends/44894
print("Now earth year:",now)
print("Now dragging year:",((now - fyear)/oyear))
