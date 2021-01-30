"""
底图边框
========================

底图的边框、标签、刻度等样式均由 :class:`pygmt.Figure` 类的 ``frame`` 选项
控制。

"""

import pygmt

########################################################################################
# 绘制底图
# ----------
#
# 默认情况下，PyGMT 不会在绘图时自动添加边框。
# 例如，使用墨卡托投影来绘制世界海岸线时：

fig = pygmt.Figure()
fig.coast(shorelines="1/0.5p", region=[-180, 180, -60, 60], projection="M25c")
fig.show()

########################################################################################
# 可以通过 :meth:`pygmt.Figure.basemap` 方法的 ``frame="f"`` 选项添加默认边框：

fig = pygmt.Figure()
fig.coast(shorelines="1/0.5p", region=[-180, 180, -60, 60], projection="M25c")
fig.basemap(frame="f")
fig.show()

########################################################################################
# 刻度线和网格线
# --------------------
#
# 添加 ``frame=True`` 或者 ``frame="a"`` 选项后 PyGMT 会根据绘图区范围
# 自动确定刻度线标注方式：

fig = pygmt.Figure()
fig.coast(shorelines="1/0.5p", region=[-180, 180, -60, 60], projection="M25c")
fig.basemap(frame="a")
fig.show()

########################################################################################
# 修改 ``frame="ag"`` 后可自动添加网格线:

fig = pygmt.Figure()
fig.coast(shorelines="1/0.5p", region=[-180, 180, -60, 60], projection="M25c")
fig.basemap(frame="ag")
fig.show()

########################################################################################
# 标题
# -----
#
# 可以通过把 **+t**\ *title* 传递给 ``frame`` 选项来
# 设置图片标题。如下所示，可以使用列表将多个参数同时传递给 ``frame`` 选项：

fig = pygmt.Figure()
# region="IS" specifies Iceland using the ISO country code
fig.coast(shorelines="1/0.5p", region="IS", projection="M25c")
fig.basemap(frame=["a", "+tIceland"])
fig.show()

########################################################################################
# 当标题内容存在空格时，可以采用单、双引号相结合的方式传递参数，如下所示：

fig = pygmt.Figure()
# region="TT" specifies Trinidad and Tobago
fig.coast(shorelines="1/0.5p", region="TT", projection="M25c")
fig.basemap(frame=["a", '+t"Trinidad and Tobago"'])
fig.show()

########################################################################################
# 轴标签
# -----------
#
# 坐标轴的 **X** 轴标签由 **x+l**\ *label* 控制，**Y** 轴标签由 **y+l**\ *label* 控制。
# 如果轴名称大写，则同时绘制该轴的刻度线和标签，反之，当轴名称小写时，仅绘制轴和刻度线。
#
# **GMT 不能为地理投影设置轴标签！**

fig = pygmt.Figure()
fig.basemap(
    region=[0, 10, 0, 20],
    projection="X10c/8c",
    frame=["WSne", "xa+lx-axis", "yf+ly-axis"],
)
fig.show()