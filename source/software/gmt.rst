GMT
============

:软件来源: http://mirrors.ustc.edu.cn
:适用平台: Linux、macOS、Windows
:推荐阅读: :doc:`gmtdoc:index`
:更新日期: 2021-01-27

------------------------

GMT 是地球科学最广泛使用的制图软件之一，具有强大的绘图功能和数据处理功能。

.. note::

    目前 GMT4 和 GMT5 都已经停止维护，建议直接学习 GMT6。

安装
-----------

由于一些地震学软件使用了较老版本的 GMT4，
因此本节同时介绍了 GMT6 和 GMT4 的安装。

.. warning::

    安装 Anaconda 后再安装 :doc:`gmt` 可能会出现找不到依赖库的情况，
    把 Anaconda 环境变量注释后再安装 :doc:`gmt` ，完成后再取消注释即可。

.. tabs::

    .. tab:: GMT6

        .. tabs::
        
            .. tab:: Ubuntu
            
                .. code-block:: bash
                   :linenos:

                    # 安装编译所需软件包
                    $ sudo apt update
                    $ sudo apt install build-essential cmake libcurl4-gnutls-dev libnetcdf-dev

                    # 安装可选软件包
                    $ sudo apt install ghostscript gdal-bin libgdal-dev libglib2.0-dev libpcre3-dev libfftw3-dev liblapack-dev

                    # 安装制作动画所需的软件包
                    $ sudo apt install graphicsmagick ffmpeg

                    # 下载软件包
                    $ cd ~/software/GMT-src
                    $ wget http://mirrors.ustc.edu.cn/gmt/gmt-6.1.1-src.tar.gz
                    $ wget http://mirrors.ustc.edu.cn/gmt/gshhg-gmt-2.3.7.tar.gz
                    $ wget http://mirrors.ustc.edu.cn/gmt/dcw-gmt-1.1.4.tar.gz

                    # 解压三个压缩文件
                    $ tar -xvf gmt-6.1.1-src.tar.gz
                    $ tar -xvf gshhg-gmt-2.3.7.tar.gz
                    $ tar -xvf dcw-gmt-1.1.4.tar.gz

                    # 将 gshhg 和 dcw 数据复制到 gmt 的 share 目录下
                    $ mv gshhg-gmt-2.3.7 gmt-6.1.1/share/gshhg-gmt
                    $ mv dcw-gmt-1.1.4 gmt-6.1.1/share/dcw-gmt

                    # 切换到 gmt 源码目录下
                    $ cd gmt-6.1.1

                    # 用文本编辑器新建并打开 CMake 用户配置文件
                    $ vim cmake/ConfigUser.cmake
                        set (CMAKE_INSTALL_PREFIX "/home/zhao/opt/GMT-6.1.1")
                        set (GMT_USE_THREADS TRUE)
                        set (GMT_ENABLE_OPENMP TRUE)
                    # 注意，此处新建的 build 文件夹位于 gmt-6.1.1 目录下，不是 gmt-6.1.1/cmake 目录下

                    # 编译安装，如果先安装了 anaconda，需要先注释掉环境变量
                    $ mkdir build
                    $ cd build/
                    $ cmake ..
                    $ make
                    $ make install

                    # 添加环境变量
                    $ vim ~/.bashrc    # 取消 anaconda 的注释
                        # GMT6 
                        export GMT6HOME=/home/zhao/opt/GMT-6.1.1
                        export PATH=${GMT6HOME}/bin:$PATH
                        export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${GMT6HOME}/lib64
                        # 关闭单行命令完成自动打开图片
                        export GMT_END_SHOW=off
                        # 将数据、配置文件放到自定义路径
                        export GMT_DATADIR=/home/zhao/data/gmtdata/
                        export GMT_CACHEDIR=/home/zhao/data/gmtdata/cache
                        export GMT_USERDIR=/home/zhao/data/gmtdata/
                    $ source ~/.bashrc

                    # GMT 添加中文字体
                    $ vim $GMT_DATADIR/PSL_custom_fonts.txt
                        STSong-Light--UniGB-UTF8-H  0.700    1
                        STFangsong-Light--UniGB-UTF8-H  0.700    1
                        STHeiti-Regular--UniGB-UTF8-H   0.700   1
                        STKaiti-Regular--UniGB-UTF8-H   0.700   1
                        STSong-Light--UniGB-UTF8-V  0.700    1
                        STFangsong-Light--UniGB-UTF8-V  0.700    1
                        STHeiti-Regular--UniGB-UTF8-V   0.700   1
                        STKaiti-Regular--UniGB-UTF8-V   0.700   1

                    # ghostscript 配置中文
                    $ sudo apt install poppler-data 
                    $ sudo apt install fonts-arphic-uming fonts-arphic-ukai  # 安装 gs 默认 Linux 字体
                    # 新建 winfonts 文件夹
                    $ sudo mkdir /usr/share/fonts/winfonts/   
                    # 将 Windows 下的中文字体拷贝过来
                    $ sudo cp /mnt/c/windows/fonts/{simhei.ttf,simkai.ttf,simsun.ttc,simfang.ttf} /usr/share/fonts/winfonts 
                    # 修改 gs 中文配置文件
                    $ sudo vim /etc/ghostscript/cidfmap.d/90gs-cjk-resource-gb1.conf    
                        % 原配置文件的内容，与 STSong-Light 等相关的四行必须删除
                        /BousungEG-Light-GB <</FileType /TrueType /Path (/usr/share/fonts/truetype/arphic/uming.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /GBZenKai-Medium    <</FileType /TrueType /Path (/usr/share/fonts/truetype/arphic/ukai.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /Song-Medium /GBZenKai-Medium ;
                        /Adobe-GB1      /BousungEG-Light-GB ;
                        /Adobe-GB1-Bold /GBZenKai-Medium ;
                        % 新增 Windows 字体的支持
                        /STSong-Light <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simsun.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /STFangsong-Light <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simfang.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /STHeiti-Regular <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simhei.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /STKaiti-Regular <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simkai.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
                    $ sudo update-gsfontmap

                    # 中文测试
                    $ vim gmt6.1.1-cn-test.sh
                        #!/bin/bash
                        gmt begin GMT_Chinese png
                        gmt set FONT_TITLE 25p,41,black
                        gmt set FONT_LABEL 15p,39,black
                        gmt text -R0/8/0/4 -JX12c/4c -Bxaf+l"X轴" -Byaf+l"Y轴" -BWSen+t"中文标题" -F+f << EOF
                        2 3.5 25p,39,black 中文宋体
                        2 2.5 25p,40,blue  中文仿宋
                        2 1.5 25p,41,red   中文黑体
                        2 0.5 25p,42,green 中文楷体
                        4 3.5 25p,43,black 中文宋体
                        5 3.5 25p,44,blue  中文仿宋
                        6 3.5 25p,45,red   中文黑体
                        7 3.5 25p,46,green 中文楷体
                        EOF
                        gmt end 
                    $ bash gmt6.1.1-cn-test.sh

                    # 将数据服务器更改为科大镜像
                    $ gmt set GMT_DATA_SERVER http://china.generic-mapping-tools.org
                    $ mv gmt.conf $GMT_DATADIR/

            .. tab:: Centos7

                .. code-block:: bash
                   :linenos:

                    # 安装 epel-release
                    $ sudo yum install epel-release

                    # 启用 GMT 官方仓库
                    $ sudo yum install yum-plugin-copr
                    $ sudo yum copr enable genericmappingtools/gmt

                    # 安装最新版GMT
                    $ sudo yum install gmt
                    
                    # 当有新版本发布时可直接更新
                    $ sudo yum update gmt

                    # ghostscript 配置中文
                    
                    $ sudo yum install ghostscript-chinese-zh_CN
                    # 新建 winfonts 文件夹
                    $ sudo mkdir /usr/share/fonts/winfonts/   
                    # 将 Windows 下的中文字体拷贝过来
                    $ sudo cp /mnt/c/windows/fonts/{simhei.ttf,simkai.ttf,simsun.ttc,simfang.ttf} /usr/share/fonts/winfonts 
                    # 修改 gs 中文配置文件
                    $ sudo vim /usr/share/ghostscript/conf.d/cidfmap.zh_CN
                        % 原配置文件的内容，与 STSong-Light 等相关的四行必须删除
                        /BousungEG-Light-GB <</FileType /TrueType /Path (/usr/share/fonts/truetype/arphic/uming.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /GBZenKai-Medium    <</FileType /TrueType /Path (/usr/share/fonts/truetype/arphic/ukai.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /Song-Medium /GBZenKai-Medium ;
                        /Adobe-GB1      /BousungEG-Light-GB ;
                        /Adobe-GB1-Bold /GBZenKai-Medium ;
                        % 新增 Windows 字体的支持
                        /STSong-Light <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simsun.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /STFangsong-Light <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simfang.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /STHeiti-Regular <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simhei.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /STKaiti-Regular <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simkai.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;

                    # 添加环境变量
                    $ vim ~/.bashrc    
                        # 将数据、配置文件放到自定义路径
                        export GMT_DATADIR=/home/zhao/data/gmtdata/
                        export GMT_CACHEDIR=/home/zhao/data/gmtdata/cache
                        export GMT_USERDIR=/home/zhao/data/gmtdata/
                    $ source ~/.bashrc

                    # GMT 添加中文字体
                    $ vim $GMT_DATADIR/PSL_custom_fonts.txt
                        STSong-Light--UniGB-UTF8-H  0.700    1
                        STFangsong-Light--UniGB-UTF8-H  0.700    1
                        STHeiti-Regular--UniGB-UTF8-H   0.700   1
                        STKaiti-Regular--UniGB-UTF8-H   0.700   1
                        STSong-Light--UniGB-UTF8-V  0.700    1
                        STFangsong-Light--UniGB-UTF8-V  0.700    1
                        STHeiti-Regular--UniGB-UTF8-V   0.700   1
                        STKaiti-Regular--UniGB-UTF8-V   0.700   1 

                    # 中文测试
                    $ vim gmt6.1.1-cn-test.sh
                        #!/bin/bash
                        gmt begin GMT_Chinese png
                        gmt set FONT_TITLE 25p,41,black
                        gmt set FONT_LABEL 15p,39,black
                        gmt text -R0/8/0/4 -JX12c/4c -Bxaf+l"X轴" -Byaf+l"Y轴" -BWSen+t"中文标题" -F+f << EOF
                        2 3.5 25p,39,black 中文宋体
                        2 2.5 25p,40,blue  中文仿宋
                        2 1.5 25p,41,red   中文黑体
                        2 0.5 25p,42,green 中文楷体
                        4 3.5 25p,43,black 中文宋体
                        5 3.5 25p,44,blue  中文仿宋
                        6 3.5 25p,45,red   中文黑体
                        7 3.5 25p,46,green 中文楷体
                        EOF
                        gmt end 
                    $ bash gmt6.1.1-cn-test.sh

                    # 将数据服务器更改为科大镜像
                    $ gmt set GMT_DATA_SERVER http://china.generic-mapping-tools.org
                    $ mv gmt.conf $GMT_DATADIR/

            .. tab:: Windows

                .. code-block::
                   :linenos:

                    1.  安装 GMT6

                        - http://mirrors.ustc.edu.cn/gmt/bin/gmt-6.1.1-win64.exe

                        安装过程中在 Choose components 页面，除 Ghostscript 组件外所有选项都勾选上。

                        安装完成后在 C:\Users\用户名\.gmt\PSL_custom_fonts.txt 中加入如下语句:

                            STSong-Light--GB-EUC-H  0.700    1
                            STFangsong-Light--GB-EUC-H  0.700    1
                            STHeiti-Regular--GB-EUC-H   0.700   1
                            STKaiti-Regular--GB-EUC-H   0.700   1
                            STSong-Light--GB-EUC-V  0.700    1
                            STFangsong-Light--GB-EUC-V  0.700    1
                            STHeiti-Regular--GB-EUC-V   0.700   1
                            STKaiti-Regular--GB-EUC-V   0.700   1                        

                    2.  安装 Ghostscript

                        - https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs950/gs950w64.exe

                        安装过程中必须勾选 Generate cidfmap for Windows CJK TrueType fonts 。

                        安装完成后必须添加环境变量：新建变量 GS_FONTPATH 并设置其值为 C:\Windows\fonts

                    3.  安装 UnixTools
                        
                        - https://gmt-china.org/data/UnixTools.zip

                        直接下载并解压到 GMT 的 bin 目录。

                    4.  中文测试

                        脚本文件和输入数据文件都必须采用 GB2312 编码方式。

                            gmt begin map pdf,png
                            REM GMT在Windows下处理中文存在一些已知BUG
                            REM 需要设置 PS_CHAR_ENCODING 为 Standard+ 以绕过这一BUG
                            gmt set PS_CHAR_ENCODING Standard+
                            gmt set FONT_TITLE 25p,41,black
                            gmt set FONT_LABEL 15p,39,black

                            echo 2 3.5 25p,39,black 中文宋体  > tmp
                            echo 2 2.5 25p,40,blue  中文仿宋 >> tmp
                            echo 2 1.5 25p,41,red   中文黑体 >> tmp
                            echo 2 0.5 25p,42,green 中文楷体 >> tmp
                            echo 4 3.5 25p,43,black 中文宋体 >> tmp
                            echo 5 3.5 25p,44,blue  中文仿宋 >> tmp
                            echo 6 3.5 25p,45,red   中文黑体 >> tmp
                            echo 7 3.5 25p,46,green 中文楷体 >> tmp

                            gmt text tmp -R0/8/0/4 -JX12c/4c -Bxaf+l"X轴" -Byaf+l"Y轴" -BWSen+t"中文标题" -F+f
                            del tmp
                            gmt end

    .. tab:: GMT4

        .. tabs::
        
            .. tab:: Ubuntu 
            
                .. code-block:: bash
                   :linenos:

                    # 安装编译所需软件包
                    $ sudo apt update
                    $ sudo apt install ghostscript
                    $ sudo apt install gcc g++ make libc6    # 开发工具
                    $ sudo apt install libnetcdf-dev libxaw7-dev

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

                    # ghostscript 配置中文
                    $ sudo apt install poppler-data 
                    $ sudo apt install fonts-arphic-uming fonts-arphic-ukai  # 安装 gs 默认 Linux 字体
                    # 新建 winfonts 文件夹
                    $ sudo mkdir /usr/share/fonts/winfonts/   
                    # 将 Windows 下的中文字体拷贝过来
                    $ sudo cp /mnt/c/windows/fonts/{simhei.ttf,simkai.ttf,simsun.ttc,simfang.ttf} /usr/share/fonts/winfonts 
                    # 修改 gs 中文配置文件
                    $ sudo vim /etc/ghostscript/cidfmap.d/90gs-cjk-resource-gb1.conf    
                        % 原配置文件的内容，与 STSong-Light 等相关的四行必须删除
                        /BousungEG-Light-GB <</FileType /TrueType /Path (/usr/share/fonts/truetype/arphic/uming.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /GBZenKai-Medium    <</FileType /TrueType /Path (/usr/share/fonts/truetype/arphic/ukai.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /Song-Medium /GBZenKai-Medium ;
                        /Adobe-GB1      /BousungEG-Light-GB ;
                        /Adobe-GB1-Bold /GBZenKai-Medium ;
                        % 新增 Windows 字体的支持
                        /STSong-Light <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simsun.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /STFangsong-Light <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simfang.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /STHeiti-Regular <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simhei.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /STKaiti-Regular <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simkai.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
                    $ sudo update-gsfontmap

                    # 中文测试
                    $ vim gmt4.5.18-cn-test.sh
                        #!/bin/bash
                        gmtset HEADER_FONT 35
                        pstext -R0/10/0/3 -JX15c/3c -B1/1:."GMT中文支持": -P > cn.ps <<EOF
                        1.5 2 30 0 35 LM GMT宋体
                        1.5 1 30 0 36 LM GMT仿宋
                        5.5 2 30 0 37 LM GMT黑体
                        5.5 1 30 0 38 LM GMT楷体
                        EOF
                        ps2raster cn.ps -A -P -Tg
                        rm .gmt* cn.ps
                        EOF
                    $ bash gmt4.5.18-cn-test.sh  # 执行脚本

            .. tab:: Centos7 
            
                .. code-block:: bash
                   :linenos:

                    # 安装编译所需软件包
                    $ sudo yum install gcc gcc-c++ make glibc  # 开发工具
                    $ sudo yum install netcdf netcdf-devel gdal gdal-devel gdal-python  # netCDF 库
                    $ sudo yum install libXaw-devel  # X 相关库
                    $ sudo yum install libICE-devel libSM-devel libX11-devel
                    $ sudo yum install libXext-devel libXmu-devel libXt-devel

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

                    # ghostscript 配置中文
                    $ ssudo yum install ghostscript-chinese-zh_CN  # 安装 gs 简体中文配置文件
                    # 新建 winfonts 文件夹
                    $ sudo mkdir /usr/share/fonts/winfonts/   
                    # 将 Windows 下的中文字体拷贝过来
                    $ sudo cp /mnt/c/windows/fonts/{simhei.ttf,simkai.ttf,simsun.ttc,simfang.ttf} /usr/share/fonts/winfonts 
                    # 修改 gs 中文配置文件
                    $ sudo vim /usr/share/ghostscript/conf.d/cidfmap.zh_CN
                        % 原配置文件的内容，与 STSong-Light 等相关的四行必须删除
                        /BousungEG-Light-GB <</FileType /TrueType /Path (/usr/share/fonts/truetype/arphic/uming.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /GBZenKai-Medium    <</FileType /TrueType /Path (/usr/share/fonts/truetype/arphic/ukai.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /Song-Medium /GBZenKai-Medium ;
                        /Adobe-GB1      /BousungEG-Light-GB ;
                        /Adobe-GB1-Bold /GBZenKai-Medium ;
                        % 新增 Windows 字体的支持
                        /STSong-Light <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simsun.ttc) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /STFangsong-Light <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simfang.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /STHeiti-Regular <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simhei.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;
                        /STKaiti-Regular <</FileType /TrueType /Path (/usr/share/fonts/winfonts/simkai.ttf) /SubfontId 0 /CSI [(GB1) 4] >> ;

                    # 中文测试
                    $ vim gmt4.5.18-cn-test.sh
                        #!/bin/bash
                        gmtset HEADER_FONT 35
                        pstext -R0/10/0/3 -JX15c/3c -B1/1:."GMT中文支持": -P > cn.ps <<EOF
                        1.5 2 30 0 35 LM GMT宋体
                        1.5 1 30 0 36 LM GMT仿宋
                        5.5 2 30 0 37 LM GMT黑体
                        5.5 1 30 0 38 LM GMT楷体
                        EOF
                        ps2raster cn.ps -A -P -Tg
                        rm .gmt* cn.ps
                        EOF
                    $ bash gmt4.5.18-cn-test.sh  # 执行脚本

            .. tab:: Windows

                .. code-block::
                   :linenos:

                    1.  安装 GMT4

                        - http://mirrors.ustc.edu.cn/gmt/bin/gmt-4.5.18-win64.exe
                        - http://mirrors.ustc.edu.cn/gmt/bin/gmt-4.5.18-pdf-win32.exe
                        - http://mirrors.ustc.edu.cn/gmt/bin/gshhg-2.3.7-win32.exe

                        依次安装，完成后在 C:\programs\gmt4\share\pslib\ 中加入如下语句:

                            STSong-Light--GB-EUC-H  0.700    1
                            STFangsong-Light--GB-EUC-H  0.700    1
                            STHeiti-Regular--GB-EUC-H   0.700   1
                            STKaiti-Regular--GB-EUC-H   0.700   1                      

                    2.  安装 Ghostscript

                        - https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs950/gs950w64.exe

                        安装过程中必须勾选 Generate cidfmap for Windows CJK TrueType fonts 。

                        安装完成后必须添加环境变量：新建变量 GS_FONTPATH 并设置其值为 C:\Windows\fonts

                    3.  安装 UnixTools
                        
                        - https://gmt-china.org/data/UnixTools.zip

                        直接下载并解压到 GMT 的 bin 目录。

                    4.  安装 Sumatra PDF 查看 PS 格式文件

                        - https://www.sumatrapdfreader.org/free-pdf-reader.html

常见问题
------------

- GMT6 下单行模式运行 GMT 命令会报错： ``sh: 1: xdg-open: not found``

这是因为单行命令会默认打开绘图结果，但是服务器或者 WSL 通常没有安装 ``xdg-open``\ ，
在 ``end`` 模块中有介绍，可以设置环境变量 ``GMT_END_SHOW=off``。

- GMT4 下 ``make`` 时报错： ``xgrid_Panner.c:4:10: fatal error: X11/Xaw/Scrollbar.h: No such file or directory`` 

登录 https://pkgs.org/ ，在网页右上角搜索 ``Scrollbar.h`` ，然后在 **Search** 一栏选择 **Files**，
根据筛选条件对 **Filter** 进行修改，找到所需的包后点击查看， 
例如在 Ubuntu 下 **Package name** 为 **libxaw7-dev**，
直接 ``sudo apt install libxaw7-dev`` 即可解决。