TauP 
============

:软件来源: http://www.seis.sc.edu/taup/
:适用平台: Linux、macOS、Windows
:更新日期: 2021-01-27

------------------------

TauP 是一款 Java 语言编写的计算射线走时、路径的程序。

安装
-----------

以下步骤在 Ubuntu20.04LTS 发行版通过测试。

.. code-block:: bash

    # 下载软件包
    $ wget http://www.seis.sc.edu/downloads/TauP/TauP-2.4.5.tgz

    # 解压
    $ tar -xvf TauP-2.4.5.tgz

    # 移动到安装目录
    $ sudo mv TauP-2.4.5 ~/opt

    # 添加环境变量
    $ echo 'export TAUPHOME=/home/zhao/opt/TauP-2.4.5' >> ~/.bashrc
    $ echo 'export PATH=${TAUPHOME}/bin:${PATH}' >> ~/.bashrc
    $ source ~/.bashrc

    # 安装 Java 环境
    $ sudo apt install default-jdk   # 安装java环境

    $ taup    # 若出现图形界面则安装成功

常用命令
-----------

- ``taup_time``\ ：用于计算震相走时、射线参数、出射角、入射角等信息

- ``taup_curve``\ ：用于计算并绘制震相的走时曲线（走时—震中距关系曲线）

- ``taup_path``\ ：用于计算并绘制射线的传播路径

- ``taup_setsac``\ ：命令用于计算理论走时并将走时信息写入到 SAC 文件头段变量中

具体使用方法可参考 https://seismo-learn.org/software/taup/ 。