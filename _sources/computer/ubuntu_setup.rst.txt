Ubuntu 安装配置
====================

:推荐阅读: :doc:`seismo_101:computer/ubuntu-setup`
:更新日期: 2021-01-27

-----------------------------

安装
--------

Ubuntu 的安装方式请参考《\ :doc:`seismo_101:computer/ubuntu-setup`\ 》。

更换软件源
--------------

将 Ubuntu 的软件源更换为国内镜像源以提高下载速度。

.. code-block:: bash

    $ sudo vim /etc/apt/sources.list     # 将 apt 更换为国内源
        :%s/security.ubuntu/mirrors.aliyun/g
        :%s/archive.ubuntu/mirrors.aliyun/g
        :wq
    $ sudo apt update     # 更新
    $ sudo apt upgrade

``dpkg`` 是 Debian 的一个底层包管理工具，
主要用于对已下载到本地和已安装的软件包进行管理。

.. code-block:: bash

    $ dpkg -i package-name.deb  # 安装 deb 包
    $ dpkg -r package-name.deb  # 移除 deb 包，保留配置文件
    $ dpkg -P package-name.deb  # 清除 deb 包所有文件
    $ dpkg -l name-pattern      # 查看系统中的软件包
    $ dpkg -L name-pattern      # 查看安装文件及目录
    $ dpkg -s                   # 查看已安装软件包的信息
    $ dpkg -l | grep ssh
    $ dpkg -L openssh-client
    $ dpkg -s openssh-client

``dpkg`` 解决了软件安装过程中的大量问题，``apt`` 能解决软件安装过程中的依赖问题

.. code-block:: bash

    $ apt update                # 从软件源服务器获取最新的软件信息并缓存到本地
    $ apt upgrade               # 已安装的软件有新版本的话则进行升级
    $ apt list                  # 列出本地仓库中所有的软件包名
    $ apt list --installed      # 列出系统中所有已安装的包名
    $ apt search                # 搜索包
    $ apt show                  # 列出指定包的详细信息
    $ apt install               # 安装指定的包，并同时安装其依赖的其他包
    $ apt remove                # 卸载包，但不删除相关配置文件
    $ apt autoremove            # 卸载因安装软件自动安装的依赖，而现在又不需要的依赖包 
    $ apt purge                 # 卸载包，同时删除相关配置文件
    $ apt clean                 # 删除所有已下载的软件包
    $ apt autoclean             # 类似 clean，但删除的是过期的包
    $ apt list --installed | grep x11


.. tip::

    Linux 用户也可以访问 https://pkgs.org/ 网站查询软件包。
    该网站支持多种 Linux 发行版和多个官方及第三方软件仓库，
    且为每个软件包提供了丰富的元信息、依赖和被依赖关系、包含的文件、
    安装方式以及更新历史等信息。

更换 pip 源
-------------------

Ubuntu 可能没有预安装 pip3，需要自行安装并更换镜像源。

.. code-block:: bash

    $ sudo apt install python3-pip
    $ sudo ln -s /usr/bin/python3 /usr/bin/python   # 更换 python 名
    $ sudo ln -s /usr/bin/pip3 /usr/bin/pip   # 更换 pip 名
    $ mkdir ~/.pip
    $ cd ~/.pip
    $ sudo vim pip.conf   # 更换 pip 国内源
        [global] 
        index-url = https://pypi.tuna.tsinghua.edu.cn/simple
        [install]
        trusted-host = https://pypi.tuna.tsinghua.edu.cn 
        :wq

.. note::

    更推荐在 Linux 中使用 :doc:`/software/anaconda` 来安装使用 Python。


git
-------------

在 Ubuntu 上安装 git 进行代码开发协作。

.. code-block:: bash

    # 在本机上配置个人信息
    $ sudo apt install git
    $ git config --global user.name "zhaozhiyuan1989"
    $ git config --global user.email "shetu2008@163.com"
    $ ssh-keygen -t rsa -C "shetu2008@163.com"

然后到 `GitHub <https://github.com/>`__ 
和 `Gitee <https://gitee.com/>`__ 上添加 ``id_rsa.pub``，
Gitee 可以在 Github 连接缓慢的时候提供帮助，
从 Gitee 上克隆下载后需要在 :file:`.git/config` 文件中
修改为 Github 的地址。 
