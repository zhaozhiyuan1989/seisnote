"""
绘制沙滩球
==============

利用 :meth:`pygmt.Figure.meca` 可以绘制沙滩球。

.. note::

    可结合《:doc:`gmtdoc:module/meca` 模块》学习。

这里给出一个简单的示例，详细的说明请参考 :meth:`pygmt.Figure.meca` 方法。

"""

import pygmt

fig = pygmt.Figure()

fig.coast(
    region=[-125, -122, 47, 49],
    projection="M6c",
    land="grey",
    water="lightblue",
    shorelines=True,
    frame="a",
)

# 将震源机制解参数以字典形式存储
focal_mechanism = dict(strike=330, dip=30, rake=90, magnitude=3)

# 传入震源机制解参数，用 scale 选项控制绘制大小
fig.meca(focal_mechanism, scale="1c", longitude=-124.3, latitude=48.1, depth=12.0)

fig.show()