ObsPy
============

:软件来源: https://github.com/obspy/obspy/wiki/Installation-via-Anaconda
:适用平台: Linux、macOS、Windows
:推荐阅读: `ObsPy 图库 <https://docs.obspy.org/gallery.html>`__
:更新日期: 2021-01-27

------------------------

ObsPy 是一款针对地震领域开发的 Python 库，功能十分齐全。

建议利用 :doc:`anaconda` 安装 ObsPy，国内用户可能需要更换镜像源。

安装
--------

.. code-block:: bash

    $ conda create -n obspy python=3.7 
    $ conda info -e
    $ conda activate obspy 
    (obspy) $ conda install obspy -c conda-forge
    (obspy) $ conda update obspy
    (obspy) $ conda install cartopy

示例
----------

ObsPy 提供了一系列功能强大的模块可以处理几乎所有格式的地震数据，
以下简单介绍几个实用功能，ObsPy 的详细介绍请查看中文手册部分。

obspy.taup
^^^^^^^^^^^^

几乎能实现 :doc:`taup` 软件的所有功能。

.. code-block:: python

    # 修改自 https://docs.obspy.org/gallery.html
    # 原图没有保存，这里演示如何保存图片
    from obspy.taup import TauPyModel
    import matplotlib.pyplot as plt
    import os

    # get the name of this script 
    fname = '.'.join(os.path.basename(__file__).split('.')[0:-1])

    fig, ax = plt.subplots(subplot_kw=dict(polar=True))

    model = TauPyModel(model='iasp91')

    arrivals = model.get_ray_paths(500, 140, phase_list=['Pdiff', 'SS'])

    ax = arrivals.plot_rays(plot_type='spherical', phase_list=['Pdiff', 'SS'], legend=True, ax=ax, fig=fig, show=False)

    plt.savefig(fname+'.png')
    plt.show()

obspy-mopad
^^^^^^^^^^^^^

MoPaD 是由 Python2 编写的地震矩绘制和分析工具，
obspy-mopad 可以实现与 MoPaD 类似的功能。

.. code-block:: bash

    # 需要安装好 ObsPy
    $ conda activate obspy
    $ obspy-mopad -h
    $ obspy-mopad plot 1,2,3,-4,-5,-10 -I -f FSD_xmpl.png
