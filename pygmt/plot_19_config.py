"""
配置参数
===================

利用 :class:`pygmt.config` 可以修改 PyGMT 的绘图参数。

.. note::

    可结合《:doc:`gmtdoc:conf/index` 》学习。
"""

import pygmt

#%%
# 默认参数绘图
# --------------

# sphinx_gallery_thumbnail_number = 3
fig = pygmt.Figure()
fig.basemap(region=[115, 119.5, 4, 7.5], projection="M10c", frame=True)
fig.coast(land="black", water="skyblue")

fig.show()

#%%
# 设置全局参数
# -------------------

fig = pygmt.Figure()

# 全局参数影响接下来所有的命令
pygmt.config(MAP_FRAME_TYPE="plain")
pygmt.config(FORMAT_GEO_MAP="ddd.xx")

fig.basemap(region=[115, 119.5, 4, 7.5], projection="M10c", frame=True)
fig.coast(land="black", water="skyblue")

fig.show()

#%%
# 设置临时参数
# -----------------

fig = pygmt.Figure()

# 仅对当前命令有效，将边框设置为 fancy+
with pygmt.config(MAP_FRAME_TYPE="fancy+"):
    fig.basemap(region=[115, 119.5, 4, 7.5], projection="M10c", frame=True)
fig.coast(land="black", water="skyblue")

# 移动原点绘制下一张图
fig.shift_origin(yshift="-10c")

# 边框恢复为 fancy
fig.basemap(region=[115, 119.5, 4, 7.5], projection="M10c", frame=True)
fig.coast(land="black", water="skyblue")

fig.show()