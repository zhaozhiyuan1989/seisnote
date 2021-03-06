PyGMT
================

.. warning:: 

    PyGMT 仍处于开发阶段，可能存在版本兼容问题，请谨慎使用。

PyGMT 为 GMT 提供了 Python 接口，是一个适用于处理地理空间
和地球物理数据并制作精美图形的模块。

由于 PyGMT 还在不断更新，如果某些 GMT 的绘图选项在 PyGMT 中
还无法实现时，可以利用 :class:`pygmt.clib.Session` 在 PyGMT
中调用 GMT 模块绘图，在《:doc:`plot_11_meca`》一节中有示例。

.. note::

    GMT 里的所有单字符选项在 PyGMT 里都可以用，
    比如可以用 ``B="WSen"``，但是 PyGMT 不鼓励这样做。

本文目的在于用简单的示例说明如何在 PyGMT 中添加、修改 GMT 绘图参数，
从而让 GMT 用户可以轻松掌握 PyGMT 的使用。


学习资源
-----------

- :doc:`gmtdoc:index`
- `PyGMT 官方文档 <https://www.pygmt.org/latest/>`__
- `ROSES: Unit 8 PyGMT <https://www.bilibili.com/video/BV1Ak4y1y7d9>`__


安装
---------

官方建议利用 `Anaconda <https://www.pygmt.org/latest/install.html>`__ 
安装 PyGMT，国内用户可能需要更换镜像源。

.. code-block:: bash

    # 添加 conda-forge channel
    $ conda config --prepend channels conda-forge

    # 创建 pygmt 运行环境，python 版本需要大于 3.6
    $ conda create --name pygmt python=3.8 pip numpy pandas xarray netcdf4 packaging gmt ipython

    # 查看所有环境名称
    $ conda info -e

    # 激活 pygmt 环境
    $ conda activate pygmt

    # 安装 pygmt
    (pygmt) $ conda install pygmt
    # 查看 pygmt 版本
    (pygmt) $ python -c "import pygmt; pygmt.show_versions()"

        PyGMT information:
          version: v0.2.1
        System information:
          python: 3.8.5 (default, Sep  4 2020, 07:30:14)  [GCC 7.3.0]
          executable: /home/zhao/anaconda3/envs/pygmt/bin/python
          machine: Linux-4.19.128-microsoft-standard-x86_64-with-glibc2.10
        Dependency information:
          numpy: 1.19.2
          pandas: 1.2.1
          xarray: 0.16.2
          netCDF4: 1.5.5.1
          packaging: 20.8
          ghostscript: 9.53.3
          gmt: 6.1.1
        GMT library information:
          binary dir: /home/zhao/anaconda3/envs/pygmt/bin
          cores: 8
          grid layout: rows
          library path: /home/zhao/anaconda3/envs/pygmt/lib/libgmt.so
          padding: 2
          plugin dir: /home/zhao/anaconda3/envs/pygmt/lib/gmt/plugins
          share dir: /home/zhao/anaconda3/envs/pygmt/share/gmt
          version: 6.1.1

主要内容
-------------