cpdf
============

:软件来源: https://github.com/coherentgraphics/cpdf-binaries
:适用平台: Linux、macOS、Windows
:推荐阅读: `cpdf 示例 <http://www.coherentpdf.com/usage-examples.html>`__
:更新日期: 2021-01-27

------------------------

安装
-------

cpdf 是一款开箱即用的软件，
下载 :download:`cpdf-binaries-master.zip <https://github.com/coherentgraphics/cpdf-binaries/archive/master.zip/>` 后，
将执行程序放到 PATH 路径下即可使用。

常用示例
-----------

.. warning::

    对于命令中 ``%`` 用作特殊字符的， 在 Windows 的 bat 文件中应该用 ``%%`` 来代替。

PDF 切割合并 
^^^^^^^^^^^^^^^

.. code-block:: bash

    # 切割 in.pdf 的 1-3 页以及 12 至最后页并输出到 out.pdf
    $ cpdf in.pdf 1-3,12-end -o out.pdf
    # 切割 in.pdf 倒数第 5 页至倒数第 3 页
    $ cpdf in.pdf ~5-~3 -o out.pdf
    # 切割 in.pdf 的偶数页
    $ cpdf in.pdf even -o out.pdf
    # 切割 in.pdf 的奇数页
    $ cpdf in.pdf odd -o out.pdf
    # 将 in.pdf 切割成单页文件 page001.pdf page002.pdf 等
    $ cpdf -split in.pdf -o page%%%.pdf  # bat 中应为 page%%%%%%.pdf
    # 将 in.pdf 每 10 页切割成 1 个 pdf 文件
    $ cpdf -split in.pdf -o Chunk%%%.pdf -chunk 10  # bat 中应为 Chunk%%%%%%.pdf
    # 以书签为分界线切割 in.pdf
    $ cpdf -split-bookmarks 0 in.pdf -o @N.pdf
    # 合并 one.pdf two.pdf three.pdf 并输出到 merge.pdf
    $ cpdf one.pdf two.pdf three.pdf -o merged.pdf
    # 合并所有 2017 开头的 pdf 文件
    $ cpdf 2017*.pdf -o out.pdf
    # 在 1，3，4 页后添加空白页
    $ cpdf -pad-after 1,3,4 in.pdf -o out.pdf


PDF 页面信息
^^^^^^^^^^^^^^

.. code-block:: bash

    # 输出文件的一些相关信息
    $ cpdf -info file.pdf
    # 输出每页的信息
    $ cpdf -page-info file.pdf
    # 设置 PDF 中所有文本内容为黑色
    $ cpdf -blacktext in.pdf -o out.pdf
    # 在 x 和 y 方向上将 in.pdf 尺寸参数都缩放 2 倍
    $ cpdf -scale-page "2 2" in.pdf -o out.pdf
    # 将页面缩放为 A4 纸
    $ cpdf -scale-to-fit a4portrait in.pdf -o out.pdf
    # 试卷模式，将 in.pdf 每 2 页组成 8 开纸
    $ cpdf -twoup-stack in.pdf -o out.pdf
    # 将 in.pdf 页面内容向 x 方向移动 26pt ， y 方向移动 18mm
    $ cpdf -shift "26pt 18mm" in.pdf -o out.pdf
    # 将 in.pdf 内容顺时针旋转 90 度
    $ cpdf -rotate-contents 90 in.pdf -o out.pdf
    # 将 in.pdf 切割成 600pt x 400pt 的矩形
    $ cpdf -crop "0 0 600pt 400pt" in.pdf -o out.pdf
    # 裁剪文件
    $ cpdf -crop "20mm 20mm 300mm 300mm" in.pdf -o out.pdf 

PDF 加密和解密
^^^^^^^^^^^^^^^^

.. code-block:: bash

    # 加密 in.pdf ，文件所有者密码为 zzy ，普通用户密码为 user
    $ cpdf -encrypt 128bit zzy user in.pdf -o encrypt.pdf
    # 使用文件所有者密码解密 encrypt.pdf
    $ cpdf -decrypt encrypt.pdf owner=zzy -o decrypt.pdf

PDF 压缩和解压缩
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # 压缩数据流
    $ cpdf -compress in.pdf -o out.pdf
    # 解压缩
    $ cpdf -decompress in.pdf -o out.pdf

PDF 书签和注释
^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # 列出 in.pdf 所有书签
    $ cpdf -list-bookmarks in.pdf
    0 "Part 1" 1 open
    1 "Part 1A" 2
    2 "Part 1B" 3
    0 "Part 2" 4
    1 "Part 2a" 5
    # 将书签文件 bookmarks.txt 中所列书签（与上述格式相同）添加到 in.pdf 
    $ cpdf -add-bookmarks bookmarks.txt in.pdf -o out.pdf
    # 列出 in.pdf 所有注释
    $ cpdf -list-annotations in.pdf
        --------------------------------
        Annotation text content 1
        --------------------------------

        --------------------------------
        Annotation text content 2
        --------------------------------
    # 将 from.pdf 中的注释信息添加到 in.pdf
    $ cpdf -copy-annotations from.pdf in.pdf -o out.pdf

PDF 演讲模式
^^^^^^^^^^^^^^

.. code-block:: bash

    # 使用 Split 样式从 in.pdf 构建演示文稿，每个幻灯片保持 10s ，作为标题的第一页不会自动移动
    $ cpdf -presentation in.pdf 2-end -trans Split -duration 10 -o out.pdf
    # 设置 pdf 打开时进入全屏模式
    $ cpdf -set-page-mode FullScreen in.pdf -o out.pdf

PDF 添加文本或者 logo
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # 添加带页码的文本
    $ cpdf -add-text "Page %Page of %EndPage" -top 100pt -font "Times-Roman" -font-size 20 in.pdf -o out.pdf
    # 在每一页添加 logo
    $ cpdf -stamp-on logo.pdf in.pdf -o out.pdf
    # 使用 AND 来同时执行几个命令：合并 in.pdf 和 in2.pdf 并在每一页上添加版权印记
    $ cpdf -merge in.pdf in2.pdf AND -add-text "Copyright 2017" -o out.pdf
    # 在 pdf 第 5 页附加一个文件
    $ cpdf -attach-file sheet.xls -to-page 5 in.pdf -o out.pdf
    # 删除所有附加文件
    $ cpdf -remove-files in.pdf -o out.pdf