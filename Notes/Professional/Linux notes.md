# Linux Notes
### 小技巧类  
* linux多个python版本共存切换方法
```  
python命令通常存在/usr/bin/python和/usr/local/bin/python下面，一般是符号链接，优先使用后者。如果有2.6和2.7两个版本，并且  
/usr/bin/python --> /usr/bin/python2.6  
/usr/local/bin/python --> /usr/local/bin/python2.7  
此时系统默认使用2.7, 如果想切换至2.6，直接用  sudo ln -s /usr/local/bin/python /usr/bin/python2.6即可。  
```

