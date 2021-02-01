"""
读取日期数据
==============

PyGMT 支持以下类型的日期数据：

- :class:`numpy.datetime64`

- :class:`pandas.DatetimeIndex`

- :class:`xarray.DataArray`

- ISO 格式的字符串（比如 ``YYYY-MM-DD``，``YYYY-MM-DDTHH`` 和 ``YYYY-MM-DDTHH:MM:SS``）

- Python 内置的 :class:`datetime.datetime` 和 :class:`datetime.date`

将上述任意一种格式的日期数据传递给 :meth:`pygmt.Figure.plot` 的 ``x``、``y`` 选项即可。

此时 ``region`` 选项的输入格式为 *date_min/date_max/ymin/ymax*。

.. note::

    可结合《:doc:`gmtdoc:basis/io-format`》
    和《:doc:`gmtdoc:conf/format`》学习。

"""

import datetime

import numpy as np
import pandas as pd
import pygmt
import xarray as xr

fig = pygmt.Figure()

# 创建底图，x 轴范围为 2010-01-01 到 2020-06-01，y 轴范围为 0 到 10 
fig.basemap(
    projection="X15c/5c", region="2010-01-01/2020-06-01/0/10", frame=["WSen", "af"]
)

# numpy.datetime64 格式
x = np.array(["2010-06-01", "2011-06-01T12", "2012-01-01T12:34:56"], dtype="datetime64")
y = [1, 2, 3]
fig.plot(x, y, style="c0.4c", pen="1p", color="red3")

# pandas.DatetimeIndex 格式
x = pd.date_range("2013", periods=3, freq="YS")
y = [4, 5, 6]
fig.plot(x, y, style="t0.4c", pen="1p", color="gold")

# xarray.DataArray 格式
x = xr.DataArray(data=pd.date_range(start="2015-03", periods=3, freq="QS"))
y = [7.5, 6, 4.5]
fig.plot(x, y, style="s0.4c", pen="1p")

# raw datetime strings 格式
x = ["2016-02-01", "2016-06-04T14", "2016-10-04T00:00:15"]
y = [7, 8, 9]
fig.plot(x, y, style="a0.4c", pen="1p", color="dodgerblue")

# Python 内置 datetime and date
x = [datetime.date(2018, 1, 1), datetime.datetime(2019, 6, 1, 20, 5, 45)]
y = [6.5, 4.5]
fig.plot(x, y, style="i0.4c", pen="1p", color="seagreen")

fig.show()