"""
绘制等高线
==============

利用 :meth:`pygmt.Figure.grdcontour` 绘制等高线。

"""
#%%
# 绘制等高线
# --------------
#
# 首先利用 :func:`pygmt.datasets.load_earth_relief` 从 GMT 服务器读取地形数据：

import pygmt
grid = pygmt.datasets.load_earth_relief(resolution="05m", region=[-92.5, -82.5, -3, 7])

#%%
# :meth:`pygmt.Figure.grdcontour` 读取网格文件后，会同时绘制有标注的等高线和无标注的
# 等高线。在下例中，等高线间距为 500m，每 1000m 进行注释，默认采用等距圆柱投影：

fig = pygmt.Figure()
# sphinx_gallery_thumbnail_number = 3
fig.grdcontour(grid=grid)  # 地形网格文件
fig.show()

#%%
# 设置等高线
# ------------

fig = pygmt.Figure()
fig.grdcontour(
    annotation=1000,  # 等高线标注间隔
    interval=250,  # 等高线绘制间隔 
    grid=grid,
    limit=[-4000, -2000],  # 等高线绘制区间
    projection="M10c",  # 设置投影方式
    frame=True,  # 显示边框
)
fig.show()

#%%
# 添加地形彩图
# ------------
#
# :meth:`pygmt.Figure.grdimage` 可以为 :meth:`pygmt.Figure.grdcontour` 添加地形彩图，
# 学习《:doc:`gmtdoc:tutorial/layers`》后可以知道必须先绘制地形彩图，再绘制等高线。

fig = pygmt.Figure()
fig.grdimage(
    grid=grid,
    cmap="haxby",
    projection="M10c",
    frame=True,
)
fig.grdcontour(
    annotation=1000,
    interval=250,
    grid=grid,
    limit=[-4000, -2000],
)
fig.show() 