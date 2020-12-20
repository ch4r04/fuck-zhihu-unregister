# fuck-zhihu-unregister
提供给你批量删除知乎回答、关注、收藏夹、想法的工具(Just fuck Zhihu)
如果你无法注销，可用本项目进行删除。
走、资、狗、乎,再见。



# 安装
##  0x1
```
pip install -r requirements.txt
```
## 0x2 安装jsdom
### win
```
# 安装nvs、node以及node_modules(jsdom)
$ npm i jsdom -g
```
### mac
```
# 安装node
# npm i jsdom -g
```
# 配置文件
```
fuck-zhihu-unregister/conf/conf.ini

配置如下用户名、d_C0,z_c0(知乎web端可抓包获取)
配置node_modules的安装路径
[Cookies]
user_name=xxx
d_c0=xxxxxxxxx
z_c0=xxxxxxxxxxxxxxxxx

[node_modules]
path=C:\Users\sanxun\AppData\Local\nvs\node\14.15.0\x64\node_modules


```

# RUN
```
python run.py
```

# version
 * v1.0
 未加入取消关注与删除收藏夹