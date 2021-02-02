"""
添加文字
============

利用 PyGMT 的 :meth:`pygmt.Figure.text` 可以添加文字。

.. note::

    可结合《:doc:`gmtdoc:tutorial/texts`》
    和《:doc:`gmtdoc:module/text` 模块》学习。

"""

#%%
# 最简单的示例
# ---------------
#
# 若需要添加文字，则必须给出文字的 X 和 Y 坐标以及具体的文字，
# 分别赋予 ``x``、``y`` 以及 ``text`` 选项。

import pygmt

# sphinx_gallery_thumbnail_number = 5
fig = pygmt.Figure()
with pygmt.config(MAP_FRAME_TYPE="plain"):
    fig.basemap(region=[108, 120, -5, 8], projection="M20c", frame="a")
fig.coast(land="black", water="skyblue")

# 绘制单个文字
fig.text(text="SOUTH CHINA SEA", x=112, y=6)

# 绘制多个文字需要写成列表形式
fig.text(text=["CELEBES SEA", "JAVA SEA"], x=[119, 112], y=[3.25, -4.6])

fig.show()

#%%
# 改变字体样式
# ---------------

fig = pygmt.Figure()
with pygmt.config(MAP_FRAME_TYPE="plain"):
    fig.basemap(region=[108, 120, -5, 8], projection="M20c", frame="a")
fig.coast(land="black", water="skyblue")

# 利用 font 选项改变字体样式
fig.text(text="BORNEO", x=114.0, y=0.5, font="22p,Helvetica-Bold,white")

fig.show()

#%%
# 改变对齐方式
# ---------------

fig = pygmt.Figure()
fig.basemap(region=[0, 3, 0, 3], projection="X10c", frame=["WSne", "af0.5g"])
for position in ("TL", "TC", "TR", "ML", "MC", "MR", "BL", "BC", "BR"):
    fig.text(
        text=position,
        position=position,
        font="28p,Helvetica-Bold,black",
        justify=position,
    )
fig.show()

#%%
# 改变旋转角度
# ---------------

fig = pygmt.Figure()
# sphinx_gallery_thumbnail_number = 6
fig.basemap(region=[0, 4, 0, 4], projection="X5c", frame="WSen")
for i in range(0, 360, 30):
    fig.text(text=f"`          {i}@.", x=2, y=2, justify="LM", angle=i)
fig.show()

#%%
# 改变文字填充颜色
# -----------------

fig = pygmt.Figure()
fig.basemap(region=[0, 1, 0, 1], projection="X5c", frame="WSen")
fig.text(text="Green", x=0.5, y=0.5, fill="green")
fig.show()

#%%
# 示例：从本地读取文本
# --------------------

fig = pygmt.Figure()
with pygmt.config(MAP_FRAME_TYPE="plain"):
    fig.basemap(region=[108, 120, -5, 8], projection="M20c", frame="a")
fig.coast(land="black", water="skyblue")

# 构建输入文本
with open("examples.txt", "w") as f:
    f.write("114 0.5 0 22p,Helvetica-Bold,white CM BORNEO\n")
    f.write("119 3.25 0 12p,Helvetica-Bold,black CM CELEBES SEA\n")
    f.write("112 -4.6 0 12p,Helvetica-Bold,black CM JAVA SEA\n")
    f.write("112 6 40 12p,Helvetica-Bold,black CM SOUTH CHINA SEA\n")
    f.write("119.12 7.25 -40 12p,Helvetica-Bold,black CM SULU SEA\n")
    f.write("118.4 -1 65 12p,Helvetica-Bold,black CM MAKASSAR STRAIT\n")

# 前两列为文字添加位置，紧跟的三列分别是“旋转角度/字体/对齐方式”，
# 最后一列是文字内容，顺序不能变！
# 设置 angle/font/justify 为 true 表示文本中有这些列
fig.text(textfiles="examples.txt", angle=True, font=True, justify=True)
fig.show()

# 删除临时文件
import os
os.remove("examples.txt")


