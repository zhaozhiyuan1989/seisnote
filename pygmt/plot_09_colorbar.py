"""
添加 colorbar
==============

为 :meth:`pygmt.Figure.colorbar` 的 ``cmap`` 选项指定颜色表后，
就可以为图片添加 colorbar。

colorbar 在图中的位置由 ``position`` 选项控制，``position`` 选项支持的输入格式包括：

- **j/J**：后跟由水平对齐方式（**T**\ op，**M**\ iddle，**B**\ ottom）和垂直对齐方式
  （**L**\ eft，**C**\ enter，**R**\ ight)组成的两个字符，如 ``position="jTR"`` 表示
  右上角为参考点

- **g**：指定某地图坐标为参考点，比如 ``position="g170/-45"`` 表示（170E，45S）为参考点

- **x**：在绘图坐标系下指定参考点，比如 ``position="x5c/7c"`` 表示距离锚点（5cm，7cm）的点为参考点

- **n**：在归一化坐标系中指定参考点，比如 ``position="n0.4/0.8"``

需要注意的是，默认的锚点为 **BL**，添加 **+h** 到 ``position`` 选项可将 colorbar
由垂直变为水平。

.. note::

    可结合《:doc:`gmtdoc:module/colorbar` 模块》学习。

"""

import pygmt

fig = pygmt.Figure()
fig.basemap(region=[0, 3, 6, 9], projection="x3c", frame=["af", 'WSne+t"Colorbars"'])

# 利用 roma 颜色表创建 colorbar
# 如果没有给定 position 参数，默认放在 BC 位置 
fig.colorbar(cmap="roma", frame=["x+lVelocity", "y+lm/s"])

# 利用 batlow 颜色表创建 colorbar
fig.colorbar(
    cmap="batlow",
    # 指定地图坐标 0.3/8.7 为参考点,
    # colorbar 长宽分别为 4cm 和 0.5cm，水平摆放(+h)
    position="g0.3/8.7+w4c/0.5c+h",
    box=True,
    frame=["x+lTemperature", r"y+l\260C"],
    scale=100,
)


fig.colorbar(
    cmap="oleron",
    # 地图的右中边框外为参考点（JMR），距离锚点水平距离为 1cm（+o1c/0c）
    # colorbar 长 7cm 宽 0.5cm，绘制 NaN 颜色块（+n）
    position="JMR+o1c/0c+w7c/0.5c+n+mc",
    # colorbar 水平标注垂直摆放，并且绘制在轴的另一侧
    frame=["x+lElevation", "y+lm"],
    scale=10,
)

fig.show()