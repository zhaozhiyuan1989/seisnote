mseed2sac
============

:软件来源: https://github.com/iris-edu/mseed2sac
:适用平台: Linux、macOS
:推荐阅读: `Seed 格式转 SAC 格式 <https://blog.seisman.info/convert-seed-to-sac/>`__
:更新日期: 2021-01-27

------------------------

mseed2sac 可以直接将 miniSEED 文件转换为 SAC 格式，而不需要 dataless SEED 文件。

安装
--------

目前源码在 GitHub 上公开。

.. code-block:: bash

    $ wget https://github.com/iris-edu/mseed2sac/archive/v2.3.tar.gz
    $ tar -xvf v2.3.tar.gz
    $ cd mseed2sac-2.3
    $ make && mv mseed2sac ~/bin
    
    $ mseed2sac infile.miniseed  # 解压出来的 SAC 文件中只有台站名和台网名