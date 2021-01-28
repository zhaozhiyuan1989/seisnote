GMT4 
============

:软件来源: http://mirrors.ustc.edu.cn
:适用平台: Linux、macOS、Windows
:更新日期: 2021-01-27

------------------------

GMT 是地球科学最广泛使用的制图软件之一，具有强大的绘图功能和数据处理功能。

GMT4 版本较老，已经停止维护。

一些老的程序可能会用到 GMT4，除此之外不建议安装老版本的 GMT。

安装
-----------

以下步骤在 Ubuntu20.04LTS 发行版通过测试。

.. code-block:: bash

    # 安装编译所需软件包
    $ sudo apt-get update
    $ sudo apt install ghostscript
    $ sudo apt-get install gcc g++ make libc6    # 开发工具
    $ sudo apt-get install libnetcdf-dev libxaw7-dev

    # 下载软件包
    $ wget http://mirrors.ustc.edu.cn/gmt/gmt-4.5.18-src.tar.bz2
    $ wget http://mirrors.ustc.edu.cn/gmt/gshhg-gmt-2.3.7.tar.gz

    # 解压
    $ tar -xvf gmt-4.5.18-src.tar.bz2

    # 编译安装 GMT4
    $ cd gmt-4.5.18
    $ ./configure --prefix=/home/zhao/opt/GMT4  # 指定 gmt 安装路径
    $ make
    $ sudo make install-all
    $ cd ../

    # 解压海岸线数据
    $ tar -xvf gshhg-gmt-2.3.7.tar.gz
    # 移动到 GMT4 安装目录
    $ sudo mv gshhg-gmt-2.3.7 ~/opt/GMT4/share/coast

    # 修改环境变量
    $ echo 'export GMT4HOME=/home/zhao/opt/GMT4' >> ~/.bashrc     
    $ echo 'export PATH=${GMT4HOME}/bin:$PATH'>> ~/.bashrc
    $ echo 'export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${GMT4HOME}/lib64'>> ~/.bashrc
    $ exec $SHELL -l

    $ psxy -   # 测试

    # GMT4 配置中文
    $ sudo vim /opt/GMT4/share/pslib/PS_font_info.d
        # 在文末添加字体  
        STSong-Light--UniGB-UTF8-H  0.700    1
        STFangsong-Light--UniGB-UTF8-H  0.700    1
        STHeiti-Regular--UniGB-UTF8-H   0.700   1
        STKaiti-Regular--UniGB-UTF8-H   0.700   1

    $ pstext -L  # 查看 gmt 当前支持字体

    # 中文测试
    $ vim gmt4.5.18-cn-test.sh
        #!/bin/bash
        gmtset HEADER_FONT 35
        pstext -R0/10/0/3 -JX15c/3c -B1/1:."GMT中文支持": -P > cn.ps        <<EOF
        1.5 2 30 0 35 LM GMT宋体
        1.5 1 30 0 36 LM GMT仿宋
        5.5 2 30 0 37 LM GMT黑体
        5.5 1 30 0 38 LM GMT楷体
        EOF
        ps2raster cn.ps -A -P -Tg
        rm .gmt* cn.ps
    $ bash gmt4.5.18-cn-test.sh  # 执行脚本

常见问题
------------

- ``make`` 出错， ``xgrid_Panner.c:4:10: fatal error: X11/Xaw/Scrollbar.h: No such file or directory`` 

在 https://pkgs.org/ 搜索 ``Scrollbar.h`` ，筛选条件为 **file**，**Ubuntu20.04LTS**，
找到 **package name** 为 **libxaw7-dev**，``sudo apt install libxaw7-dev`` 解决。