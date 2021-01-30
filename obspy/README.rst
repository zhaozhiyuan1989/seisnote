ObsPy
================

ObsPy 是一款针对地震领域开发的 Python 库，功能十分齐全。

本文主要记录 ObsPy 的一些常用功能和用法，
目标为熟悉 ObsPy 的设计哲学和掌握基本的数据处理流程。

安装
--------

官方建议利用 `Anaconda <https://github.com/obspy/obspy/wiki#installation>`__ 
安装 ObsPy，国内用户可能需要更换镜像源。

.. code-block:: bash

    # 创建 obspy 运行环境
    $ conda create -n obspy python=3.8

    # 查看所有环境名称
    $ conda info -e

    # 激活 obspy 环境
    $ conda activate obspy

    # 安装 obspy 预编译包 
    (obspy) $ conda install obspy -c conda-forge
    (obspy) $ conda update obspy
    # 查看 obspy 版本
    (obspy) $ python -c "import obspy; print(obspy.__version__)"
        1.2.2

    # 安装地图绘制包
    (obspy) $ conda install cartopy

    # 测试 obspy 
    $ obspy-plot -h    # Simple script to plot waveforms in one or more files.
    $ obspy-mopad -h    # Just like MoPad.

学习资源
-----------

- `ObsPy 官方文档 <https://docs.obspy.org>`__
- `Using Syngine with ObsPy <https://nbviewer.jupyter.org/gist/krischer/3e655576e4d17e6c95f2>`__
- `ROSES: Unit 1 ObsPy <https://www.bilibili.com/video/BV1St4y1v7uk>`__
- :download:`ObsPy Tutorial in Chinese <https://docs.obspy.org/archive/ObsPy_Tutorial_2020-04_chinese.pdf>`

主要内容
----------