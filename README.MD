# DaoMuBiJiSpider
----->使用scrapy框架抓取盗墓笔记小说<url: [http://www.daomubiji.com/]>


备注：
* 演示了log日志文件的管理维护
* 演示了通过下载器中间件设置User-Agent池
* 演示了将小说整体内容分集分章节自动化存储到本地
* 演示了将小说整体内容存储到MongoDB数据库中
* 演示了将小说整体内容以异步的方式写入MySQL数据库中


## 安装

### 安装Python3.7.2以上版本

### 安装MySQL数据库
在宿主机安装好之后开启MySQL数据库

### 安装MongoDB数据库
在宿主机安装好之后开启MongoDB数据库

###安装三方依赖库

```
cd DaoMuBiJiSpider
pip3 install -r requirements.txt
```

## 配置 DaoMuBiJiSpider
### 打开 models.py 配置mysql数据库连接
```
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://数据库用户名:数据库连接密码@数据库所在宿主机ip:3306/数据库名称'
e.g.
 SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:qcl123@127.0.0.1:3306/daomubiji'
 
```
### 手动创建数据库
```
mysql -u数据库用户名 -p数据库连接密码

mysql> create database daomubiji default charset="utf8";

```
### 创建迁移仓库
#### 这个命令会创建migrations文件夹，所有迁移文件都放在里面。
```
python models.py db init
```
### 创建迁移脚本
#### 创建自动迁移脚本
```
python models.py db migrate -m 'initial migration'
```

### 更新数据库
```
python models.py db upgrade
```

## 启动程序
```
1. python start.py
2. scrapy scawl daomubiji

```