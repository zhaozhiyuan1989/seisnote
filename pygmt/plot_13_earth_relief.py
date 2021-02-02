"""
绘制地形
==============

利用 :meth:`pygmt.Figure.grdimage` 绘制地形。

.. note::

     可结合《:doc:`gmtdoc:tutorial/earth-relief`》和《:doc:`gmtdoc:dataset/earth-relief`》学习。

"""
#%%
# 首先利用 :func:`pygmt.datasets.load_earth_relief` 从 GMT 服务器读取地形数据： 

import pygmt
grid = pygmt.datasets.load_earth_relief(resolution="30m")

#%%
# 利用  :meth:`pygmt.Figure.grdimage` 读取网格文件后绘制地形图，
# 默认采用等距圆柱投影和 turbo 颜色表。

fig = pygmt.Figure()
# sphinx_gallery_thumbnail_number = 4
fig.grdimage(grid=grid)
fig.show()

#%% 
# 可以修改投影方式和颜色表：

fig = pygmt.Figure()
fig.grdimage(grid=grid, projection="R12c", cmap="geo")
fig.show()

#%%
# 添加 colorbar：

fig = pygmt.Figure()
fig.grdimage(grid=grid, projection="R12c", cmap="relief")
fig.colorbar(frame=["a2500", "x+lElevation", "y+lm"])
fig.show()

#%%
# 绘制局部区域：

grid = pygmt.datasets.load_earth_relief(resolution="05m", region=[-14, 30, 35, 60])
fig = pygmt.Figure()
fig.grdimage(grid=grid, projection="M15c", frame="a", cmap="geo")
fig.colorbar(frame=["a1000", "x+lElevation", "y+lm"])
fig.show()
