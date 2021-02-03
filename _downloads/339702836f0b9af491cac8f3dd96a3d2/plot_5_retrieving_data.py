"""
从数据中心申请地震数据
============================

通过 :mod:`obspy.clients.fdsn` 模块可以访问任何支持
`FDSN Web Services <https://www.fdsn.org/webservices/>`__
协议的网络服务器，功能强大，基本上可以满足科研需求，
比如下载波形数据、地震目录和台站元数据等。

.. warning:: 

    由于数据中心和 Web 服务可能会有变化，所以本节的相关示例未来可能会失效，
    当出现这种情况的时候请自行参阅最新文档。

"""

#%%
# 第一步，初始化 client 对象，总是需要执行这一步：

from obspy.clients.fdsn import Client
client = Client("IRIS")  # 这里既可以用数据中心的简写，也可以用 URL 地址

#%%
# 显示当前可用的数据中心列表：

from obspy.clients.fdsn.header import URL_MAPPINGS
for key in sorted(URL_MAPPINGS.keys()):
    print("{0:<7} {1}".format(key,  URL_MAPPINGS[key]))
    
#%%
# 下载波形数据
# ---------------
# 
# 通过 :meth:`get_waveforms() <obspy.clients.fdsn.client.Client.get_waveforms>` 方法
# 从服务器下载波形数据时，可以添加关键字参数自定义申请数据。
# 
# 例如，添加参数 ``filename="1.mseed"`` 后将会把申请的数据保存在本地目录中
# 的 :file:`1.mseed` ，返回对象的结果为 ``None`` ；
# 
# 设置 ``attach_response=True`` 将为波形数据添加仪器响应信息。
#
# 以下示例申请了美国 IU 台网 ANMO 和 AFI 台站 LHZ 分量
# 从 2010-02-27 06:45 (UTC) 开始的 60 分钟连续波形数据，结果作为
# :class:`Stream <obspy.core.stream.Stream>` 对象返回。
# 如果想同时发送多个请求可以使用
# :meth:`get_waveforms_bulk() <obspy.clients.fdsn.client.Client.get_waveforms_bulk>` 方法。

from obspy import UTCDateTime
t = UTCDateTime("2010-02-27T06:45:00.000")
st = client.get_waveforms("IU", "ANMO,AFI", "00", "LHZ", t, t + 60 * 60)  # 多个参数使用逗号分隔
print(st)
#st.plot(size=(800,300)) 

#%%
# 当然也可以使用通配符作为参数：

st = client.get_waveforms("IU", "A*", "1?", "LHZ", t, t + 5)  
print(st)
#st.plot()

#%%
# 申请波形数据时添加仪器响应信息：

t = UTCDateTime("2012-12-14T10:36:01.6Z")
st = client.get_waveforms("TA", "E42A", "*", "BH?", t+300, t+400,
                          attach_response=True)  
st.remove_response(output="VEL")   # 去除仪器响应
print(st)
#st.plot(size=(800,400))

#%%
# 利用 :meth:`get_waveforms_bulk() <obspy.clients.fdsn.client.Client.get_waveforms_bulk>` 方法
# 可以同时提交多个申请， 符合要求的 **bulk** 有以下形式：
# 
# - 多个列表项组成的列表，每一个列表项必须包含 ``network, station, location, channel, starttime and endtime``
# - 包含有效 ``request`` 的字符串
# - 包含有效 ``request`` 的文件名
# - 包含有效 ``request`` 的已打开文件的句柄
#
# 多个列表项组成的列表:

client = Client("IRIS")
t1 = UTCDateTime("2010-02-27T06:30:00.000")
t2 = t1 + 1
t3 = t1 + 3
bulk = [("IU", "ANMO", "*", "BHZ", t1, t2),
          ("IU", "AFI", "1?", "BHE", t1, t3),
            ("GR", "GRA1", "*", "BH*", t2, t3)]
st = client.get_waveforms_bulk(bulk)
print(st)
#st.plot()

#%%
# 包含有效 ``request`` 的字符串:

bulk = 'quality=B\n' + \
         'longestonly=false\n' + \
         'IU ANMO * BHZ 2010-02-27 2010-02-27T00:00:02\n' + \
         'IU AFI 1? BHE 2010-02-27 2010-02-27T00:00:04\n' + \
         'GR GRA1 * BH? 2010-02-27 2010-02-27T00:00:02\n'
st = client.get_waveforms_bulk(bulk)
print(st)
#st.plot()

# 包含 request 的文件:
#st = client.get_waveforms_bulk("request.txt", attach_response=True)
#st.remove_response(output="VEL")

#%%
# 下载地震事件
# --------------------
# 通过 :meth:`get_events <obspy.clients.fdsn.client.Client.get_events>` 方法
# 可以从服务器申请地震数据，申请结果返回 :class:`Catalog <obspy.core.event.Catalog>` 对象。
#
# 用 ``eventid`` 申请地震：

client = Client("IRIS")
cat = client.get_events(eventid=609301)
print(cat)

#%%
# 用起止时间和震级等条件筛选地震，然后
# 利用 :class:`Catalog <obspy.core.event.Catalog>` 的
# :meth:`plot() <obspy.core.event.Catalog.plot>` 方法绘制震中分布图：

t1 = UTCDateTime("2001-01-07T00:00:00")
t2 = UTCDateTime("2001-01-07T03:00:00")
cat = client.get_events(starttime=t1, endtime=t2, minmagnitude=4,
                        catalog="ISC")
print(cat)
cat.plot(projection="ortho")

#%%
# 下载台站数据
# ------------------
# 通过 :meth:`get_stations <obspy.clients.fdsn.client.Client.get_stations>` 方法
# 可以从服务器申请台站数据，
# 申请结果返回 :class:`Inventory <obspy.core.inventory.inventory.Inventory>` 对象：

inventory = client.get_stations(network="IU", station="A*",
                                 starttime=t1,
                                 endtime=t2, level="response")  # 申请所有台站的所有分量和仪器响应文件
print(inventory)

#%%
# 利用 :class:`Inventory <obspy.core.inventory.inventory.Inventory>`
# 的 :meth:`plot() <obspy.core.inventory.inventory.Inventory.plot>` 方法
# 绘制台站分布图：

inventory.plot(projection="local")  # 绘制台站分布

#%%
# 利用 :class:`Inventory <obspy.core.inventory.inventory.Inventory>`
# 的 :meth:`plot_response() <obspy.core.inventory.inventory.Inventory.plot_response>` 方法
# 绘制仪器响应文件：

inventory.plot_response(min_freq=0.01, output="DISP", station="ADK", channel="BH?")  
