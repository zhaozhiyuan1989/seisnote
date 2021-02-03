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

本项目需要安装 :doc:`rdseed`\ 、:doc:`SAC <sac>`\ 、:doc:`GMT4 <gmt4>`\ 、:doc:`taup`\ 、fk、gcap、pssac。

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

常见问题
-----------------

- ``Warning: flag=21 => the minimum 0.0/57.8/ 6.4 is at boundary``

  可能某个台站位于节面上，特点是 P 波非常的弱，在权重文件中去除这个台站就可以。
  当然，也可以选择忽略这个警告，对结果没有太大影响。

- ``... no minimum found ...``

  首先查看格林函数有没有正确生成。
  然后利用 :doc:`sac` 查看波形有无问题，有的台站可能预处理后波形“消失”了，
  在权重文件中删除这个台站即可。利用 RESP 去除仪器响应波形数据消失的情况下改用 PZ 试试。
  

说明
--------

Cap 研究中需要的频段是 0.05 到 0.2 Hz，f1|f2|f3|f4 可以取为 0.02|0.03|0.5|1，
这个基本是最小的范围，也可以取更大范围，比如 0.01|0.02|20|30，
因为 ``trans`` 是第一次滤波，``cap.pl`` 中 ``-C`` 选项进行了第二次实际滤波，
另外，地震的能量主要部分也不在高频，震级越小，信号越高频，所以小震机制解是难点。

初始速度模型很关键，台站的选取也影响到最后的结果。
可以选取四象限分布较好的震中距范围在 100-300km 范围内的几个信噪比较好的台站进行反演，
因为震中距太大波形不清晰，震中距太小面波没到。

反演结果中 ISO、CLVD 代表非构造地震的成分，默认不反演，可以在 ``event.conf`` 中
用 ``-J: 0/0.1/0/0.1`` 控制。 深度反演结果中横坐标为深度，纵坐标为误差，``h`` 
后的两个数为拟合结果最好的深度以及深度估计范围。
  