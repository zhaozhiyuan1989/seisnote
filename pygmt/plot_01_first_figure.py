"""
命令初探
========================

本节简单介绍 PyGMT 的一些基本概念。

.. note:: 
 
   PyGMT 采用 GMT6 的现代模式执行绘图命令，与传统模式相比有了较大改变。
   经典模式和现代模式的区别请参考《\ :doc:`gmtdoc:migrating/classic2modern`\ 》。

"""

#%%
# 首先导入 :mod:`pygmt` 模块：

import pygmt

#%%
# 
# 利用 :class:`pygmt.Figure` 类创建实例：

fig = pygmt.Figure()

#%%
# 使用 :meth:`pygmt.Figure.basemap` 方法来添加元素，
# 给定绘图经纬度范围、投影方式以及边框属性。
# ``region`` 选项可以采用如下列表形式，也可以采用字符串形式 ``1/2/3/4`` ：

fig.basemap(region=[-90, -70, 0, 20], projection="M16c", frame=True)

#%%
# 利用 :meth:`pygmt.Figure.coast` 方法添加海岸线数据，
# 采用与前文相同的参数绘图时可以省略选项：

fig.coast(shorelines=True)

#%%
# 利用 :meth:`pygmt.Figure.show` 方法显示图像：

fig.show()

#%%
# 当然，我们也可以直接通过 :meth:`pygmt.Figure.coast` 方法设置地图区域，投影和框架类型，
# 而无需调用 :meth:`gmt.Figure.basemap` 方法： 

fig = pygmt.Figure()
fig.coast(shorelines=True, region=[-90, -70, 0, 20], projection="M16c", frame=True)
fig.show()

#%%
# 最后可以选择利用 :meth:`pygmt.Figure.savefig` 方法将图片保存到本地，
#
# .. code:: python
#
#     fig.savefig("central-america-shorelines.png")
#
