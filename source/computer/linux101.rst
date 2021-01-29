Linux 基础
============

:推荐阅读: https://101.lug.ustc.edu.cn/
:更新日期: 2021-01-27

-----------------------------

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

.. code-block:: bash

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

