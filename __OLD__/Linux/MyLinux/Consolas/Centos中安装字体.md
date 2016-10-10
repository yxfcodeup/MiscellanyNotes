## Centos中安装字体
此处以YaHei.Consolas.1.12.ttf为例。
* 在fonts目录下建立相关的字体文件夹，并设定权限
```
sudo mkdir -p /usr/share/fonts/consolas
sudo cp YaHei.Consolas.1.12.ttf /usr/share/fonts/consolas
sudo chmod 644 /usr/share/fonts/consolas/*.ttf
```

* 安装字体
```
cd /usr/share/fonts/consolas
sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fv
```