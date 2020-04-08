# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)


class Config(object):
    """app配置相关信息类"""

    # SQLAlchemy相关配置选项
    # 设置连接数据库的URL
    # 注意：district_code数据库要事先手动创建
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:qcl123@127.0.0.1:3306/daomubiji'

    # 动态跟踪配置
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)


# 创建一个SQLAlchemy数据库连接对象
db = SQLAlchemy(app)

# 创建flask脚本管理工具对象
manager = Manager(app)

# 创建数据库迁移工具对象
Migrate(app, db)

# 向manager对象中添加数据库操作命令
manager.add_command("db", MigrateCommand)


class DaoMuBiJi(db.Model):
    """定义一个用来存储盗墓笔记小说的mysql数据表"""
    # 定义表名
    __tblname__ = "dao_mu_bi_ji"

    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))  # 集名
    chapter_nums = db.Column(db.String(64))  # 章节数
    chapter_title = db.Column(db.String(64))  # 章节所属标题
    content = db.Column(db.Text)  # 章节内容

    def __str__(self):
        return 'DaoMuBiJi:%s' % self.name


if __name__ == '__main__':
    manager.run()


