hypoDD
============

:软件来源: https://www.ldeo.columbia.edu/~felixw/hypoDD.html
:适用平台: Linux
:推荐阅读: `D Yao's Teaching <http://geophysics.eas.gatech.edu/people/dyao/teaching.html>`__
:更新日期: 2021-01-27

------------------------

基于给定的一维速度模型利用双差算法计算震源相对位置的程序。

.. note::

    A new version 2.0b is available, which includes 3D models/ray tracing,
    station elevation, and an improved weighting scheme.
    If you would like to use/test this beta version, 
    please email felixw@ldeo.columbia.edu.

安装
--------

.. code-block:: bash

    # 下载 hypoDD 程序
    $ wget http://www.ldeo.columbia.edu/~felixw/HYPODD/HYPODD_1.3.tar.gz

    # 编译
    $ cd src
    $ make clean && make
    $ cp hypoDD/hypoDD ~/bin
    $ cp ph2dt/ph2dt ~/bin

    # 下载示例数据
    $ wget http://www.ldeo.columbia.edu/~felixw/HYPODD/HYPODD_1.3_Examples.tar.gz
    $ wget http://www.ldeo.columbia.edu/~felixw/HYPODD/HYPODD_moreExamples.tar.gz
    $ wget http://geophysics.eas.gatech.edu/people/dyao/Files/WFCC_HYPODD.tar