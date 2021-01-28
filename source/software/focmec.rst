FOCMEC
============

:软件来源: http://ds.iris.edu/pub/programs/focmec/
:适用平台: Linux
:推荐阅读: 暂无
:更新日期: 2021-01-27

------------------------

FOCMEC 程序包利用 P、SV、SH 极性或 SV/P、SH/P、SV/SH 振幅比计算震源机制解，
包含 ``dsretc`` 等多个实用的二进制程序。

安装
--------

.. code-block:: bash

    $ wget http://ds.iris.edu/pub/programs/focmec/focmec.tgz
    $ tar -xvf focmec.tgz
    $ cd focmec/src

    # 需要 csh 运行
    $ ./build_package
    $ cd ../..
    $ mv focmec ~/opt
    $ echo "export PATH=/home/zhao/opt/focmec/bin:${PATH}" >> ~/.bashrc
    $ source ~/.bashrc
    $ dsretc
