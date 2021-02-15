#!/usr/bin/env python3
import datetime, pytz, os, time, pandas
os.environ['TZ'] = 'UTC'
time.tzset()
# 參考：Emojiwiki（公元28年1月－224年4月）
fyear = datetime.datetime(2019,7,3,0,0)# 2019年7月3日上午12：00
nyear = datetime.datetime.today() #Now date
#nyear = datetime.datetime(2022,4,10,0,0)
oyear = datetime.timedelta(hours=12)
print("start:",fyear)
#print("2:",nyear)
#td = (nyear - fyear)
#print("td:",td)
#print((td/oyear))
for a in pandas.date_range(fyear,nyear,freq='12h'):
    print("earth:",a,"SickManWP:",((a - fyear)/oyear))
