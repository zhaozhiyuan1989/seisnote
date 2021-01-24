# 地震学学习笔记

![build](https://github.com/zhaozhiyuan1989/seisnote/workflows/CI/badge.svg)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc/4.0/deed.zh)


本项目主要用来记录在不同操作系统上安装、使用和学习地震学软件时遇到的一些问题。

- 项目主页：https://github.com/zhaozhiyuan1989/seisnote
- 网页版：https://zhaozhiyuan1989.github.io/seisnote/

## 构建项目

本项目使用 [Sphinx](http://www.sphinx-doc.org/) 构建得到。Sphinx 是基于 Python 的
文档生成工具。

1.  下载文档源码

        git clone git@github.com:zhaozhiyuan1989/seisnote.git

2.  安装所需依赖

        cd seisnote
        pip install -r requirements.txt

3.  编译生成 HTML 格式的文档。生成的文档位于 `build/html/` 目录下

        make html

## 项目部署

本项目采用 GiHub Actions 自动部署到 gh-pages 分支。

## 许可协议

本作品采用 [知识共享署名-非商业性使用 4.0 国际许可协议 (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.zh) 。
任何人都可以自由地分享、修改本作品，但必须遵循如下条件：

- 署名：必须提到原作者，提供指向此许可协议的链接，表明是否有做修改
- 非商业性使用：不能对本作品进行任何形式的商业性使用
