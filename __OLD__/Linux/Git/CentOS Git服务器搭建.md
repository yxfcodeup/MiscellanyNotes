## CentOS Git服务器搭建
#### 准备  
* Git  
* Gitolite

#### 安装配饰Git服务器  
```
sudo yum install git*
# 新建用户git
sudo adduser git  
passwd git  
su
chmod u+w /etc/sudoers  
cat "git ALL=(ALL) ALL" >> /etc/sudoers  
chmod u-w /etc/sudoers  
su git  
```

#### 安装Gitolite  
```
su git  
cd ~/
git clone git://github.com/sitaramc/gitolite  
gitolite/install -ln ~/bin    #assumes $HOME/bin exists and is in your $PATH
或者
gitolite/install -to ~/bin  
# 从工作站拷贝SSH公钥（也就是ssh-keygen默认生成的~/.ssh/id_dsa.pub文件），重命名为<yourname>.pub（我们这里使用ployo.pub作为例子）。然后执行下面的命令：  
gitolite setup -pk $HOME/ployo.pub  
# 上面一个命令在服务器上创建了一个名为gitolite-admin的Git仓库
```
最后，回到自己的工作站后，执行命令：  
```
git clone git@gitserver:gitolite-admin  
```
就完成了。

#### 配置文件和访问规则  

