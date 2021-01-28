Linux 基础
============

:推荐阅读: https://101.lug.ustc.edu.cn/
:更新日期: 2021-01-27

-----------------------------

``apt`` 和 ``dpkg``
----------------------

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

``curl``
-----------

``curl: error while loading shared libraries: libssl.so.1.0.0: cannot open shared object file: No such file or directory``
``curl: symbol lookup error: curl: undefined symbol: curl_mime_free``

升级 conda ``conda update conda`` 解决问题。

``tldr``
-----------

非常简洁的命令用法查询工具。

.. code-block:: bash

    $ sudo apt install tldr
    $ tldr tar  # 查询 tar 的用法

执行命令会自动克隆远程仓库到 ``~/.tldr`` 文件夹。

``trap ... DEBUG``
-------------------

解决 SHELL 指令同时显示命令和执行结果，以 ``echo`` 开头的行只显示结果的问题。

``trap DEBUG`` 表示读取每行的命令赋予变量 ``$BASH_COMMAND``，
先执行 ``trap DEBUG`` 中间的命令后在执行 ``$BASH_COMMAND``。

.. code-block::

    $ cat test.sh
        trap '[[ $BASH_COMMAND != echo* ]] && echo $BASH_COMMAND' DEBUG
        echo 显示 GMT 的版本号
        gmt --version

    $ bash test.sh
        显示 GMT 的版本号
        gmt --version
        6.1.1

``x11``
-----------

seisman:

The biggest difference is: libx11-6 only provides libraries, while libx11-dev provides both header files and libraries (libx11-dev depends on libx11-6).

When you run SAC, you need libraries, so libx11-6 must be installed.

When you want to build SAC from source codes, you need both libraries and headers, so you have to install libx11-dev.

That's also why the libx11-dev package has the -dev suffix, because you only need it when you're developing something (i.e., compileing a package from source).

