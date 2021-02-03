"""
绘制三维散点图
==============

利用 :meth:`pygmt.Figure.plot3d` 绘制三维散点图。

"""

import pandas as pd
import pygmt

#从 iris 服务器读取数据 
df = pd.read_csv("https://github.com/mwaskom/seaborn-data/raw/master/iris.csv")

# 将 species 列数据格式转为 category
df["species"] = df.species.astype(dtype="category")

# 利用 pygmt.info 读取绘图区域 (xmin, xmax, ymin, ymax, zmin, zmax)
region = pygmt.info(
    table=df[["petal_width", "sepal_length", "petal_length"]],  # x, y, z c
    per_column=True,  # 输出为 numpy array 格式
    spacing="1/2/0.5",  # x y z 间距分别为 1, 2 和 0.5
)

# 绘制三维散点图 
fig = pygmt.Figure()
pygmt.makecpt(cmap="cubhelix", color_model="+c", series=(0, 3, 1))

# 用不同颜色绘制三个不同种类数据
fig.plot3d(
    x=df.petal_width,
    y=df.sepal_length,
    z=df.petal_length,
    sizes=0.1 * df.sepal_width,  # 指定符号大小
    color=df.species.cat.codes.astype(int),  # P指定颜色
    cmap=True,  # 使用 makecpt 制作的颜色表
    region=region,  # (xmin, xmax, ymin, ymax, zmin, zmax)
    frame=[
        "WsNeZ3",  # z 轴标注
        'xafg+l"Petal Width"',
        'yafg+l"Sepal Length"',
        'zafg+l"Petal Length"',
    ],
    style="uc",  # 符号种类大小
    perspective=[315, 25],  # 视角
    zscale=1.5,  # Z 轴高度
)
fig.show()