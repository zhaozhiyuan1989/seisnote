"""
绘制海岸线
======================

PyGMT 利用 :meth:`pygmt.Figure.coast` 方法绘制海岸线，
该方法不仅可以绘制海岸线和湖岸线，还可以绘制比例尺和行政边界等。

.. note::

    可结合《:doc:`gmtdoc:tutorial/coastline`》
    和《:doc:`gmtdoc:module/coast` 模块》学习。

"""

import pygmt

#%%
# 海岸线
# ----------
#
# 使用 ``shorelines`` 选项绘制海岸线：

# sphinx_gallery_thumbnail_number = 4
fig = pygmt.Figure()
fig.basemap(region="g", projection="W15c", frame=True)
fig.coast(shorelines=True)
fig.show()

#%%
# 海岸线分为四个等级（ *level* 取 1-4）：
#
# 1. coastline：海岸线
# 2. lakeshore：湖泊与陆地的岸线
# 3. island-in-lake shore：首先要有陆地，陆地中有个湖，湖里有个岛。即岛的岸线
# 4. lake-in-island-in-lake shore：首先有陆地，陆地中有个湖，湖中有个岛，岛里又有个湖。这里指的是湖的岸线
#
# 海岸线绘制效果由级别参数 *level* 和画笔参数 *pen* 共同决定。
# 下图绘制了岸线级别 *level* 为 ``1``\ ，
# 画笔参数 *pen* 为 ``0.5p/black`` 的全球海岸线样式：

fig = pygmt.Figure()
fig.basemap(region="g", projection="W15c", frame=True)
fig.coast(shorelines="1/0.5p,black")
fig.show()

#%%
# 允许通过列表形式一次性传递多个不同等级海岸线的绘制参数：

fig = pygmt.Figure()
fig.basemap(region="g", projection="W15c", frame=True)
fig.coast(shorelines=["1/1p,black", "2/0.5p,red"])
fig.show()

#%%
# 海岸线数据分为 5 个不同精度版本，通过 ``resolution`` 选项指定要使用的数据精度：
#
# 1. ``"c"``: crude
# 2. ``"l"``: low (default)
# 3. ``"i"``: intermediate
# 4. ``"h"``: high
# 5. ``"f"``: full

oahu = [-158.3, -157.6, 21.2, 21.8]
fig = pygmt.Figure()
for res in ["c", "l", "i", "h", "f"]:
    fig.coast(resolution=res, shorelines="1p", region=oahu, projection="M5c")
    fig.shift_origin(xshift="5c")
fig.show()

#%%
# 使用 ``land`` 和 ``water`` 选项可以指定如何填充陆地与水体：

fig = pygmt.Figure()
fig.basemap(region="g", projection="W10i", frame=True)
fig.coast(land="#666666", water="skyblue")
fig.show()

#%%
# 行政边界
# --------------------
#
# 利用 ``borders`` 选项可以绘制国界、州界等行政边界，可供选择的参数有：
#
# 1. ``"1"``: National boundaries
# 2. ``"2"``: State boundaries within the Americas
# 3. ``"3"``: Marine boundaries
# 4. ``"a"``: All boundaries (1-3)
#

import pygmt

fig = pygmt.Figure()
fig.basemap(region=[-150, -30, -60, 60], projection="I-90/8c", frame="afg")
# 用不同的颜色绘制不同等级的行政边界
fig.coast(borders=["1/0.5p,black", "2/0.5p,red", "3/0.5p,blue"], land="gray")
fig.show()