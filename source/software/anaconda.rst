Anaconda
============

:软件来源: https://mirrors.tuna.tsinghua.edu.cn/
:适用平台: Linux、macOS、Windows
:推荐阅读: :doc:`seismo_software:anaconda/index`
:更新日期: 2021-01-27

------------------------

Anaconda 是一个用于科学计算的 Python 发行版，
其提供了方便使用的包管理器和环境管理器。

.. warning::

    安装 Anaconda 后再安装 :doc:`gmt` 可能会出现找不到依赖库的情况，
    把 Anaconda 环境变量注释后再安装 :doc:`gmt` ，完成后再取消注释即可。

安装
--------

.. code-block:: bash

    # 下载 Anaconda
    $ wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.sh

    # 安装
    $ bash Anaconda3-2020.11-Linux-x86_64.sh # 可以选择安装位置，最后一步 yes 添加环境变量
    $ source ~/.bashrc
    
    # 使用国内镜像源加速下载
    $ conda config --set show_channel_urls yes
    $ vim .condarc   

    # 说明：channels 中包括了搜索库，默认只有 defaults，自己添加了 conda-forge
    # defaults 对应了 default_channels，官方只包括了 main、r、msys2，这里清华源添加了 free 和 pro
    # custom_channels 中自定义了库的名称和 URL，用到时可添加到 channels 下
    # 添加越多解决依赖关系越慢
        channels:
          - conda-forge
          - defaults
        show_channel_urls: true
        default_channels:
          - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
          - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
          - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
          - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
          - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
        custom_channels:
          conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
          msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
          bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
          menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
          pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
          simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

    $ conda clean -i
    $ conda update conda

    # 不自动启动 Anaconda 的 base 环境
    $ conda config --set auto_activate_base False

    # 创建新的虚拟环境
    $ conda create -n seisnote
    # 激活环境
    $ conda activate seisnote
    # 取消激活
    $ conda deactivate

    # 利用 environment.yml 构建运行环境
    $ cat environment.yml 
        name: seisnote
        channels:
            - conda-forge
            - defaults
        dependencies:
            - python==3.8
            - pip
            - obspy
            - cartopy
            - pip:
              - sphinx-cjkspace
    $ conda env create

    # 激活运行环境
    $ conda activate seisnote
    # 查看所有环境
    $ conda info -e
    # 你可以随时删除创建的 seisnote 环境
    $ conda activate base
    $ conda remove -n seisnote --all

    # 搜索模块
    $ conda search obspy
    # 安装模块
    $ conda install obspy
    # 升级模块
    $ conda update obspy

