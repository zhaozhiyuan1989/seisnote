# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# 删除所有运行产生的文件
clean:
	rm -rf build
	rm -rf source/gen_modules
	rm -rf source/obspydoc
	rm obspy/events.kml obspy/inv.pz obspy/singlechannel.pdf obspy/test.mseed


# obspy 绘图需要从服务器下载数据，较为缓慢，设置命令不运行任何 python 脚本
nofig:
	make html SPHINXOPTS="-D sphinx_gallery_conf.filename_pattern='/no_'"