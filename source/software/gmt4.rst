GMT4
============

:软件来源: http://mirrors.ustc.edu.cn
:适用平台: Linux、macOS、Windows
:推荐阅读: `GMT4 官方文档 <http://www.soest.hawaii.edu/gmt/gmt/html/>`__
:更新日期: 2021-01-27

------------------------

.. note::

    目前 GMT4 和 GMT5 都已经停止维护，建议直接学习 :doc:`gmt6`\ 。

安装
-----------

2018 年官方推出 GMT4.5.18 后不再对 GMT4 进行维护。

由于很多老的脚本都是用 GMT4 的语法写的，全部修改成新的语法很麻烦而且没有必要，最好的办法就是同时安装 GMT4 和 GMT 的最新版本。

下面简要介绍 GMT4 的安装。

.. warning::

    如果已经安装了 :doc:`anaconda` ，安装 GMT 过程中可能会出现找不到依赖库的情况，
    把 :doc:`anaconda` 环境变量注释后再安装 GMT，完成后再取消注释即可。

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


用法指南
------------

GMT4 绘图脚本非常简单，无非就是以下三步：**配置参数**、**设置变量**、**模块绘图**。

**配置参数**\ 时可以利用 ``gmtdefaults`` 模块来快速查询参数具体名称和参数值的格式。

**设置变量**\ 是为了简化脚本，在不同平台设置变量的语法不同，可根据实际情况自行搜索。

**模块绘图**\ 需要你了解所有 GMT 常用模块的基本用途，这样你才能知道绘图时都需要用到哪些模块，
我们不需要把所有模块的语法全部背会，用到的时候去查模块的用法就可以了。
模块绘图的顺序就跟画画是一样的，从最底层画起，一层盖一层，最终完成绘制。

绘图时脚本中所有的单位都应该显式表达，比如 ``JX6c/-3c`` 最好不要写成 ``JX6/-3``，
因为不同电脑中默认单位可能会不一致。

最容易出错的地方就是模块绘图时 ``-K`` ``-O`` ``>`` ``>>`` 的使用，请给予足够重视。

掌握了脚本的写作思路后，剩下的就是根据实际需要去查询模块用法了。
需要了解的是，在每个模块之后都有一些如 ``-R`` ``-W`` 之类的选项，
在所有模块中含义用法都相同的选项叫做\ **标准选项**，
而\ **非标准选项**\ 在不同模块中的用法含义完全不同；
在使用某个模块时必须要用的选项叫做\ **必选选项**\ ，可用可不用的选项叫做这个模块的\ **可选选项**\ 。

常见问题
------------

- **make** 时报错： ``xgrid_Panner.c:4:10: fatal error: X11/Xaw/Scrollbar.h: No such file or directory`` 

 登录 https://pkgs.org/ ，在网页右上角搜索 **Scrollbar.h** ，然后在 **Search** 一栏选择 **Files**，
 根据筛选条件对 **Filter** 进行修改，找到所需的包后点击查看， 
 例如在 Ubuntu 下 **Package name** 为 **libxaw7-dev**，
 直接 ``sudo apt install libxaw7-dev`` 即可解决。

附录
---------

``gmtdefaults`` 模块用来列出 GMT 所有参数的系统默认值或当前值：

.. code-block:: bash

    $ gmtdefautls -D   # 列出所有参数的系统默认值
    $ gmtdefautls -L   # 列出所有参数的当前值

它的主要用处是快速查询某个参数的准确名称或参数值的格式：

.. code-block:: bash

    $ gmtdefaults -L | grep PLOT
        PLOT_CLOCK_FORMAT	= hh:mm:ss
        PLOT_DATE_FORMAT	= yyyy-mm-dd
        PLOT_DEGREE_FORMAT	= ddd:mm:ss

下面列出 GMT4 所有参数的简介，详细用法请参考该模块
的 `官方文档 <http://www.soest.hawaii.edu/gmt/gmt/html/man/gmtdefaults.html>`__ ：

.. code-block:: bash

    $ gmtdefaults -L
    #
    #-------- Plot Media Parameters -------------
    PAGE_COLOR		= white     # 纸张背景色
    PAGE_ORIENTATION	= landscape  # 纸张方向为水平，垂直用portrait
    PAPER_MEDIA		= a4    # 纸张大小
    #-------- Basemap Annotation Parameters ------
    ANNOT_MIN_ANGLE		= 20 # 倾斜投影最小标注角
    ANNOT_MIN_SPACING	= 0  # 相邻标注间最小距离
    ANNOT_FONT_PRIMARY	= Helvetica  # 主轴标注字体
    ANNOT_FONT_SIZE_PRIMARY	= 14p  # 主轴标注字体大小
    ANNOT_OFFSET_PRIMARY	= 0.2c  # 主轴标注与主轴之间的距离
    ANNOT_FONT_SECONDARY	= Helvetica  # 次轴标注字体
    ANNOT_FONT_SIZE_SECONDARY	= 16p  # 次轴标注字体大小
    ANNOT_OFFSET_SECONDARY	= 0.2c  # 次轴标注与次轴之间的距离
    DEGREE_SYMBOL		= ring  # 度符号
    HEADER_FONT		= Helvetica  # 标题字体
    HEADER_FONT_SIZE	= 36p    # 标题字体大小
    HEADER_OFFSET		= 0.5c   # 标题与上边界的距离
    LABEL_FONT		= Helvetica  # 轴标签字体
    LABEL_FONT_SIZE		= 24p    # 轴标签字体大小
    LABEL_OFFSET		= 0.3c   # 轴标注底部与轴标签顶部之间的距离
    OBLIQUE_ANNOTATION	= 1    # 倾斜投影的标注方式
    PLOT_CLOCK_FORMAT	= hh:mm:ss  # 绘图时间标注格式
    PLOT_DATE_FORMAT	= yyyy-mm-dd  # 绘图日期标注格式
    PLOT_DEGREE_FORMAT	= ddd:mm:ss  # 绘图经纬度标注格式，常用 ddd.xF
    Y_AXIS_TYPE		= hor_text  # Y轴标注水平或垂直 ver_text
    #-------- Basemap Layout Parameters ---------
    BASEMAP_AXES		= WESN   # 控制显示标注的边框，常用 WesN
    BASEMAP_FRAME_RGB	= black  # 底图边框的颜色
    BASEMAP_TYPE		= fancy  # 底图类型。inside：标注和刻度朝内。graph：线性投影，轴有箭头。fancy：火车轨道。plain：线。
    FRAME_PEN		= 1.25p  # plain 边框宽度
    FRAME_WIDTH		= 0.2c   # fancy 边框宽度
    GRID_CROSS_SIZE_PRIMARY	= 0c  # 一级网格线的交叉线大小，0表示连续
    GRID_PEN_PRIMARY	= 0.25p # 一级网格线的线条属性
    GRID_CROSS_SIZE_SECONDARY	= 0c # 二级网格线的交叉线大小，0表示连续
    GRID_PEN_SECONDARY	= 0.5p  # 二级网格线的线条属性
    MAP_SCALE_HEIGHT	= 0.2c  # 地图比例尺高度
    POLAR_CAP		= 85/90  # 控制两极地区网格线
    TICK_LENGTH		= 0.2c  # 刻度线的长度，负值代表向内，-JX6i/-3i表示Y轴反向
    TICK_PEN		= 0.5p  # 刻度线的属性
    X_AXIS_LENGTH		= 25c  # 设置x轴默认长度
    Y_AXIS_LENGTH		= 15c  # 设置y轴默认长度
    X_ORIGIN		= 2.5c  # 新图在纸张上的原点坐标
    Y_ORIGIN		= 2.5c  # 新图在纸张上的原点坐标
    UNIX_TIME		= FALSE  # 是否显示时间戳，可用-U控制
    UNIX_TIME_POS		= BL/-2c/-2c # 时间戳位置
    UNIX_TIME_FORMAT	= %Y %b %d %H:%M:%S  # 时间戳格式
    #-------- Color System Parameters -----------
    COLOR_BACKGROUND	= black   # 图片背景色，Z值小于cpt文件中最小值时的颜色
    COLOR_FOREGROUND	= white  # 图片前景色，Z值大于cpt文件中最大值时的颜色
    COLOR_NAN		= 128   # Z值为NAN时的颜色
    COLOR_IMAGE		= adobe   # 控制PS的渲染方式
    COLOR_MODEL		= rgb   # 对cpt文件插值时使用的颜色模型
    HSV_MIN_SATURATION	= 1   # 模拟光照时最小负强度对应的饱和度S值
    HSV_MAX_SATURATION	= 0.1 # 模拟光照时最大正强度对应的饱和度S值
    HSV_MIN_VALUE		= 0.3 # 模拟光照时最小负强度对应的明度V值
    HSV_MAX_VALUE		= 1   # 模拟光照时最大正强度对应的明度V值
    #-------- PostScript Parameters -------------
    CHAR_ENCODING		= ISOLatin1+  # 字符编码
    DOTS_PR_INCH		= 300  # 绘图精度，每英寸像素数
    GLOBAL_X_SCALE		= 1   # 整体缩放时x方向的比例
    GLOBAL_Y_SCALE		= 1   # 整体缩放时y方向的比例
    N_COPIES		= 1   # 每张图的绘图数量
    PS_COLOR		= rgb  # 设置生成PS代码时使用的颜色模型
    PS_IMAGE_COMPRESS	= lzw  # 设置PS中图像压缩算法
    PS_IMAGE_FORMAT		= ascii  # 生成PS图像格式
    PS_LINE_CAP		= butt # 控制线段端点绘制方式。butt：不对端点做处理。round：端点处为直径与线宽相等的半圆弧。square：端点处为边长与线宽相等的半个正方形。
    PS_LINE_JOIN		= miter # 控制线段拐点的绘制方式。
    PS_MITER_LIMIT		= 35  # 设置 miter 拐角的角度阈值
    PS_VERBOSE		= FALSE # 是否在PS文件中写详细注释
    TRANSPARENCY		= 0  # 设置透明度
    #-------- I/O Format Parameters -------------
    D_FORMAT		= %.12lg  # 双精度浮点数的输出格式
    FIELD_DELIMITER		= tab   # GMT输出每列的分隔符
    GRIDFILE_FORMAT		= nf   # 默认网格文件格式
    GRIDFILE_SHORTHAND	= FALSE  # 是否检查网格文件后缀名
    INPUT_CLOCK_FORMAT	= hh:mm:ss  # 输入文件的时间格式
    INPUT_DATE_FORMAT	= yyyy-mm-dd  # 输入文件的日期格式
    IO_HEADER		= FALSE  # 输入输出文件是否有头段
    N_HEADER_RECS		= 1  # 如果有头端默认为1个
    NAN_RECORDS		= pass  # 遇到NAN值跳过
    OUTPUT_CLOCK_FORMAT	= hh:mm:ss  # 输出文件的时间格式
    OUTPUT_DATE_FORMAT	= yyyy-mm-dd  # 输出文件的日期格式
    OUTPUT_DEGREE_FORMAT	= D  # 控制地理坐标数据的输出格式
    XY_TOGGLE		= FALSE  # 经纬度互换
    #-------- Projection Parameters -------------
    ELLIPSOID		= WGS-84  # 地球椭球模型
    MAP_SCALE_FACTOR	= default # 最小化面积失真所使用的比例因子
    MEASURE_UNIT		= cm  # 默认单位长度
    #-------- Calendar/Time Parameters ----------
    TIME_FORMAT_PRIMARY	= full # 一级标注中月份、周名的格式。full：January。abbrevaite：Jan。character：J。
    TIME_FORMAT_SECONDARY	= full # 二级标注中月份、周名的格式
    TIME_EPOCH		= 2000-01-01T12:00:00  # 指定所有相对时间的参考时刻
    TIME_IS_INTERVAL	= OFF  # 输入日期不按间隔调整
    TIME_INTERVAL_FRACTION	= 0.5   # 时间标注置于间隔中心
    TIME_LANGUAGE		= us   # 时间语言
    TIME_UNIT		= d  # 指定相对时间数据相对于参考时刻的单位
    TIME_WEEK_START		= Sunday  # 指定一周的第一天
    Y2K_OFFSET_YEAR		= 1950  # 给定用两位数字表示四位数年份时100年序列的第一年1950-2049，51表示1951，20表示2020
    #-------- Miscellaneous Parameters ----------
    HISTORY			= TRUE # 是否记录历史命令中的参数
    INTERPOLANT		= akima  # 一维插值算法
    LINE_STEP		= 0.025c  # 绘制直线时取点的间隔
    VECTOR_SHAPE		= 0    # 矢量箭头形状。0：三角形。1：箭头形状。2：打开的v字
    VERBOSE			= FALSE # 运行时是否显示详细信息，-V