OH MY CAP
============

:软件来源: https://github.com/wangliang1989/oh-my-cap
:适用平台: Linux、macOS
:推荐阅读: `oh My CAP <https://seismology.xyz/oh-my-cap/>`__
:更新日期: 2021-01-27

------------------------

CAP 是计算震源机制的一种常用方法。

王亮博士基于 gCAP1.0 建立了 Oh My CAP 开源项目。

.. warning::

    经测试，在 Ubuntu 下需要从源码编译 SAC，否则 fk 和 gcap 可能
    会出现类似 ``recompile with -fPIE`` 的编译报错。

安装
--------

请参考项目主页。

本项目需要安装 :doc:`rdseed`\ 、:doc:`SAC <sac>`\ 、:doc:`GMT4 <gmt>`\ 、:doc:`taup`\ 、fk、gcap、pssac。

.. code-block:: bash

    $ cd fk && make
    $ cd ../gcap && make
    $ cd ../pssac && make 

    $ cpan
    cpan[1]> install Parallel::ForkManager

    $ # 进入 Glib 目录，生成格林函数
    $ cd Glib
    $ perl run_fk.pl model.fk

    # 进入 example 目录
    $ cd ../example/

    # 对示例数据进行预处理
    $ perl process.pl 20080418093658
    # 警告 WARNING potential for aliasing. new delta: 0.200000 data delta: 0.025000 可忽略

    # 生成权重文件
    $ perl weight.pl 20080418093658

    # 反演并查看反演结果
    $ perl inversion.pl 20080418093658
    # 路径 20080418093658 下面的 model_*.pdf为各个深度的结果和波形拟合图

    # 绘制并查看深度反演结果
    $ perl get_depth.pl 20080418093658