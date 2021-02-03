"""
绘制沙滩球
==============

利用 :meth:`pygmt.Figure.meca` 可以绘制沙滩球。

.. note::

    可结合《:doc:`gmtdoc:module/meca` 模块》学习。

这里给出一个简单的示例，详细的说明请参考 :meth:`pygmt.Figure.meca` 方法。

"""

#%%
# 利用字典传入数据
# ------------------

# sphinx_gallery_thumbnail_number = 2
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
focal_mechanism = dict(strike=330, dip=30, rake=90, magnitude=3, longitude=-124.3, latitude=48.1, depth=12.0)

# 传入震源机制解参数，用 scale 选项控制绘制大小
fig.meca(focal_mechanism, scale="1c")

fig.show()

#%%
# 利用文本传入数据
# ---------------------

fig = pygmt.Figure()
fig.coast(
    region="102.5/105.5/30.5/32.5",
    projection="Q104/15c",
    land="grey",
    frame=["WSen", "a"],
)

# 构建输入文本
with open("examples.txt", "w") as f:
    f.write("104.3300  31.90    39.8  32.00 64.00   85.00  7.0 0        0        A\n")
    f.write("104       31.52    27.1  22.00 53.00   57.00  6.0 0        0        B\n")
    f.write("103.6700  31.1300   6.4  86.00 32.00  -65.00  8.0 0        0        C\n")
    f.write("103.900   31.3400  43.6 194.00 84.00  179.00  4.9 104.180  30.8400  D\n")
    f.write("103.7200  31.4400  67.3  73.00 84.00 -162.00  4.9 103.120  31.6400  E\n")
    f.write("104.1200  31.7800  12.7 186.00 68.00  107.00  4.7 103.830  32.2600  F\n")
    f.write("104.2300  31.6100  62.0  86.00 63.00  -51.00  4.7 104.960  31.6900  G\n")

# 输入文件时需要 convention 指定震源机制解的格式，可以添加 offset 偏移震源球位置
fig.meca("examples.txt", scale="1c", convention="aki", offset="0.1p,red,.+s0.2c")
fig.show()

#%%
# PyGMT 访问 GMT 模块
# --------------------
# 目前 PyGMT 的功能还不是很齐全，对于目前无法实现的功能可以
# 利用 PyGMT 的 :class:`pygmt.clib.Session` 访问 GMT 模块的功能。

fig = pygmt.Figure()
fig.coast(
    region="102.5/105.5/30.5/32.5",
    projection="Q104/15c",
    land="grey",
    frame=["WSen", "a"],
)

# 生成 CPT 文件，为每个深度设置不同的颜色
with open('meca.cpt','w') as f:
    f.write(" 0   0-1-1   20   0-1-1\n")
    f.write("20  60-1-1   40  60-1-1\n")
    f.write("40 120-1-1   60 120-1-1\n")
    f.write("60 240-1-1  100 240-1-1\n")

with pygmt.clib.Session() as session:
    session.call_module('meca','examples.txt -CP5p -Sa1.3c -Zmeca.cpt')
    session.call_module('colorbar','-Cmeca.cpt -DjBL+w5c/0.5c+ml+o0.8c/0.4c -Bx+lDepth -By+lkm -S')

fig.show()
#%%
# 清除临时文件

import os
os.remove("examples.txt")
os.remove("meca.cpt")