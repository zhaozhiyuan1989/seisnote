"""
投影方式
===================

PyGMT 支持多种投影方式，绘图时使用 ``projection`` 参数可以指定投影方式。

.. note::

    可结合《:doc:`gmtdoc:proj/index` 》和《:doc:`gmtdoc:option/B`》学习。
"""
#%%
# 在开始之前先用 :func:`numpy.arange` 生成示例数据供下文使用：

import numpy as np
import pygmt

xline = np.arange(0, 101)    # 创建从 0-100（步长为 1） 的 xline 列表
yline = xline ** 0.5        # 将 xline 列表中的值开方后赋予 yline 列表

xpoints = np.arange(0, 101, 10)   # 创建从 0-100（步长为 10） 的 xpoints 列表
ypoints = xpoints ** 0.5    # 将 xpoints 列表中的值开方后赋予 ypoints 列表

#%%
# **-JX:** 笛卡尔线性投影
# ------------------------------

# sphinx_gallery_thumbnail_number = 29
fig = pygmt.Figure()
# 绘制线
fig.plot(
    region=[1, 100, 0, 10],    # 设置绘图区域
    projection="X15c/10c",     # 设置投影方式为笛卡尔线性投影
    frame=["WSne", "ag"],   # 设置底图边框
    x=xline,
    y=yline,
    pen="1p,blue,-",     # 设置线型
)
# 绘制点，超出范围的点也绘制
fig.plot(x=xpoints, y=ypoints, style="c0.3c", color="red", no_clip=True, pen="black")
fig.show()

#%%
# **-JX:** 笛卡尔对数投影
# ----------------------------

fig = pygmt.Figure()
fig.plot(
    region=[1, 100, 0, 10],
    projection="X15cl/10c",   # 设置投影方式为笛卡尔对数投影（l）
    frame=["WSne+gbisque", "xa1f2g3p", "ya2f1g2"],    # 设置边框标签显示为 10 的 n 次方形式（p）
    x=xline,
    y=yline,
    pen="1p,blue,-",
)
fig.plot(x=xpoints, y=ypoints, style="s0.3c", color="green", no_clip=True, pen="black")
fig.show()

#%%
# **-JX:** 笛卡尔指数投影
# --------------------------

fig = pygmt.Figure()
fig.plot(
    region=[1, 100, 0, 10],
    projection="X15cp0.5/10c",   # 设置投影方式为笛卡指数投影，x 轴显示开方后的标注（p0.5）
    frame=["WSne+givory", "xa1g1p", "ya2f1g2"],    # 设置标注按照转换后的值等间隔出现(p)
    x=xline,
    y=yline,
    pen="1p,blue,-",
)
# 不显示超出范围的点
fig.plot(x=xpoints, y=ypoints, style="t0.3c", color="purple", no_clip=False, pen="black")
fig.show()

#%%
# **-JP:** 极坐标线性投影
# ----------------------------

fig = pygmt.Figure()

# 配置参数
pygmt.config(FORMAT_GEO_MAP="+D")
pygmt.config(FONT_TITLE="14p,1,red")

# 移动原点。绘制第一张图
fig.shift_origin(yshift="10c")
# 绘制极坐标数据，默认为 角度 和 半径，默认情况下，角度是指相当于东方向逆时针旋转的角度
fig.basemap(region="0/360/0/1", projection="P5c", frame=['+t"-JP5c -R0/360/0/1"', "xa45f"])

fig.shift_origin(xshift="8c")
# 加上 +a 则表明输入数据是相对于北方向顺时针旋转的角度（地理学中的方位角）
fig.basemap(region="0/360/0/1", projection="P5c+a", frame=['+t"-JP5c+a -R0/90/0/1"', "xa45f", "ya0.2"])

fig.shift_origin(xshift="8c")
fig.basemap(region="0/90/0/1", projection="P5c+a", frame=['WNe+t"-JP5c+a -R0/90/0/1"', "xa45f", "ya0.2"])

fig.shift_origin(xshift="-16c", yshift="-6.5c")
# +t 设置东方向对应的角度，相当于对整个坐标轴做顺时针旋转；若使用了 +a 选项，则设置北方向对应的角度，相当于将整个坐标轴逆时针旋转。
fig.basemap(region="0/90/0/1", projection="P5c+a+t45", frame=['WNse+t"-JP5c+a+t45 -R0/90/0/1"', "xa45f", "ya0.2"])

fig.shift_origin(xshift="8c", yshift="1c")
fig.basemap(region="0/90/3480/6371", projection="P5c+a+t45", frame=['WNse+t"-JP5c+a+t45 -R0/90/3480/6371"', "xa45f", "ya"])

fig.shift_origin(xshift="8c")
# +z 表示将 r 轴标记为深度而不是半径
fig.basemap(region="0/90/3480/6371", projection="P5c+a+t45+z", frame=['WNse+t"-JP5c+a+t45+z -R0/90/3480/6371"', "xa45f", "ya"])

fig.show()

#%%
# **-JE:** 方位等距投影
# -------------------------
# 方位投影最显著的特征是在图上测量的从中心到任意一点的距离是真实的。
# 因而，地图上以投影中心为圆心的圆在真实地球上与投影中心是等距离的。
# 同时，从中心出发的任意方向也是真实的。
#
# 该投影常用于展示多个地理位置与指定点的距离图。

fig = pygmt.Figure()
fig.coast(projection="E-100/40/15c", region="g", frame="g", land="gray")
fig.show()

#%%
# **-JG:** 正交投影
# ---------------------
# 正交方位投影是一种从无穷远距离处的透视投影，因而常用于绘制从外太空看地球。
# 与 Lambert 等面积投影以及立体投影类似，一次只能看到一个半球。
# 
# 该投影既不是等面积也不是保角，在半球边界处有较大得畸变。从投影中心出发的任意方向是真实的。

fig = pygmt.Figure()
fig.coast(projection="G10/52/12c", region="g", frame="g", land="gray")
fig.show()

#%%
# 加上更多的参数时还可以用于绘制透视投影，以在二维平面内模拟从太空看三维的地球。

fig = pygmt.Figure()
fig.coast(
    projection="G4/52/250/30/45/0/60/60/12c",
    region="g",
    frame=["x10g10", "y5g5"],
    land="gray",
)
fig.show()

#%%
# **-JS:** 立体等角投影
# -------------------------
# 此投影是保角方位投影，主要用于绘制南北极区域。在两极，所有经线都是直线，纬线则是圆弧。

fig = pygmt.Figure()
fig.coast(region=[4, 14, 52, 57], projection="S0/90/12c", frame="ag", land="gray")
fig.show()

#%%
# **-JF:** 球心方位投影
# -------------------------
# 此投影是一个从中心投影到与表面相切的一个平面的透视投影。
# 此投影既不等面积也不保角，且在半球的边界处有很大畸变。
# 事实上，对于指定的中心而言，只能绘制不超过半球的区域。
# 但从投影中心出发的方向是真实的。大圆弧会被投影成直线。

fig = pygmt.Figure()
fig.coast(projection="F-90/15/12c", region="g", frame="20g20", land="gray")
fig.show()

#%%
# **-JA:** 球心方位投影
# -------------------------
# 通常用于绘制大区域地图（例如整个大洲或半球），该投影是方位等面积投影。
# 在投影的中心畸变为 0，离投影中心越远畸变越大。

fig = pygmt.Figure()
fig.coast(region="g", frame="afg", land="gray", projection="A30/-20/60/12c")
fig.show()

#%%
# **-JB:** Albers 圆锥等面积投影
# ------------------------------------
# 此投影是圆锥、等面积投影。纬线是不等间隔分布的同心圆，在地球南北极处分布较密。
# 经线则是等间隔分隔，并垂直切割纬线。在两条标准纬线处，比例尺和形状的畸变最小；
# 在两者之间，沿着纬线的比例尺偏小；在两者外部，沿着经线的比例尺则偏大。
# 沿着经线，则完全相反。
# 
# 主要用于绘制东西方向范围很大的地图，尤其是美国地图。

fig = pygmt.Figure()
# Use the ISO country code for Brazil and add a padding of 2 degrees (+R2)
fig.coast(
    projection="B-55/-15/-25/0/12c", region="BR+R2", frame="afg", land="gray", borders=1
)
fig.show()

#%%
# **-JD:** 等距圆锥投影
# -------------------------
# 此投影既不是保角也不是等面积，而是两种的折衷。
# 在所有经线以及标准纬线上比例尺没有畸变。
# 
# 等距圆锥投影常用于绘制小国家的地图集。

fig = pygmt.Figure()
fig.coast(
    shorelines="1/0.5p",
    region=[-88, -70, 18, 24],
    projection="D-79/21/19/23/12c",
    land="lightgreen",
    water="lightblue",
    frame="afg",
)
fig.show()

#%%
# **-JL:** Lambert 圆锥保角投影
# -------------------------------
# 主要用于绘制东西方向范围很大的地图。与 Albers 投影不同的是，
# Lambert 投影不是等面积的。纬线是共圆心的圆弧，经线是这些圆
# 的等间隔分布的半径。与 Albers 投影类似，只有两条标准纬线是无畸变的。
# 投影中心的选取并不影响投影，但其指定了哪一条经线垂直于地图。
#
# Lambert 保角投影场用于绘制美国地图，两个固定的标准纬线是 33°N 和 45°N。

fig = pygmt.Figure()
fig.coast(
    shorelines="1/0.5p",
    region=[-130, -70, 24, 52],
    projection="L-100/35/33/45/12c",
    land="gray",
    borders=["1/thick,black", "2/thin,black"],
    frame="afg",
)

fig.show()

#%%
# **-JPoly:** 多圆锥投影
# -------------------------------
# 此投影既不是等面积也不是保角投影，沿着中心经线处畸变为0。
# 所有纬线的比例尺都是真实的，但其余经线则存在畸变。

fig = pygmt.Figure()
fig.coast(
    shorelines="1/0.5p",
    region=[-180, -20, 0, 90],
    projection="Poly/12c",
    land="gray",
    borders="1/thick,black",
    frame="afg10",
)

fig.show()

#%%
# **-JC:** Cassini 圆柱投影
# -------------------------------
# 此投影既不保角也不等面积，而是介于二者之间的一种投影方式。
# 沿着中心经线的畸变最小，适合绘制南北方向区域范围较大的地图。
# 其中，中心经线、距离中心经线90度的两条经线以及赤道是直线，其余经线和纬线都是复杂的曲线。

fig = pygmt.Figure()
# Use the ISO code for Madagascar (MG) and pad it by 2 degrees (+R2)
fig.coast(projection="C47/-19/12c", region="MG+R2", frame="afg", land="gray", borders=1)
fig.show()

#%%
# **-JY:** 圆柱等面积投影
# -------------------------------
# 选择不同的标准纬线，则对应不同的圆柱投影。
# 所有的这些圆柱投影都是等面积且不保角的。
# 所有经线和纬线都是直线。在高纬度处畸变很大。

fig = pygmt.Figure()
# Use region "d" to specify global region (-180/180/-90/90)
fig.coast(
    region="d",
    projection="Y35/30/12c",
    water="dodgerblue",
    shorelines="thinnest",
    frame="afg",
)
fig.show()

#%%
# **-JQ:** 圆柱等距投影
# -------------------------------
# 这个简单的圆柱投影是一个经度和纬度的线性缩放。
# 最常用的形式是 Plate Carrée 投影，
# 其中对经线和纬线的缩放比例是相同的。所有的经纬线都是直线。

fig = pygmt.Figure()
# Use region "d" to specify global region (-180/180/-90/90)
fig.coast(
    region="d",
    projection="Q12c",
    land="tan4",
    water="lightcyan",
    frame="afg",
)
fig.show()

#%%
# **-JM:** Mercator 投影
# -------------------------------
# 此投影是各种地图投影中最著名的一个，是圆柱保角投影，沿着赤道无畸变，但两极畸变严重。
# 此投影的主要特点是等方位角的线是一条直线，在常规 Mercator 投影中，
# 圆柱与赤道相切。若圆柱沿着其他方向与地球相切，则称为横向 Mercator 投影或倾斜 Mercator 投影。

fig = pygmt.Figure()
fig.coast(region=[0, 360, -80, 80], frame="afg", land="red", projection="M0/0/12c")
fig.show()

#%%
# **-JJ:** Miller 圆柱投影
# -------------------------------
# 该投影既不是保角也不是等面积。所有的经线和纬线都是直线。
# 该投影是 Mercator 与其他圆柱投影之间的折衷。
# 在此投影中，纬线之间的间距使用了 Mercator 公式并乘以 0.8 倍的真实纬度，
# 因而避免了极点的奇点，然后再将结果除以 0.8。

fig = pygmt.Figure()
fig.coast(
    region=[-180, 180, -80, 80],
    projection="J-65/12c",
    land="khaki",
    water="azure",
    shorelines="thinnest",
    frame="afg",
)
fig.show()

#%%
# **-JCyl_stere:** 圆柱立体投影
# -------------------------------
# 圆柱立体投影不像其它的圆柱投影那样令人关注，但由于其相对简单且能够克服其它
# 圆柱投影的缺点（比如高纬度的畸变），故而仍然被使用。立体投影是透视投影，
# 将整个球沿着赤道上的对跖点投影到一个圆柱上。该圆柱于两条距赤道等间距的标准纬线处穿过球体。

fig = pygmt.Figure()
fig.coast(region="g", frame="afg", land="gray", projection="Cyl_stere/30/-20/12c")
fig.show()

#%%
# **-JT:** 横向 Mercator 投影
# -------------------------------
# 此投影圆柱与某条经线相切。在该经线处无畸变，离中心经线越远畸变越大，
# 距离中心经线 90 度处的经线畸变达到无穷。中心经线和赤道都是直线，
# 其余经线和纬线则是复杂曲线。

fig = pygmt.Figure()
fig.coast(
    region=[20, 50, 30, 45],
    projection="T35/12c",
    land="lightbrown",
    water="seashell",
    shorelines="thinnest",
    frame="afg",
)
fig.show()

#%%
# **-JU:** 通用横向 Mercator(UTM) 投影
# --------------------------------------
# 通用横向 Mercator（UTM）投影是横向 Mercator 投影的一个特殊子集。
# 此处，全球在南北纬 84 度之间被划分为 60 个区域，大多数区域的宽度都是 6 度。
# 每一个区域都有各自位移的中心经线。进一步，每个区域都被划分为纬度带。

fig = pygmt.Figure()
# UTM Zone is set to 52R
fig.coast(
    region=[127.5, 128.5, 26, 27],
    projection="U52R/12c",
    land="lightgreen",
    water="lightblue",
    shorelines="thinnest",
    frame="afg",
)
fig.show()

#%%
# **-JK:** Eckert 投影
# --------------------------------------
# Eckert IV 和 VI 投影是伪圆柱等面积投影。中心经线以及所有的纬线都是直线，
# 其余经线是等间隔分布的椭圆弧（IV）或正弦曲线（VI）。
# 比例尺在纬线 40°30’（IV）和 49°16’（VI）是真实的。
# **-JKf**\ （f 代表 four）表示使用 Eckert IV 投影，**-JKs**\ （s 代表 six）表示使用 Eckert VI 投影。
# 若不指定 f 或 s，则默认使用 Eckert VI 投影。

fig = pygmt.Figure()
# Use region "d" to specify global region (-180/180/-90/90)
fig.coast(region="d", projection="Kf12c", land="ivory", water="bisque4", frame="afg")
fig.show()

fig = pygmt.Figure()
# Use region "d" to specify global region (-180/180/-90/90)
fig.coast(region="d", projection="Ks12c", land="ivory", water="bisque4", frame="afg")
fig.show()

#%%
# **-JH:** 等面积 Hammer 投影
# --------------------------------------
# 投影后的边界是一个椭圆，赤道和中心经线是直线，其余纬线和经线都是复杂曲线。

fig = pygmt.Figure()
# Use region "d" to specify global region (-180/180/-90/90)
fig.coast(region="d", projection="H12c", land="black", water="cornsilk", frame="afg")
fig.show()

#%%
# **-JW:** Mollweide 投影
# --------------------------------------
# 纬线是不等间隔分布的直线，经线是等间隔分布的椭圆弧。
# 比例尺仅在南北纬 40 度 44 分纬线上才是真实的。
# 
# 此投影主要用于绘制全球的数据分布图。

fig = pygmt.Figure()
# Use region "d" to specify global region (-180/180/-90/90)
fig.coast(region="d", projection="W12c", land="tomato1", water="skyblue", frame="ag")
fig.show()

#%%
# **-JN:** Robinson 投影
# ------------------------------
# 此投影既不是保角也不是等面积。中心经线以及所有纬线都是直线，
# 其余经线都是曲线。其使用查找表的方式而不是解析表达式来使得
# 全球看上去比较正常。比例尺在经线 38° 是真实的。

fig = pygmt.Figure()
# Use region "d" to specify global region (-180/180/-90/90)
fig.coast(region="d", projection="N12c", land="goldenrod", water="snow2", frame="afg")
fig.show()

#%%
# **-JI:** 正弦曲线投影
# ------------------------------
# 正弦曲线投影是等面积投影，是已知的最古老的投影之一，也被称为等面积 Mercator 投影。
# 其中心经线是直线，其余经线是正弦曲线，纬线是等间距的直线。在所有纬线和中心经线处比例尺是真实的。

fig = pygmt.Figure()
# Use region "d" to specify global region (-180/180/-90/90)
fig.coast(region="d", projection="I12c", land="coral4", water="azure3", frame="afg")
fig.show()

#%%
# 为了减少形状的畸变，引入了间断正弦曲线投影，即用三个对称的段来覆盖全球。
# 传统上，间断出现在 160°W、20°W 和 60°E 处，一般仅用于显示全球不连续数据分布。

fig = pygmt.Figure()
fig.coast(region="200/340/-90/90", projection="i0.04c", land="darkred", 
            water="azure", frame="g", area_thresh="10000", resolution="c")

fig.shift_origin(xshift="5.6c")
fig.coast(region="-20/60/-90/90", land="darkgreen", water="azure", frame="g", 
            area_thresh="10000", resolution="c")

fig.shift_origin(xshift="3.2c")
fig.coast(region="60/200/-90/90", land="darkblue", frame="g", area_thresh="10000", 
            resolution="c")

fig.show()

#%%
# **-JV:** Van der Grinten 投影
# ------------------------------
# 此投影既不等面积也不保角。中心经线和赤道都是直线，其余经线则是圆弧，
# 仅在赤道处比例尺是真实的，主要用于在一个圆内展示整个世界地图。

fig = pygmt.Figure()
# Use region "d" to specify global region (-180/180/-90/90)
fig.coast(region="d", projection="V12c", land="gray", water="cornsilk", frame="afg")
fig.show()

#%%
# **-JR:** Winkel Tripel 投影
# ------------------------------
# 该投影在三个元素（面积、角度、距离）之间折衷，在绘制全球地图时，这三个元素的畸变最小。
# 此投影不是保角也不是等面积投影。中心经线和赤道是直线，其他经线和纬线是曲线。
# 该投影取等距圆柱投影和 Aitoff 投影的坐标的平均值。极点处投影为 0.4 倍赤道长度的直线。

fig = pygmt.Figure()
# Use region "d" to specify global region (-180/180/-90/90)
fig.coast(region="d", projection="R12c", land="burlywood4", water="wheat1", frame="afg")
fig.show()