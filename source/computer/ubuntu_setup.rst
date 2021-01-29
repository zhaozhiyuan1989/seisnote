Ubuntu 安装配置
====================

:推荐阅读: :doc:`seismo_101:computer/ubuntu_setup`
:更新日期: 2021-01-27

-----------------------------

安装
--------


更换 apt 源
--------------

::
    $ sudo vim /etc/apt/sources.list     # 将 apt 更换为国内源
        :%s/security.ubuntu/mirrors.aliyun/g
        :%s/archive.ubuntu/mirrors.aliyun/g
        :wq
    $ sudo apt update     # 更新
    $ sudo apt upgrade

更换 pip 源
-------------

    $ sudo apt install python3-pip
    $ sudo ln -s /usr/bin/python3 /usr/bin/python   # 更换 python名
    $ sudo ln -s /usr/bin/pip3 /usr/bin/pip   # 更换 pip 名
    $ mkdir ~/.pip
    $ cd ~/.pip
    $ sudo vim pip.conf   # 更换 pip 国内源
        [global] 
        index-url = https://pypi.tuna.tsinghua.edu.cn/simple
        [install]
        trusted-host = https://pypi.tuna.tsinghua.edu.cn 
        :wq

安装工具
---------------

::

    # 安装编译器
    $ sudo apt install make gcc g++ gfortran 

    $ 安装常用工具
    $ sudo apt install unzip tree

    # 添加 bin 环境变量
    $ echo 'export PATH=${HOME}/bin:${PATH}' >> ~/.bashrc
    $ source ~/.bashrc

git
-------------

在 WSL 上安装 git 进行代码开发协作。

https://www.liaoxuefeng.com/wiki/896043488029600/896067074338496

::

    $ sudo apt install git
    $ git config --global user.name "zhaozhiyuan1989"
    $ git config --global user.email "shetu2008@163.com"
    $ ssh-keygen -t rsa -C "shetu2008@163.com"

然后到 GitHub 和 Gitee 上添加 id_rsa.pub，Gitee 可以在 Github 连接缓慢的时候提供帮助，不过下载后需要去 .git 文件夹中修改 conf 改为 Github 的地址。 `git remote -v`
