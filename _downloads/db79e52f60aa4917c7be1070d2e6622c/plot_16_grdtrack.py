"""
对网格文件采样
==============

利用 :func:`pygmt.grdtrack` 对网格文件进行采样。

"""

import pygmt

# 从 GMT 服务器加载地形数据
grid = pygmt.datasets.load_earth_relief()
# 从 GMT 服务器加载洋中脊数据 
points = pygmt.datasets.load_ocean_ridge_points()
# 沿轨迹点对洋中脊测深
track = pygmt.grdtrack(points=points, grid=grid, newcolname="bathymetry")

fig = pygmt.Figure()
fig.basemap(region="g", frame=True, projection="Cyl_stere/150/-20/15c")
fig.grdimage(grid=grid, cmap="gray")
fig.coast(land="#666666")

fig.plot(
    x=track.longitude,
    y=track.latitude,
    style="c0.15c",
    cmap="terra",
    color=(track.bathymetry - track.bathymetry.mean()) / track.bathymetry.std(),
)
fig.show()