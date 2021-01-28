SAC 
============

:软件来源: http://ds.iris.edu/ds/nodes/dmc/software/downloads/sac/
:适用平台: Linux、macOS
:推荐阅读: :doc:`sacdoc:index`
:更新日期: 2021-01-27

------------------------

SAC 是天然地震学领域使用最广泛的数据分析软件包之一。

官方于 2020 年 9 月推出了 SAC 的 v102.0 版本,
新版本增加了很多新的功能和特性。

安装
--------

本节同时记录了常用版本 v101.6 和最新版本 v102.0 的安装使用步骤。

以下步骤在 Ubuntu20.04LTS 发行版通过测试。

.. tabs:: 

    .. tab:: v101.6

        .. tabs:: 
        
            .. tab:: Ubuntu
        
                .. code-block:: bash
                   :linenos:

                    # 安装依赖
                    $ sudo apt update
                    $ sudo apt install build-essential
                    $ sudo apt install libncurses5-dev libsm-dev libice-dev
                    $ sudo apt install libxpm-dev libx11-dev zlib1g-dev

                    # 解压
                    $ tar -xvf sac-101.6a_source.tar.gz

                    # 编译安装
                    $ cd sac-101.6a
                    $ mkdir build
                    $ cd build
                    $ ../configure --prefix=/home/zhao/opt/sac101  # 指定安装位置
                    $ make
                    $ sudo make install

                    # 添加环境变量
                    $ vim ~/.bashrc
                        # SAC
                        export SACHOME=/home/zhao/opt/sac101
                        export SACAUX=${SACHOME}/aux
                        export PATH=${SACHOME}/bin:${PATH}
                        export SAC_DISPLAY_COPYRIGHT=1
                        export SAC_PPK_LARGE_CROSSHAIRS=1
                        export SAC_USE_DATABASE=0
                    $ source ~/.bashrc

                    $ sac  # 测试是否安装成功

            .. tab:: Centos7
        
                .. code-block:: bash
                   :linenos:

                    # 安装依赖
                    $ sudo yum install gcc gcc-c++ make
                    $ sudo yum install glibc ncurses-devel libSM-devel libICE-devel
                    $ sudo yum install libXpm-devel libX11-devel zlib-devel

                    # 解压
                    $ tar -xvf sac-101.6a_source.tar.gz

                    # 编译安装
                    $ cd sac-101.6a
                    $ mkdir build
                    $ cd build
                    $ ../configure --prefix=/home/zhao/opt/sac101  # 指定安装位置
                    $ make
                    $ sudo make install

                    # 添加环境变量
                    $ vim ~/.bashrc
                        # SAC
                        export SACHOME=/home/zhao/opt/sac101
                        export SACAUX=${SACHOME}/aux
                        export PATH=${SACHOME}/bin:${PATH}
                        export SAC_DISPLAY_COPYRIGHT=1
                        export SAC_PPK_LARGE_CROSSHAIRS=1
                        export SAC_USE_DATABASE=0
                    $ source ~/.bashrc

                    $ sac  # 测试是否安装成功

    .. tab:: v102.0

        .. tabs::

            .. tab:: Ubuntu    
    
                .. code-block:: bash 
                   :linenos:

                    # v102.0 版本安装方式有所变化
                    # 安装依赖
                    $ sudo apt install build-essential
                    $ sudo apt install libncurses5-dev libsm-dev libice-dev
                    $ sudo apt install libxpm-dev libx11-dev zlib1g-dev

                    # 解压
                    $ tar -xvf sac-102.0-linux_x86_64.tar.gz

                    # 移动到安装目录
                    $ mv sac ~/opt/sac102

                    # 添加环境变量
                    $ vim ~/.bashrc
                        # SAC102
                        export SACHOME=/home/zhao/opt/sac102
                        . ${SACHOME}/bin/sacinit.sh

                    # 根据需求修改环境变量 SACHOME 一定要修改 
                    $ vim ~/opt/sac102/bin/sacinit.sh

                    $ source ~/.bashrc
                    $ sac  # 测试是否安装成功

            .. tab:: Centos7
        
                .. code-block:: bash
                   :linenos:

                    # 安装依赖
                    $ sudo yum install gcc gcc-c++ make
                    $ sudo yum install glibc ncurses-devel libSM-devel libICE-devel
                    $ sudo yum install libXpm-devel libX11-devel zlib-devel

                    # 解压
                    $ tar -xvf sac-102.0-linux_x86_64.tar.gz

                    # 移动到安装目录
                    $ mv sac ~/opt/sac102

                    # 添加环境变量
                    $ vim ~/.bashrc
                        # SAC102
                        export SACHOME=/home/zhao/opt/sac102
                        . ${SACHOME}/bin/sacinit.sh

                    # 根据需求修改环境变量 SACHOME 一定要修改 
                    $ vim ~/opt/sac102/bin/sacinit.sh

                    $ source ~/.bashrc
                    $ sac  # 测试是否安装成功