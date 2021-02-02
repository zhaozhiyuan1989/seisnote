"""
绘制 3D 曲面
==============

利用 :meth:`pygmt.Figure.grdview` 绘制 3D 曲面。

"""

#%%
# 首先利用 :func:`pygmt.datasets.load_earth_relief` 从 GMT 服务器读取地形数据： 

import pygmt
grid = pygmt.datasets.load_earth_relief(resolution="05m", region=[-108, -103, 35, 40])

#%%
# 利用  :meth:`pygmt.Figure.grdview` 读取网格文件后绘制 3D 曲面，
# ``perspective`` 选项控制了视角，``zsize`` 控制了 3D 图在 Z 方向上的高度：

# sphinx_gallery_thumbnail_number = 3
fig = pygmt.Figure()
fig.grdview(
    grid=grid,
    # 视角方位 130°，高度 30°
    perspective=[130, 30],
    # 设置边框显示方式
    frame=["xa", "ya", "WSnE"],
    # S设置投影方式
    projection="M15c",
    # 设置 Z 方向高度
    zsize="1.5c",
)
fig.show()

#%% 

fig = pygmt.Figure()
fig.grdview(
    grid=grid,
    perspective=[130, 30],
    frame=["xa", "ya", "WSnE"],
    projection="M15c",
    zsize="1.5c",
    # 设置 surftype 为 "surface" 进行平滑
    surftype="s",
)
fig.show()

#%%

fig = pygmt.Figure()
fig.grdview(
    grid=grid,
    perspective=[-130, 30],  # 设置 3D 视角
    frame=["xaf", "yaf", "WSnE"],
    projection="M15c",
    zsize="1.5c",
    surftype="s",
    cmap="geo",  # 设置 CPT
    plane="1000+ggrey",  # 设置平面高度 1000m，地表下填充灰色
    contourpen="0.1p",  # 设置等高线样式
)
fig.colorbar(perspective=True, frame=["a500", "x+lElevation", "y+lm"])  # 设置 perspective 选项让 colorbar 与图片角度一致
fig.show()

#%%

import numpy as np
import pygmt
import xarray as xr


# 定义一个有趣的函数
# https://en.wikipedia.org/wiki/Ackley_function
def ackley(x, y):
    return (
        -20 * np.exp(-0.2 * np.sqrt(0.5 * (x ** 2 + y ** 2)))
        - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y)))
        + np.exp(1)
        + 20
    )


# 创建网格数据
INC = 0.05
x = np.arange(-5, 5 + INC, INC)
y = np.arange(-5, 5 + INC, INC)
data = xr.DataArray(ackley(*np.meshgrid(x, y)), coords=(x, y))

fig = pygmt.Figure()

# 绘制 3D 曲面
SCALE = 0.5  
fig.grdview(
    data,
    frame=["a5f1", "za5f1"],
    projection=f"x{SCALE}c",
    zscale=f"{SCALE}c",
    surftype="s",
    cmap="roma",
    perspective=[135, 30],  
    shading="+a45",
)

fig.show()