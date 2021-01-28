WSL 安装配置
=============

:推荐阅读: :doc:`seismo_101:computer/wsl-setup`
:更新日期: 2021-01-27

-------------------------------------------------------------------------------

安装 WSL
--------

WSL 的安装方式可以参考官方文档：

- 中文指南：https://docs.microsoft.com/zh-cn/windows/wsl/install-win10

推荐使用 WSL 安装 Ubuntu 20.04 LTS。

在 CMD 或者 PowerShell 中输入::

   $ wsl --set-default-version 2  # 默认安装版本为 WSL2

到商店内进行安装，很快完成后输入用户账号密码，
然后输入 ``sudo passwd root`` 修改 root 密码。

导入的 WSL 系统默认以 root 启动，在管理员权限的 PowerShell 中
输入如下命令即可改为非 root 用户，其中 UbuntuName 为发行版的名称::

   Get-ItemProperty Registry::HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Lxss\*\ DistributionName | Where-Object -Property DistributionName -eq UbuntuName  | Set-ItemProperty -Name DefaultUid -Value 1000
    
如果发生意外，可以在 PowerShell 中输入::

   $ Ubuntu config --default-user root
   $ bash
   $ passwd

即可修改 root 密码。然后输入::

   $ Ubuntu config --default-user xxx  # 切回账号  
   $ wsl --export Ubuntu E:\WSLBAK\WSL2-UBUNTU-20210120-NEW.tar  # 导出
   $ wsl --unregister Ubuntu    # 注销删除
   $ wsl --import Ubuntutest D:\VirtualMachine\WSLDIR\Ubuntutest E:\WSLBAK\WSL2-UBUNTU-20210120-NEW.tar    # 导入

安装 WSL 之后，还需要对 Linux 系统进行配置。

Ubuntu 用户可以参考《\ :doc:`/computer/ubuntu_setup`\ 》对系统进行配置，以满足科研工作的需求。

配置 WSL
-----------

- Visual Studio Code 

安装插件 ``Remote - WSL`` 和 ``Settings Sync`` 。

- Windows Terminal

https://docs.microsoft.com/zh-cn/windows/terminal/tutorials/powerline-setup

界面美观、操作方便，支持同时开启多个 CMD、PowerShell 以及 WSL，
随意切换无卡顿。可完全替代 CMD 和 PowerShell。

在 Windows 下安装 Windows Terminal 后安装字体 Cascadia Code PL，
然后在 **设置** 中修改初始目录和字体::

   "guid": "{2c4de342-38b7-51cf-b940-2309a097f518}",
   "hidden": false,
   "name": "Ubuntu",
   "source": "Windows.Terminal.Wsl",
   "startingDirectory": "//wsl$/Ubuntu/home/zhao",
   "fontFace":  "Cascadia Code PL"

- Powerlinego

美化 Windows Terminal 的外观，显示 Git 分支状态。

.. code-block:: bash

    $ sudo apt install golang-go
    $ vim ~/.bashrc
        GOPATH=$HOME/go
        function _update_ps1() {
        PS1="$($GOPATH/bin/powerline-go -error $?)"
        }
        if [ "$TERM" != "linux" ] && [ -f "$GOPATH/bin/powerline-go" ]; then
        PROMPT_COMMAND="_update_ps1; $PROMPT_COMMAND"
        fi

    $ go get -u github.com/justjanne/powerline-go
    
    # 由于网络问题可能会出现 package golang.org/x/crypto/ssh/terminal
    # 参考 https://www.phpbloger.com/article/346.html
    $ mkdir -p ~/go/src/golang.org/x
    $ cd ~/go/src/golang.org/x
    
    # 报错了提到了 crypto、sys、text、term
    $ git clone git@github.com:golang/crypto.git
    $ git clone git@github.com:golang/sys.git
    $ git clone git@github.com:golang/text.git
    $ git clone git@github.com:golang/term.git
    $ go get -u github.com/justjanne/powerline-go



安装 X Server
--------------

WSL 本身不支持图形界面，需要在 Windows 中安装 X Server
来接收和显示 Linux 中的图形界面。

1.  下载 `VcXsrv <https://sourceforge.net/projects/vcxsrv/>`__\ ，默认安装即可

2.  运行 XLaunch，在 **Extra settings** 界面勾选 **Disable access control**\，其他选项无需更改

3.  Windows 每次重启后，WSL2 nameserver 的 IP 可能发生变化，修改 Linux 的
    环境变量以保证始终能连接到 X Server::

        $ echo "export DISPLAY=\$(awk '/nameserver / {print \$2; exit}' /etc/resolv.conf 2>/dev/null):0" >> ~/.bashrc
        $ echo "export LIBGL_ALWAYS_INDIRECT=1" >> ~/.bashrc
        $ source ~/.bashrc

4.  打开图形界面进行测试::

        # x11-apps 中包含了很多小程序如 xclock、xeyes
        $ sudo apt install x11-apps

        # 运行 xclock。若能看到一个时钟窗口，则表示图形界面设置成功
        $ xclock

.. note::

   安装并配置好 X Server 之后，切记先运行 XLaunch 再进入 Linux 环境打开图形界面。

 