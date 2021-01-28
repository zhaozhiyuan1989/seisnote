MATLAB
============

:软件来源: 暂无
:适用平台: Linux、macOS、Windows
:推荐阅读: 暂无
:更新日期: 2021-01-27

------------------------


.. admonition:: 免责声明

   若使用 MATLAB 请付费购买正版，本文仅抱着学习的目的
   研究 MATLAB 在 Linux 下的安装使用。


安装
--------

.. code-block:: bash

    $ cd ~
    $ sudo mkdir tmp
    $ sudo mount -o loop software/matlab-src/MATHWORKS_R2014A.iso tmp
    $ cd tmp
    $ sudo ./install
    # - without internet
    # - create symbolink to /usr/local/bin
    # - activate number: 12345-67890-12345-67890
    # - license: Crack/license_405329_R2014a.lic
    # - cp Crack/Linux/libmwservices.so /usr/local/MATLAB/R2014A/bin/glnxa64
    $ sudo umount tmp
    $ rm -rf tmp
    $ matlab &

.. note::

    若在 WSL 中安装，需要提前安装并运行 X server。
    经测试，仅在 WSL2 中安装成功。

常见问题
---------

- **Windows 下在 Jupyter 中添加 MATLAB kernel**

如果 MATLAB 安装在系统盘，很可能没有写入权限，这时需要在有权限的地方编译，
在 MATLAB 窗口输入以下命令

.. code-block:: matlab

    cd (fullfile(matlabroot,'extern','engines','python'))
    system('python setup.py build --build-base="d:\builddir" install') % 安装完成之后可以删除builddir文件夹
    system('pip install matlab_kernel')
    system('jupyter kernelspec list')

详情可参考 `MATLAB官方说明 <https://ww2.mathworks.cn/help/matlab/matlab_external/install-matlab-engine-api-for-python-in-nondefault-locations.html>`__\ 。
