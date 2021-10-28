"""
读写地震数据
=========================

本节简单介绍如何利用 ObsPy 读写地震波形数据、地震目录和元数据。
"""

import glob
import obspy

#%%
# 读写波形数据
# ---------------------
#
# ObsPy 利用 :func:`read() <obspy.core.stream.read>` 函数将各种格式的
# 地震数据（如 SAC、MiniSEED 等）读入 :class:`Stream <obspy.core.stream.Stream>` 中。
#
# :class:`Stream <obspy.core.stream.Stream>` 类似于列表对象，可以包含多个
# :class:`Trace <obspy.core.trace.Trace>`。
#
# 每个 :class:`Trace <obspy.core.trace.Trace>` 都包含指向连续时间序列的 ``data``
# 属性和指向所有元数据的 ``stats`` 属性。例如，``starttime`` 和 ``endtime`` 等
# 元数据都以字典形式储存在 :class:`Stats <obspy.core.trace.Stats>` 对象中。 
#
# 经过处理后，可以用 :meth:`write() <obspy.core.stream.Stream.write>` 方法将数据保存到本地。
#
# 下面举例说明：
#  
# **从服务器读取波形数据并写入到本地文件**

tr = obspy.read()  # 从服务器读取波形数据示例文件到 Stream 对象中
print(tr)  # 打印 Stream 对象信息
tr.write("test.mseed")  # 将波形数据保存到本地，可通过后缀名确定文件类型
#%%
# **从本地读取地震波形数据并转换格式存储到本地**

for file in glob.glob('*.sac'):  # 遍历当前目录中以 ".sac" 结尾的文件
    st = obspy.read(file)  # 将数据读取到以 st 命名的 Stream 对象中
    tr = st[0]  # 把 Stream 对象中的第一个 Trace 赋予变量 tr
    # 打印头段变量和经过处理的波形数据
    msg = "%s %s %f %f" % (tr.stats.station, str(tr.stats.starttime),tr.data.mean(), tr.data.std())  
    print(msg)
    print(tr.stats)  # 打印元数据
  # tr.write(file+".mseed", format="mseed")  # 以 mseed 格式存储至本地
    print("===================================================\n")

#%%
# **从本地读取 miniseed 地震波形数据并转换格式存储到本地**
import obspy
import glob
st=obspy.read('E04834KP.544')
print(st[0].stats)

for tr in st:
    #print(type(tr))
    filename='.'.join([tr.stats.network,tr.stats.station,tr.stats.location,tr.stats.channel])
    tr.write(filename+'.sac')

st1=obspy.Stream()
for file in glob.glob('*.sac'):
    st1+=obspy.read(file)
st1.write('test.mseed')
st1.plot()

for tr1 in st1:
    print(tr1.stats)
    
#%%    
# 读写地震目录
# -------------------
#
# 利用 :func:`read_events() <obspy.core.event.catalog.read_events>` 函数
# 读取地震目录到 :class:`Catalog <obspy.core.event.Catalog>` 对象，
# 然后通过 :meth:`write() <obspy.core.event.Catalog.write>` 方法保存到本地。

cat = obspy.read_events()  # 从服务器读取地震目录示例文件
print(cat)  # 打印地震目录信息
cat.write('events', format='kml')  # 以 kml格式存储至本地


#%%
# 读写元数据
# -------------------
# 
# 可以通过 :func:`read_inventory() <obspy.core.inventory.inventory.read_inventory>` 函数
# 读取元数据到 :class:`Inventory <obspy.core.inventory.inventory.Inventory>` 对象，
# 然后利用 :meth:`write() <obspy.core.inventory.inventory.Inventory.write>` 方法
# 将元数据保存到本地。

inv = obspy.read_inventory()  # 从服务器读取元数据示例文件
print(inv)  # 打印元数据信息
inv.write('inv.pz', format='sacpz')  # 以 pz 格式存储至本地

#%%
# 删除临时文件

import os
os.remove("test.mseed")
os.remove("events.kml")
os.remove("inv.pz")