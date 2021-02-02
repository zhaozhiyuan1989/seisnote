"""
在地图上添加 logo
===================

利用 :meth:`pygmt.Figure.logo` 可以将 GMT 的
图形 logo 绘制在图上。

.. note::

    可结合《:doc:`gmtdoc:module/gmtlogo` 模块》学习。
"""

import pygmt

fig = pygmt.Figure()
fig.basemap(region=[0, 10, 0, 2], projection="X6c", frame=True)

fig.logo(position="jTR+o0.3c/0.6c+w3c")

fig.show()