distaz
============

:软件来源: http://www.seis.sc.edu/software/distaz/
:适用平台: Linux、macOS、Windows
:推荐阅读: :doc:`seismo_software:utilities/distaz`
:更新日期: 2021-01-27

------------------------

``distaz`` 是一个可以用于计算球面上任意两点间球面距离、方位角和反方位角的小工具。

安装
--------

.. code-block:: bash

    $ wget http://www.seis.sc.edu/software/distaz/distaz.c
    $ cc distaz.c -o distaz -lm
