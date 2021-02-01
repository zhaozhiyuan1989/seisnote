"""
设置绘图区域
========================

利用 PyGMT 绘图时需要通过 ``region`` 选项来设置绘图区域，本节介绍
``region`` 选项支持的输入格式。

.. note::

    可结合《:doc:`gmtdoc:option/R`》和《:doc:`gmtdoc:dataset/dcw/index`》学习。

"""

import pygmt

#%%
# 利用经纬度坐标设置绘图区域
# --------------------------
#
# ``region`` 选项主要支持两种经纬度坐标形式，分别为 *xmin/xmax/ymin/ymax*、
# *[xmin,xmax,ymin,ymax]* 以及 *xlleft/ylleft/xuright/yuright+r* 三种。
#
# *xmin/xmax/ymin/ymax*
# ^^^^^^^^^^^^^^^^^^^^^^^^^^

# sphinx_gallery_thumbnail_number = 4
fig = pygmt.Figure()
fig.coast(
    # 经度范围 10E 到 20E，纬度范围 35N 到 45N
    region="10/20/35/45",
    # 墨卡托投影,图片宽度为 15 厘米
    projection="M15c",
    # 设置陆地颜色
    land="lightgray",
    # 设置水体颜色
    water="white",
    # 设置国界样式
    borders="1/0.5p",
    # 设置海岸线样式
    shorelines="1/0.5p",
    # 设置底图边框格式
    frame="ag",
)
fig.show()

#%%
# *[xmin,xmax,ymin,ymax]*
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^

fig = pygmt.Figure()
fig.coast(
    # 经度范围 10E 到 20E，纬度范围 35N 到 45N
    region=[10, 20, 35, 45],
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()

#%%
# xlleft/ylleft/xuright/yuright+r
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

fig = pygmt.Figure()
fig.coast(
    # 设置左下角坐标（10E, 35N）和右上角坐标（20E, 45N）
    region="10/35/20/45+r",
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()

#%%
# 全球区域
# -----------------
#
# 绘制全球区域时，经纬度坐标可简写为 **d** 或者 **g**。
# 其中， **d** 表示经度范围 180W 到 180E，纬度范围 90S 到 90N，
# 中心点为（0，0），**g** 表示经度范围 0E 到 360E，纬度范围 90S 到 90N，
# 中心点为（180，0）。
#
# **d**
# ^^^^^^^

fig = pygmt.Figure()
fig.coast(
    region="d",
    projection="Cyl_stere/12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()
#%%
# **g**
# ^^^^^^^^

fig = pygmt.Figure()
fig.coast(
    region="g",
    projection="Cyl_stere/12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()
#%%
# ISO 代码
# --------------
#
# ``region`` 选项支持 `ISO code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ 。

fig = pygmt.Figure()
fig.coast(
    # 设置绘图区域为 Japan 
    region="JP",
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()
#%%
# **+r**\ *inc*
# ^^^^^^^^^^^^^^^^^^^^^

fig = pygmt.Figure()
fig.coast(
    # 扩张区域后使得调整后各个方向的范围是 3 的倍数
    region="JP+r3",
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()

#%%
# **+r**\ *xinc/yinc*
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

fig = pygmt.Figure()
fig.coast(
    # 扩张区域后使得调整后经度范围是 3 的倍数，纬度范围是 5 的倍数
    region="JP+r3/5",
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()

#%%
# **+r**\ *winc/einc/sinc/ninc*
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

fig = pygmt.Figure()
fig.coast(
    # 扩张区域后使得调整后左边范围是 3 的倍数，右边范围是 5 的倍数，
    # 下边范围是 7 的倍数，上边范围是 9 的倍数
    region="JP+r3/5/7/9",
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()

#%%
# **+R**\ *inc*
# ^^^^^^^^^^^^^^^^^^^^

fig = pygmt.Figure()
fig.coast(
    # 扩张区域为 3 °
    region="JP+R3",
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()

#%%
# **+e**\ *inc*
# ^^^^^^^^^^^^^^^^^^^^

fig = pygmt.Figure()
fig.coast(
    # 与 +r 类似，但必须保证至少向外扩展 0.25 倍的 inc
    region="JP+e3",
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()