"""
绘制线条
============

利用 PyGMT 的 :meth:`pygmt.Figure.plot` 可以绘制线条。

.. note::

    可结合《:doc:`gmtdoc:tutorial/lines`》
    和《:doc:`gmtdoc:module/plot` 模块》学习。

"""

#%%
# 绘制简单符号
# ---------------
#
# 首先利用 :mod:`numpy.random` 模块生成数据集：

import numpy as np

np.random.seed(42)
region = [150, 240, -10, 60]
x = np.random.uniform(region[0], region[1], 20)
y = np.random.uniform(region[2], region[3], 20)
z = np.random.uniform(1,5,20)
print("x:\n", x)
print("y:\n", y)
print("z:\n", z)
#%%
# 通过 :meth:`pygmt.Figure.plot` 绘制符号时需要用 ``style`` 选项控制符号类型和大小：

import pygmt

fig = pygmt.Figure()
fig.basemap(region=region, projection="X8c", frame=True)
# 绘制三角符号（i），大小为 0.5 厘米（0.5c）
fig.plot(x, y, style="i0.5c", color="black")
fig.show()

#%%
# 大小变化的符号
# -----------------
#
# 绘制大小变化的符号时在选项 ``style`` 中说明
# 符号类型和单位，由 ``sizes`` 控制符号大小：

fig = pygmt.Figure()
fig.basemap(region=region, projection="X8c", frame=["nSWe","af"])
# 绘制五角星符号（a），单位为厘米（c），大小由 sizes 控制
fig.plot(x, y, style="ac", pen="1p,black", color="red", sizes=z*0.1)
fig.show()

#%%
# 颜色变化的符号
# ---------------
#
# 如果想要让符号的颜色根据某个数值的不同而使用不同的颜色，
# 则需要使用 ``color`` 选项。``color`` 选项表示符号的
# 填充色由某个数值以及 CPT 颜色表所控制。
# CPT 颜色表给出了数值与颜色之间的对应关系。
# 因而对于任意一个符号，我们都可以给其一个数值，
# PyGMT 会根据该数值从 CPT 颜色表中找到对应的颜色作为该符号的填充色。
# 因而，在输入数据中，需要在 X 和 Y 坐标的基础上额外加一列 Z 值，
# 用于控制符号的填充色。
#
# 下面的示例中，首先使用 :func:`pygmt.makecpt` 模块，以内置 CPT 颜色表 hot 为基础，
# 生成了一个新的 CPT 颜色表，该 CPT 颜色表为 1 到 5 之内的每个数值都对应了一个颜色。
# 在使用 :meth:`pygmt.Figure.plot` 绘制符号时，通过 ``color`` 选项决定每个符号的填充颜色：

fig = pygmt.Figure()
fig.basemap(region=region, projection="X8c", frame=["nSWe","af"])
pygmt.makecpt(cmap='hot', series=[1, 5])
# 绘制圆形符号（c），单位为厘米（c），大小由 sizes 控制
fig.plot(x, y, style="cc", pen="1p,black", sizes=z*0.1, color=z, cmap=True)
fig.show()

#%%
# 具有透明度的符号
# -----------------
#
# :meth:`pygmt.Figure.plot` 的 ``transparency`` 选项可以为符号添加透明度。
#
# 首先利用 :mod:`numpy` 模块的 :func:`numpy.arange` 函数和 :func:`numpy.ones` 函数生成示例数据：

x = np.arange(0, 105, 5)
y = np.ones(x.size)
print('x:\n', x)
print('y:\n', y)

#%%

transparency = x

fig = pygmt.Figure()
fig.basemap(
    region=[-5, 105, 0, 2],
    frame=['xaf+l"Transparency level"+u%', "WSrt"],
    projection="X15c/6c",
)
fig.plot(x=x, y=y, style="c0.6c", color="blue", pen="1p,red", transparency=transparency)
fig.show()

#%%
# 示例
# -----------
#
# 通过 PyGMT 提供的 :mod:`pygmt.datasets` 包可以访问 GMT 服务器上
# 的示例数据。第一次访问时，数据会自动下载并保存到 GMT 的缓存目录中（通常为 ``~/.gmt/cache``）。
#
# 通过 :func:`pygmt.datasets.load_japan_quakes` 函数加载日本附近海啸诱发地震，
# 数据以 :class:`pandas.DataFrame` 形式加载。

# sphinx_gallery_thumbnail_number = 7
data = pygmt.datasets.load_japan_quakes()  # 从服务器加载数据

# 绘图区域一般比数据区域大一点
region = [
    data.longitude.min() - 1,
    data.longitude.max() + 1,
    data.latitude.min() - 1,
    data.latitude.max() + 1,
]

print(region)  # 打印绘图区域
print(data.head())  # 打印 data 数据结构

########################################################################################
# 利用 :meth:`pygmt.Figure.plot` 方法绘制震中分布：

fig = pygmt.Figure()  # 创建绘图实例
fig.basemap(region=region, projection="M15c", frame=True)  # 绘制底图
fig.coast(land="black", water="skyblue")  # 绘制海岸线

# 把 data 的 longitude 和 latitude 值赋予 x、y，调整绘图参数进行绘制
fig.plot(x=data.longitude, y=data.latitude, style="c0.3c", color="white", pen="1p,black")
fig.show()

########################################################################################
# 其中，``style="c0.3c"`` 表示将数据点绘制成半径为 0.3 厘米的圆，
# ``color="white"`` 和 ``pen="1p,black"`` 分别控制了符号的填充样式和边框样式。
#
# 通过 ``sizes`` 参数可以用圆的大小来表征地震震级，这里通过幂运算可以更好的表现震级差异：

fig = pygmt.Figure()
fig.basemap(region=region, projection="M15c", frame=True)
fig.coast(land="black", water="skyblue")

# 在 style 中不显式指定符号大小，此时符号大小由 sizes 控制
fig.plot(
    x=data.longitude,
    y=data.latitude,
    sizes=0.02 * (2 ** data.magnitude),
    style="cc",
    color="white",
    pen="1p,black",
)
fig.show()

########################################################################################
# 请注意，上例中 ``style="cc"`` 并没有指明符号大小，
# 仅包含符号 ``c`` （圆形）和单位 ``c`` （厘米）。
#
#
# 那么如何用符号的填充颜色来表征发震深度呢？简单来说，
# 首先根据发震深度利用 :func:`pygmt.makecpt` 创建一个连续的颜色表，
# 然后在 :meth:`pygmt.Figure.plot` 中设置 ``cmap=True`` 使用颜色映射即可。
#

fig = pygmt.Figure()
fig.basemap(region=region, projection="M15c", frame=True)
fig.coast(land="black", water="skyblue")

# 将 data.depth_km 的最小值和最大值赋予 series 指定 cpt 数值范围
# 使用 matplotlib 的 viridis 颜色表
pygmt.makecpt(cmap="viridis", series=[data.depth_km.min(), data.depth_km.max()])

fig.plot(
    x=data.longitude,
    y=data.latitude,
    sizes=0.02 * 2 ** data.magnitude,
    color=data.depth_km,  # 发震深度决定填充颜色
    cmap=True,  # 设置为 True 表示使用 makecpt 制作的 cpt 作为颜色表
    style="cc",
    pen="1p,black",
)

# 绘制 colorbar
fig.colorbar(frame='af+l"Depth (km)"')
fig.show()