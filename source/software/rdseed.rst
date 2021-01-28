reseed
============

:软件来源: http://ds.iris.edu/pub/programs/
:适用平台: Linux、macOS
:推荐阅读: `rdseed 的安装 <https://blog.seisman.info/rdseed-install/>`__
:更新日期: 2021-01-27

------------------------

rdseed 用于将 SEED 格式的数据转换为 SAC 格式。

`官方消息 <http://ds.iris.edu/ds/nodes/dmc/manuals/rdseed/>`__\ 
今后不再更新和维护 rdseed 。

安装
--------

目前源码在 GitHub 上公开。

.. code-block:: bash

    $ git clone git@github.com:iris-edu-legacy/rdseed.git
    $ cd rdseed && make
    $ mv rdseed ~/bin

经测试，用 GitHub 上下载的 rdseed 可能无法正确
解压缩波形文件，继续采用老的二进制包。

.. code-block:: bash

    $ wget http://ds.iris.edu/pub/programs/rdseedv5.3.1.tar.gz
    $ tar -xvf rdseedv5.3.1.tar.gz
    $ cd rdseedv5.3.1/
    $ mv rdseed.rh6.linux_64 ~/bin/rdseed