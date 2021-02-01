"""
添加图例
==============

当利用 :meth:`pygmt.Figure.plot` 绘图时为 ``label`` 选项赋值，
:meth:`pygmt.Figure.legend` 会自动产生图例。

.. note::

    可结合《:doc:`gmtdoc:module/legend` 模块》和《:doc:`gmtdoc:tutorial/legend`》学习。

"""

import pygmt

fig = pygmt.Figure()

fig.basemap(projection="x1i", region=[0, 7, 3, 7], frame=True)

fig.plot(
    data="@Table_5_11.txt",
    style="c0.15i",
    color="lightgreen",
    pen="faint",
    label="Apples",
)
fig.plot(data="@Table_5_11.txt", pen="1.5p,gray", label='"My lines"')
fig.plot(data="@Table_5_11.txt", style="t0.15i", color="orange", label="Oranges")

fig.legend(position="JTR+jTR+o0.2c", box=True)

fig.show()

#%%

import numpy as np
import pygmt

np.random.seed(19680801)
n = 200  # 创建的数据点个数

fig = pygmt.Figure()
fig.basemap(
    region=[-0.1, 1.1, -0.1, 1.1],
    projection="X10c/10c",
    frame=["xa0.2fg", "ya0.2fg", "WSrt"],
)
for color in ["blue", "orange", "green"]:
    x, y = np.random.rand(2, n)  # x y 范围 [0,1]
    sizes = np.random.rand(n) * 0.5  # 范围 [0,0.5], in cm

    fig.plot(
        x=x,
        y=y,
        style="cc",
        sizes=sizes,
        color=color,
        # 设置图例
        # 设置图例中的符号大小为 0.25 cm (+S0.25c)
        label=f"{color}+S0.25c",
        transparency=70,  # 设置所有符号的透明度
    )

fig.legend(transparency=30)  # 设置图例的透明度
fig.show()