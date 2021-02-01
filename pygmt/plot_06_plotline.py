"""
绘制线条
============

利用 PyGMT 的 :meth:`pygmt.Figure.plot` 可以绘制线条。

.. note::

    可结合《:doc:`gmtdoc:tutorial/lines`》
    和《:doc:`gmtdoc:module/plot` 模块》学习。

"""

#%%
# 绘制单条线段
# ---------------

import pygmt
# sphinx_gallery_thumbnail_number = 5
fig = pygmt.Figure()
fig.plot(
    region=[0, 10, 0, 10],  
    projection="X25c/20c",  # 设置投影方式为笛卡尔坐标
    frame="a",
    x=[1, 8],
    y=[5, 9],  # （1，5）和（8，9）两点连成一条线
    pen="1p,black",
)
fig.show()

#%%

fig = pygmt.Figure()
fig.plot(
    region=[0, 10, 0, 10],
    projection="X25c/20c",
    frame="a",
    x=[1, 6, 9],
    y=[5, 7, 4],  # 三个点相连
    pen="1p,black",
)
fig.show()

#%%
# 绘制多条线段
# -----------------

fig = pygmt.Figure()

# 绘制第一条线段
fig.plot(
    region=[0, 10, 0, 10],
    projection="X25c/20c",
    frame="a",
    x=[1, 6, 9],
    y=[5, 7, 4],
    pen="2p,blue,..-",
)

# 绘制第二条线段
fig.plot(x=[2, 4, 10], y=[3, 8, 9], pen="2p,red,-.-")
fig.show()

#%%
# 线条样式
# ---------------

import numpy as np
import pygmt

# 生成绘制线段所用的两个点
x = np.array([0, 7])
y = np.array([9, 9])

fig = pygmt.Figure()
fig.basemap(region=[0, 10, 0, 10], projection="X15c/8c", frame='+t"Line Styles"')

# 利用默认样式绘制线段
fig.plot(x=x, y=y)
fig.text(x=x[-1], y=y[-1], text="solid (default)", justify="ML", offset="0.2c/0c")

# 利用不同的线条样式绘图
for linestyle in [
    "1p,red,-",  # dashed line
    "1p,blue,.",  # dotted line
    "1p,lightblue,-.",  # dash-dotted line
    "2p,blue,..-",  # dot-dot-dashed line
    "2p,tomato,--.",  # dash-dash-dotted line
    "2p,tomato,4_2:2p",  # A pattern of 4-point-long line segment and 2-point-gap between segment
]:
    y -= 1  # 绘制完成后向下移动
    fig.plot(x=x, y=y, pen=linestyle)
    fig.text(x=x[-1], y=y[-1], text=linestyle, justify="ML", offset="0.2c/0c")

# 绘制火车轨道线
# 难点在于要先绘制黑线再绘制白线
y -= 1  
fig.plot(x=x, y=y, pen="5p,black")
fig.plot(x=x, y=y, pen="4p,white,20p_20p")
fig.text(x=x[-1], y=y[-1], text="5p,black", justify="ML", offset="0.2c/0.2c")
fig.text(x=x[-1], y=y[-1], text="4p,white,20p_20p", justify="ML", offset="0.2c/-0.2c")

fig.show()

#%%
# 自定义线条颜色
# ------------------
#
# 利用 :meth:`pygmt.Figure.plot` 绘图时，设置 ``cmap=True`` 以及 ``pen=+z``
# PyGMT 就会根据 ``zvalue`` 选项的值映射颜色表。

import numpy as np
import pygmt

# 构建 x 坐标数据集
x = np.arange(start=20, stop=30, step=0.2)

fig = pygmt.Figure()
fig.basemap(frame=["WSne", "af"], region=[20, 30, -10, 10])

# 制作自定义 CPT
pygmt.makecpt(cmap="batlow", series=[0, 10, 1])

# 绘制 10 条不同 zvalue 值的线条
for zvalue in range(0, 10):
    y = zvalue * np.sin(x)
    fig.plot(x=x, y=y, cmap=True, zvalue=zvalue, pen="thick,+z,-")
# 显示 colorbar
fig.colorbar()
fig.show() 