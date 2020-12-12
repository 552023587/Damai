# Damai
大麦购票(仅供学习使用)
# 准备
目前只支持Firefox浏览器
## 依赖庫
- selenium 
- configparser
# 快速开始
**获取cookie**
```
python login.py
```
运行后30秒内点击登录选择任何一种登录方式，推荐扫码，不然可能出现验证码失败的情况

**开启购票**

```
python main.py
```

**配置**
```
[APP]
#购票目标地址
url=https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.2cca2ecbNzwz46&id=632432584423
#购买数量，购买前填写好购票人，配送地址
buyNum=1
#场次
date=1
#票档
sku=1
#开启后台运行，不推荐开启 0关闭 1开启
backend=1
#失败重试 0关闭 1开启
retry=0
```

