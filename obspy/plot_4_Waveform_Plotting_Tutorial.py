"""
波形绘制
================================

本节主要介绍如何利用 ``Stream`` 的 ``plot()`` 方法
来绘制单分量或多分量的地震波形。
"""

from obspy import read

#%%
# 绘制单分量波形
# --------------------
#
# 从服务器读取单分量波形数据：

singlechannel = read('https://examples.obspy.org/COP.BHZ.DK.2009.050')  
singlechannel.plot(outfile='singlechannel.pdf')   # 绘制单分量波形数据，默认大小为 800x250, 保存图像


#%%
# 绘制三分量波形
# ---------------------
#
# 分别读取三分量波形数据并叠加：

threechannels = read('https://examples.obspy.org/COP.BHE.DK.2009.050')
threechannels += read('https://examples.obspy.org/COP.BHN.DK.2009.050')
threechannels += read('https://examples.obspy.org/COP.BHZ.DK.2009.050') 
threechannels.plot(size=(800,400))  # 绘制多分量波形数据，大小为 800x400

#%%
# 自定义绘图
# ---------------------------
# 自定义绘图，更多选项参考 ``plot()`` 方法：

dt = singlechannel[0].stats.starttime
singlechannel.plot(color='red', number_of_ticks=5,
                    tick_rotation=15, tick_format='%I:%M %p',
                    starttime=dt + 60*60, endtime=dt + 60*60 + 120)

#%%
# 绘制 ``dayplot`` 图
# ---------------------------
#
# 绘制 ``dayplot`` 图，参数含义参考 ``plot()``：

singlechannel.plot(type='dayplot', interval=20) 


#%%
# 将地震信息添加到 dayplot 中：

from obspy import read
st = read("https://examples.obspy.org/GR.BFO..LHZ.2012.108")
st.filter("lowpass", freq=0.1, corners=2)  # 低通滤波
st.plot(type="dayplot", interval=60, right_vertical_labels=True,
            vertical_scaling_range=2e4, one_tick_per_line=True,  # 振幅缩放比例2e4, Y轴每个刻度都标上时间
            color=['k', 'r', 'b', 'g'], show_y_UTC_label=False,
            events={'min_magnitude': 6.5})  # 标上6.5级以上地震

#%%
# 绘制 ``section`` 图
# -------------------------

import matplotlib.pyplot as plt
from matplotlib.transforms import blended_transform_factory
from obspy import read, Stream
from obspy.geodetics import gps2dist_azimuth

host = 'https://examples.obspy.org/'
# 文件格式： SAC
files = ['TOK.2011.328.21.10.54.OKR01.HHN.inv',
         'TOK.2011.328.21.10.54.OKR02.HHN.inv',
         'TOK.2011.328.21.10.54.OKR03.HHN.inv',
         'TOK.2011.328.21.10.54.OKR04.HHN.inv',
         'TOK.2011.328.21.10.54.OKR05.HHN.inv',
         'TOK.2011.328.21.10.54.OKR06.HHN.inv',
         'TOK.2011.328.21.10.54.OKR07.HHN.inv',
         'TOK.2011.328.21.10.54.OKR08.HHN.inv',
         'TOK.2011.328.21.10.54.OKR09.HHN.inv',
         'TOK.2011.328.21.10.54.OKR10.HHN.inv']
# 震源
eq_lat = 35.565
eq_lon = -96.792

# 从服务器读取波形数据
st = Stream()
for waveform in files:
    st += read(host + waveform)

# 读取头段变量中的经纬度信息计算震中距，单位为 米
for tr in st:
    tr.stats.distance = gps2dist_azimuth(tr.stats.sac.stla, tr.stats.sac.stlo,
                                         eq_lat, eq_lon)[0]
    # 设置台网名用于图片标题
    tr.stats.network = 'TOK'

st.filter('bandpass', freqmin=0.1, freqmax=10)

fig = plt.figure(figsize=(12, 4))
st.plot(type='section', plot_dx=20e3, recordlength=100,  # x 轴间距为 20km，y 轴长度为 100s
        time_down=True, linewidth=.25, grid_linewidth=.25, show=False, fig=fig)  # 后面还要添加信息时，必须带上后两项

# 添加台站名
ax = fig.axes[0]
transform = blended_transform_factory(ax.transData, ax.transAxes)
for tr in st:
    ax.text(tr.stats.distance / 1e3, 1.0, tr.stats.station, rotation=270,
            va="bottom", ha="center", transform=transform, zorder=10)
plt.show()

#%%
# 利用 ``matplotlib`` 自定义绘图
# -----------------------------------

import matplotlib.pyplot as plt
from obspy import read
st = read()
tr = st[0]
fig = plt.figure(figsize=(12,3))
ax = fig.add_subplot(1, 1, 1)
ax.plot(tr.times("matplotlib"), tr.data, "b-")
ax.xaxis_date()
fig.autofmt_xdate()
plt.show()
