## Git技巧
#### Http或Https方式设置记住用户名和密码的方法
设置记住密码：  
```
git config --global credential.helper cache  
```
如果想自己设置时间，可以这样做：  
```
git config credential.helper 'cache --timeout=3600'  
```
这样就设置一个小时之后失效  
长期存储密码：  
```
git config --global credential.helper store  
```
增加远程地址的时候带上密码也是可以的。(推荐)  
```
http://yourname:password@git.oschina.net/name/project.git  
```

#### Git设置账户邮箱
```
git config --global user.name yxfcodeup
git config --global user.email 825378343@qq.com
git config --list #查看已设置的
```

#### Git忽略文件(.gitignore)
在git中如果想忽略掉某个文件，不让这个文件提交到版本库中，可以使用修改根目录中 .gitignore 文件的方法（如无，则需自己手工建立此文件）。这个文件每一行保存了一个匹配的规则例如：  
```
"#"为注释 – 将被 Git 忽略  
*.a       # 忽略所有 .a 结尾的文件  
!lib.a    # 但 lib.a 除外  
/TODO     # 仅仅忽略项目根目录下的 TODO 文件，不包括 subdir/TODO  
build/    # 忽略 build/ 目录下的所有文件  
doc/*.txt # 会忽略 doc/notes.txt 但不包括 doc/server/arch.txt
```
规则很简单，不做过多解释，但是有时候在项目开发过程中，突然心血来潮想把某些目录或文件加入忽略规则，按照上述方法定义后发现并未生效，原因是.gitignore只能忽略那些原来没有被track的文件，如果某些文件已经被纳入了版本管理中，则修改.gitignore是无效的。那么解决方法就是先把本地缓存删除（改变成未track状态），然后再提交：  
```
git rm -r --cached .
git add .
git commit -m 'update .gitignore'
```
最后需要强调的一点是，如果不慎在创建.gitignore文件之前就push了项目，那么即使在.gitignore文件中写入新的过滤规则，这些规则也不会起作用，Git仍然会对所有文件进行版本管理。