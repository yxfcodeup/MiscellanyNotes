## CentOS7 Minimal安装后配置
*参考网页：[用CentOS 7打造合适的科研环境](http://seisman.info/linux-environment-for-seismology-research.html)*
### 安装CentOS
***
#### 准备工作  
1. 准备材料  
```
U盘  
镜像：CentOS-7-x86_64-Everything-1503-01.iso
```

2. 制作U盘启动盘  
3. 插入电脑并安装CentOS-7  

#### 安装过程  
1. 选择安装过程中使用的语言，这里应使用英语，不要使用汉语。若安装界面使用汉语，最终安装的系统中会出现两个比较麻烦的问题：  
    * 家目录下的系统文件夹，比如Downloads、Desktop等会以中文表示，这使得在命令行 cd 变得很麻烦  
    * 终端中某些字符用英文字体，某些字符用中文字体，效果非常差，需要自己修改终端字体方可  
2. 选择区域和城市：Asia和Shanghai  
3. 键盘使用English(US)而不是English(UK)  
4. Hostname可以改也可以不改，我用master。安装完以后也可以进行修改  
```
$ hostnamectl set-hostname master (注：CentOS 7原有的修改hosts方法无效了) 
```

5. 安装的目的地，选择要使用的硬盘，在“Other Storage Options”处选择“I will configure partioning”，即手动分区  

#### 分区  
1. 点击“Click here to create them automatically”，即让安装程序帮忙分区  
2. 默认的分区方案是使用LVM，其好处在于“当机器有多块硬盘时，在使用的时候看上去只有一块”  
3. 默认的文件系统为XFS而不是以前常用的EXT4  
4. 自动分区完成后，再根据自己的需求，手动修改分区细节  
    * /boot ：CentOS自动分配，一定不要乱改  
    * / ：根目录，合理使用并及时清理的话15G就够了，不过建议30G以上
    * swap ：与物理内存大小一致即可  
    * /opt ：个人习惯是将第三方软件都安装在 /opt 下，所以分了70G  
    * /home ：余下的全部空间  
5. 点击“Begin to Install”开始安装  

#### 真正的安装  
1. 设置root密码  
2. 创建一般用户  
3. 等待安装完成  
4. 安装完成，重启  
5. 重启后，同意License即可  

### 对系统的若干修改  
***
*若干原则：  
为了搭建一个稳定的系统，尽量避免因为各种瞎折腾而导致的系统问题，特订立了一些软件安装的原则。具体参见[CentOS7下的软件安装方法与策略](http://seisman.info/how-to-install-softwares-under-centos-7.html)*  
#### 给一般账号root权限
默认情况下，一般账号是没有root权限的。为什么不直接用root账号，而是要给一般账号root权限呢？  
* 日常工作中使用root账号，是非常糟糕且危险的习惯！无论是服务器还是个人电脑都是如此  
* 安装软件时需要root权限，只能 su 切换到root账户再安装。对于习惯使用 sudo 的人来说，还是有些麻烦

自己的通用用户名为yxf，要授予他root权限，则要修改配置文件 /etc/sudoers  

```
$ su  
$ echo 'yxf ALL=(ALL) ALL' >> /etc/sudoers # 向配置文件中加入语句  
$ tail -1 /etc/sudoers  # 检查一下是否正确  
yxf ALL=(ALL) ALL  
```  

#### 添加第三方源  
CentOS由于很追求稳定性，所以官方源中自带的软件不多，因而需要一些第三方源，比如EPEL、ATrpms、ELRepo、Nux Dextop、RepoForge等。根据上面提到的软件安装原则，为了尽可能保证系统的稳定性，此处大型第三方源只添加EPEL源、Nux Dextop和ELRepo源。  
##### EPEL  
EPEL即Extra Packages for Enterprise Linux，为CentOS提供了额外的10000多个软件包，而且在不替换系统组件方面下了很多功夫，因而可以放心使用。  

```
$ yum install epel-release  
```

执行完该命令后，在 /etc/yum.repos.d 目录下会多一个 epel.repo 文件。
##### Nux Dextop  
Nux Dextop中包含了一些与多媒体相关的软件包，作者尽量保证不覆盖base源。官方说明中说该源与EPEL兼容，实际上个别软件包存在冲突，但基本不会造成影响:   

```
$ rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm  
```  

完成该命令后，在 /etc/yum.repos.d 目录下会多一个 nux-dextop.repo 文件。  
##### ELRepo  
ELRepo包含了一些硬件相关的驱动程序，比如显卡、声卡驱动:  

```
$ rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org  
$ rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm  
```  

完成该命令后，在 /etc/yum.repos.d 目录下会多一个 elrepo.repo 文件。
##### Ali源

```
$ wget -O /etc/yum.repos.d/CentOS-Ali.repo http://mirrors.aliyun.com/repo/Centos-7.repo
```

##### 安装yum-axelget  
添加完第三方源后需要yum makecache一下。  
yum-axelget是EPEL提供的一个yum插件。使用该插件后用yum安装软件时可以并行下载，大大提高了软件的下载速度，减少了下载的等待时间:  
```
$ yum makecache  
$ yum install yum-axelget
```  

安装该插件的同时会安装另一个软件axel。axel是一个并行下载工具，在下载http、ftp等简单协议的文件时非常好用。  
#### 第一次全面更新  
在进一步操作之前，先把已经安装的软件包都升级到最新版:
```
$ sudo yum update
```  

要更新的软件包有些多，可能需要一段时间。不过有了yum-axelget插件，速度已经快了很多啦。  
#### 重启  
此处建议重启。  
#### 删除多余的kernel  
在前面的 yum update 执行之后，可能会将kernel也一起更新，则在启动CentOS时启动项中会有很多项。  
确认当前使用的kernel版本号:  
```
$ uname -r
3.10.0-123.9.3.el7.x86_64  
```  

查找当前系统安装的所有kernel:  
```
$ rpm -qa | grep kernel | sort  
kernel-3.10.0-123.8.1.el7.x86_64  
kernel-3.10.0-123.9.2.el7.x86_64  
kernel-3.10.0-123.9.3.el7.x86_64  
kernel-devel-3.10.0-123.8.1.el7.x86_64  
kernel-devel-3.10.0-123.9.2.el7.x86_64  
kernel-devel-3.10.0-123.9.3.el7.x86_64  
kernel-headers-3.10.0-123.9.3.el7.x86_64  
kernel-tools-3.10.0-123.9.3.el7.x86_64  
kernel-tools-libs-3.10.0-123.9.3.el7.x86_64  
```

可以看出有三个版本的kernel，123.8.1、123.9.2和123.9.3。除了最新的kernel外，建议多保留一个旧kernel，以免新kernel出现问题时可以通过旧kernel进入系统。因而此处删除123.8.1版本的kernel:  
```
$ sudo yum remove kernel-3.10.0-123.8.1.el7.x86_64  
$ sudo yum remove kernel-devel-3.10.0-123.8.1.el7.x86_64  
```  

#### 桌面环境下目录语言  
若是GNOME桌面环境，且为中文目录，执行以下命令将目录更改为英文目录，  
```
$ export LANG=en_US  
$ xdg-user-dirs-update  
$ export LANG=zh_CN.UTF-8  
```

#### 网络相关设置  
* 静态IP设置  
```
$ vim /etc/sysconfig/network-scripts/ifcfg-eno16777736 #我自己使用的是虚拟机，实体机安装略有不同  
TYPE="Ethernet"  
BOOTPROTO="none"  
DEFROUTE="yes"  
PEERDNS="yes"  
PEERROUTES="yes"  
IPV4_FAILURE_FATAL="no"  
IPV6INIT="yes"  
IPV6_AUTOCONF="yes"  
IPV6_DEFROUTE="yes"  
IPV6_PEERDNS="yes"  
IPV6_PEERROUTES="yes"  
IPV6_FAILURE_FATAL="no"  
NAME="eno16777736"  
UUID="2f615c54-abaf-4d19-8868-9600cd816b55"  
DEVICE="eno16777736"  
ONBOOT="yes"  
IPADDR="192.168.2.111"  
PREFIX="24"  
GATEWAY="192.168.2.1"  
DNS1="8.8.8.8"   
```

* 关闭防火墙  
```
$ systemctl status firewalld.service（查看防火墙状态）  
$ systemctl stop firewalld.service（关闭防火墙）  
$ systemctl disable firewalld.service（永久关闭防火墙）
```

* 检测SSH是否安装，若没有，则安装SSH  
* 配置本机localhost模式SSH无密钥登陆  
```
$ su yxf 
$ ssh-keygen -t rsa -P ''
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys  
$ chmod 600 ~/.ssh/authorized_keys  
$ su  
$ vim /etc/ssh/sshd_config  
RSAAuthentication yes #启用RSA认证
PubkeyAuthentication yes #启用公钥私钥配对认证方式
AuthorizedKeysFile .ssh/authorized_keys #公钥文件路径
```

* 安装必要网络工具  
```
$ yum install net-tools -y  
$ yum install wget*  
```

* Samba使用  
```
待定
```

### 基础开发环境  
*** 
#### GCC系列
```
$ sudo yum install gcc                     # C编译器  
$ sudo yum install gcc-c++                 # C++编译器  
$ sudo yum install gcc-gfortran            # Fortran编译器  
$ sudo yum install compat-gcc-44           # 兼容gcc 4.4  
$ sudo yum install compat-gcc-44-c++       # 兼容gcc-c++ 4.4  
$ sudo yum install compat-gcc-44-gfortran  # 兼容gcc-fortran 4.4  
$ sudo yum install compat-libf2c-34        # g77 3.4.x兼容库  
```

#### 软件开发辅助工具
```
$ sudo yum install make
$ sudo yum install gdb     # 代码调试器  
$ sudo yum install cmake   # Cmake  
$ sudo yum install git     # 版本控制  
$ sudo yum install tig     # git的文本模式接口  
$ sudo yum install git-svn # git的svn插件  
```

### 驱动程序  
***
*虚拟机下可略过此步骤*
#### 显卡驱动  
Linux默认只使用开源的显卡驱动，就目前的情况来看，开源驱动的效果还是不错的，但跟官方的闭源驱动相比还是有一定差距。最明显的区别是，在使用SAC的ppk功能放大波形时，使用开源驱动会出现延迟，而使用官方闭源则整个过程非常顺畅。  
关于显卡驱动的安装，请参考[Linux下安装nvidia显卡驱动](http://seisman.info/install-nvidia-drivers-under-linux.html)一文中的“从ELRepo源中安装驱动”部分。  
*注意：目前的显卡驱动似乎有问题，安装后终端有时会出现屏幕闪烁、一屏文字上下重复跳动的情况，稍微有些影响用vim写代码。是否要安装显卡驱动自己决定。*
#### NTFS驱动  
CentOS下默认无法挂载NTFS格式的硬盘。需安装nfts-3g即可实现即插即用:  
```
$ sudo yum install ntfs-3g
```  

### 进阶开发环境  
*** 
#### Java环境  
Java的一大特色在于跨平台，安装了Java运行环境，即可运行Java程序:  
```
$ sudo yum install java                        # java运行环境
```

*此处建议下载自己所需版本的Java版本使用*
*使用SE7和SE8双版本，随时切换*
```
#以下为自定义安装jdk的方法
$ Chmod –R 777 /opt/
$ tar -zxvf jdk-7u79-linux-x64.tar.gz -C /opt/
$ mv jdk1.7.0_79/ java
$ vim /etc/profile     
#加入以下内容
export JAVA_HOME=/opt/java
export JRE_HOME=${JAVA_HOME}/jre  
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib  
export PATH=${JAVA_HOME}/bin:$PATH
#然后source /etc/profile
#再用以下命令配置默认JDK版本
$ update-alternatives --install /usr/bin/java java /usr/opt/java/bin/java 300
$ update-alternatives --install /usr/bin/javac javac /opt/java/bin/javac 300
$ update-alternatives --install /usr/bin/jar jar /opt/java/bin/jar 300   
$ update-alternatives --install /usr/bin/javah javah /opt/java/bin/javah 300
$ update-alternatives --install /usr/bin/javap javap /opt/java/bin/javap 300
$ update-alternatives --config java
```

#### Clang系列  
Clang可以认为是GCC的替代品，可以用于编译C、C++、Objective-C和Objective-C++。其提供了更友好的报错信息，在有些方面比GCC更友好，同时其提供了一个代码静态分析器，可以用于分析代码中可能出现的bug和内存溢出问题。  
```
$ sudo yum install clang             # clang编译器
$ sudo yum install clang-analyzer    # clang静态分析器
```  
####　Intel系列  
Intel的大部分软件都是非开源且收费的，但同时部分软件也提供了Linux下的非商业免费版。比如icc、mkl数学库以及代码性能分析工具等。  
Intel软件的申请以及安装参考[《Intel非商业免费开发工具》](http://seisman.info/intel-non-commercial-software.html)。  
还有一点需要注意的是，Intel也提供了并行相关的几个命令，比如mpicc、mpirun。所以openmpi、mpich和intel三者，在并行时只能用其中一个。  
#### 并行计算  
并行可以用openmpi，也可以用mpich，二者应该是并列的。但是由于二者提供了几乎一样的命令，所以二者可以同时安装，但是不可以同时处于使用状态。  
* 安装openmpi  
```
$ sudo yum install openmpi openmpi-devel
```

安装后，二进制文件位于 /usr/lib64/openmpi/bin 下，动态库文件位于 /usr/lib64/openmpi/lib 下，因而实际使用的话还需要额外的配置，在 .bashrc 中加入如下语句:  
```
export PATH=/usr/lib64/openmpi/bin/:${PATH}  
module load mpi/openmpi-x86_64  
```

*PS：要使用 module 命令需要先安装 environment-modules 包。*  
* 安装mpich  
```
$ sudo yum install mpich mpich-devel  
```

安装后，二进制文件位于 /usr/lib64/mpich/bin 下，动态库文件位于 /usr/lib64/mpich/lib 下，因而实际使用的话还需要额外的配置，在 .bashrc 中加入如下语句:  
```
export PATH=/usr/lib64/mpich/bin/:${PATH}  
module load mpi/mpich-x86_64  
```

### 脚本语言环境  
***
#### Perl  
CentOS 7.0自带了Perl 5.16.3（2013年03月11日发布），目前的最新版本为5.20.1（2014年09月14日发布）。  
* 系统自带Perl
系统自带Perl，就目前来看，版本不算老，基本够用。官方源和EPEL源中提供了1000多个模块，可以直接用yum安装:  
```
$ sudo yum install perl-Parallel-ForkManager  # 并行模块
```

若源中没有已打包好的模块，也可以使用perl自带的cpan来安装模块。
*优先级：yum > cpan*  
* plenv管理新版本  
若需要使用最新版本的perl，可以使用plenv安装新版本的perl，并使用plenv提供的cpanm命令安装模块:  
```
$ cpanm install Parallel::ForkManager # 并行模块
```

#### Python  
CentOS 7.0自带Python 2.7.5，目前Python 2的最新版本为2.7.8，Python 3的最新版本为3.4.2。  
* 系统自带Python  
系统自带的Python 2.7.5，基本已经够用，Python 2常用的模块在官方源或EPEL源中也有有编译好的包，因而直接通过yum安装即可:  
```
$ sudo yum install pylint
$ sudo yum install python-debug
$ sudo yum install python-devel
$ sudo yum install python-lxml
$ sudo yum install python-setuptools
$ sudo yum install python-matplotlib  # 2D绘图库
$ sudo yum install PyQt4  # Qt4的Python绑定
$ sudo yum install numpy  # 数组操作库
$ sudo yum install scipy  # 科学计算库
$ sudo yum install python-requests  # 网页请求
$ sudo yum install python-docopt  # 命令行参数分析器
$ sudo yum install gdal-python    # gdal的Python绑定
```  

* pyenv管理Python3  
Python2与Python3之间是不完全兼容的，而我以Python3为主，所以需要安装一个Python3。  
首先，安装pyenv来管理多个Python版本，然后利用pyenv安装anaconda3（即Python 3.4）。anaconda自带了众多科学计算所需的包，免去了安装的麻烦，对于其他包，则可以利用Python自带的pip安装:  
```
$ pip install requests
$ pip install docopt
```

* python3.4
```
$ yum install python34 python34-Cython python34-PyYAML python34-debug python34-devel python34-libs python34-numpy python34-setuptools 
```

* easy_install && pip
下载ez_setup.py，然后
```
$ python ez_setup.py
$ python3 ez_setup.py
$ easy_install-2.7 pip
$ easy_install-3.4 pip
```

* 第三方库
以下pip可以换成pip3，部分第三方库有效，可以先查找后再安装。对于部分库，在Python2和Python3上面有所区别，因此需要由源码编译安装。
```
$ pip install lxml  
$ pip install -U selenium
$ pip install pyvirtualdisplay
```

##### 在Linux服务器上同时安装python2和python3
在centos上，python2.7是默认安装。因此，下载python3源码在配置的时候指定prefix, 然后安装。最后将python3链接到/usr/bin/python或者/usr/local/bin/python
```
$ su  
$ ./configure --prefix=/opt/python3  
$ make & make install  
$ ln -s /opt/python3/python3/bin/python3 /usr/bin/python3
```
Manual installation and use of setuptools is not the standard process anymore.  
** If you're running Python 2.7.9+ or Python 3.4+  **
Congrats, you should already have pip installed. If you do not, read onward.  
If you're running a Unix-like System  
You can usually install the package for pip through your package manager if your version of Python is older than 2.7.9 or 3.4, or if your system did not include it for whatever reason.  
Instructions for some of the more common distros follow.  
** Installing on Debian (Wheezy and newer) and Ubuntu (Trusty Tahr and newer) for Python 2.x **  
Run the following command from a terminal:  
```
sudo apt-get install python-pip
```
** Installing on Debian (Wheezy and newer) and Ubuntu (Trusty Tahr and newer) for Python 3.x **  
Run the following command from a terminal:  
```
sudo apt-get install python3-pip
```
** Installing pip on CentOS 7 for Python 2.x **  
On CentOS 7, you have to install setup tools first, and then use that to install pip, as there is no direct package for it.  
```
sudo yum install python-setuptools
sudo easy_install pip
```
** Installing pip on CentOS 7 for Python 3.x **
Assuming you installed Python 3.4 from EPEL, you can install Python 3's setup tools and use it to install pip.  
First command requires you to have enabled EPEL for CentOS7
```
sudo yum install python34-setuptools
sudo easy_install pip
```
If your Unix/Linux distro doesn't have it in package repos
Install using the manual way detailed below.
The manual way
If you want to do it the manual way, the now-recommended method is to install using the get-pip.py script from pip's installation instructions.
```
Install pip
```
To install pip, securely download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
Then run the following (which may require administrator access):
```
python get-pip.py
```
If setuptools is not already installed, get-pip.py will install setuptools for you.




### 编程相关软件
*** 
编辑器：  
* vim
* sublime text3
* Visual Studio Code  

IDE:  
* Python IDE：PyCharm Community Edition

### 各种工具软件
*** 
* Icinga-cn 
[主页链接](http://icinga-cn.sourceforge.net/)

### 个性化操作  
* ~/.bashrc
```
$ vim ~/.bashrc
alias ll='ls -al'
alias p='python3'
alias p2='python2'
```
