"""
2. UTCDateTime
====================

本节简单介绍 ``UTCDateTime`` 函数。

“时间问题”是申请地震数据最基本的问题，
利用 ``ObsPy`` 申请数据时需要用 ``UTCDateTime`` 函数
来确定发震时刻、申请波形数据的起始时间和结束时间等。
"""

from obspy import UTCDateTime

#%%
# 打印参考时间和距离零时刻3600秒的时间

UTCDateTime(0) 
UTCDateTime(3600) 

#%%
# 不同日期格式

a = UTCDateTime("2012-09-07T12:15:00")  
b = UTCDateTime(2018, 9, 17, 15, 18, 1.1)
print('a:  ' ,a)
print('b:  ' ,b)

#%%
# 加上时区

UTCDateTime("2012-09-07T12:15:00+08:00")  

#%%
# 查看时间的属性

time = UTCDateTime("2019-04-07T12:15:00")
print('Year:  ', time.year)
print('Month:  ', time.month)
print('Julday:  ', time.julday)
print('Weekday:  ', time.weekday)

#%%
# 时间运算

time1 = UTCDateTime(2018,12,31)
time2 = UTCDateTime("2019-05-01T00:00:00")
print('Interval Day:   ', (time2-time1)/(3600*24))
print(time1+3672.6)
