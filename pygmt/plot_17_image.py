"""
在地图上添加图片
===================

利用 :meth:`pygmt.Figure.image` 可以读取 EPS 文件
或任意一个光栅图片文件，并将其画在图上。

.. note::

    可结合《:doc:`gmtdoc:module/image` 模块》学习。
"""

import pygmt

fig = pygmt.Figure()

fig.basemap(region=[0, 2, 0, 2], projection="X6c", frame=True)

fig.image(
    # 1. 可直接将 URL 传递给 imagefile 选项
    # 2. 也可将文件名作为字符串传递给 imagefile 选项
    # 3. 或者省略 imagefile 直接把文件名放在第一个位置
    imagefile="https://docs.gmt-china.org/latest/_images/GMT6_Summit_2019.jpg",
    position="g1/1+w4c+jCM",
    box=True,
)

fig.show()