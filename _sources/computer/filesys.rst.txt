文件管理
============

:推荐阅读: :doc:`seismo_101:best-practices/file-organization`
:更新日期: 2021-01-27

-----------------------------

**“正确管理电脑文件是非常重要的。错误的文件管理方式会使你花费更多的时间去寻找文件，拖慢你的科研进度，还可能导致文件的大量冗余与误删。”**

在上述思想的指导下，我将 Linux 下的文件管理方式在此记录。

.. code-block:: bash

    $ cd ~
    $ tree -d -L 2
        .
        ├── anaconda3            # Anaconda 默认安装位置
        │   ├── ...
        │   
        ├── bin                  # 存放可直接执行的二进制程序
        ├── codes                # 存放自己写的代码
        │   ├── gmtscript
        │   └── ...
        ├── data                 # 存放数据
        │   └── gmtdata          # 存放 GMT 相关数据配置文件
        ├── go                   # 用于美化 Windows Terminal 下的 WSL
        │   ├── ...
        ├── opt                  # 地震学软件安装目录
        │   ├── GMT-6.1.1
        │   ├── GMT4
        │   ├── TauP-2.4.5
        │   ├── sac101
        │   ├── sac102
        │   └── ...
        ├── perl5                # cpan 产生
        │   ├── ...
        ├── project              # 存放项目
        │   ├── tomoDD
        │   ├── ...
        ├── software             # 备份软件安装包
        │   ├── CPS330-src
        │   ├── FMC-src
        │   ├── GMT-src
        │   ├── ...
        │   ├── SAC-src
        │   ├── SACTools-src
        │   ├── TauP-arc
        │   ├── VELEST-src
        │   ├── ccp-src
        │   ├── focmec-src
        │   ├── hk-src
        │   ├── hypo2000-src
        │   ├── hypodd-src
        │   ├── matlab-src
        │   ├── mseed2ascii-src
        │   ├── mseed2sac-src
        │   ├── oh-my-cap
        │   ├── rdseed-src
        │   └── tomoDD-src
        ├── src                   # 存放别人写的简单源代码
        └── workspace             # 临时测试脚本命令
            

