"""
读写地震数据
=========================

本节简单介绍如何利用 ``ObsPy`` 读写地震波形数据、地震目录和元数据。
"""

import glob
import obspy

#%%
# 从服务器读取波形数据并写入到本地文件

tr = obspy.read()  
print(tr)
tr.write("test.mseed")
#%%
# 从本地读取地震波形数据并转换格式存储到本地

for file in glob.glob('*.sac'):  # 遍历当前目录中以 sac 结尾的文件
    st = obspy.read(file)  # 读取 sac 文件以 Stream 对象的形式赋予变量 st
    tr = st[0]  # Stream 可以有多个 Trace，每个 Trace 都包含波形数据和元数据，将第一个 Trace 赋予变量 tr
    # 打印头段变量和经过处理的波形数据
    msg = "%s %s %f %f" % (tr.stats.station, str(tr.stats.starttime),tr.data.mean(), tr.data.std())  
    print(msg)
    print(tr.stats)  # 打印元数据
  # tr.write(file+".mseed", format="mseed")  # 以 mseed 格式存储至本地
    print("===================================================\n")
    
#%%    
# 从服务器读取地震目录并写入到本地文件

cat = obspy.read_events()
print(cat)
cat.write('events', format='kml')  # 以kml格式存储至本地


#%%
# 从服务器读取元数据并写入到本地文件

inv = obspy.read_inventory()
print(inv)
inv.write('inv.pz', format='sacpz')  # 以pz格式存储至本地
