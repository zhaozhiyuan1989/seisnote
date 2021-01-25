# 地震学学习笔记

![build](https://github.com/zhaozhiyuan1989/seisnote/workflows/CI/badge.svg)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc/4.0/deed.zh)


本项目主要用来记录学习过程中遇到的一些问题。

- 项目主页： https://github.com/zhaozhiyuan1989/seisnote
- GitHub Pages： https://zhaozhiyuan1989.github.io/seisnote/
- Gitee Pages： https://seismology.gitee.io/seisnote

因为 Gitee Pages 目前是手动同步 GitHub Pages，所以可能会有延迟更新。

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

4.  维护

        # 创建并切换到开发分支
        $ git checkout -b mydev
        
        # 合并主分支的更新
        $ git checkout main
        $ git pull
        $ git checkout mydev
        $ git merge main

        # 修改并提交
        $ git add --all
        $ git commit -m ""

        # 将开发分支推送到远程仓库
        $ git push -u origin mydev
        $ git push
        
        # 切换回主分支
        $ git checkout main
        # 删除本地开发分支
        $ git branch -D mydenv
        # 删除远程开发分支
        $ git push origin :mydev

## 项目部署

本项目采用 GiHub Actions 自动部署到 gh-pages 分支。

## 许可协议

本作品采用 [知识共享署名-非商业性使用 4.0 国际许可协议 (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.zh) 。
任何人都可以自由地分享、修改本作品，但必须遵循如下条件：

- 署名：必须提到原作者，提供指向此许可协议的链接，表明是否有做修改
- 非商业性使用：不能对本作品进行任何形式的商业性使用
