# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import logging
import pymongo
import pymysql
from twisted.enterprise import adbapi


class SaveLocalPipeline(object):
    """将盗墓笔记保存到本地文件中"""

    def __init__(self, base_path):
        self.base_path = base_path

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            base_path=crawler.settings.get("BASE_PATH")
        )

    def process_item(self, item, spider):
        filename_path = os.path.join(self.base_path, item["name"])
        if not os.path.exists(filename_path):
            os.makedirs(filename_path)
        if 4 == len(item):
            chapter_path = os.path.join(filename_path, "{}_{}.txt".format(item["chapter_nums"], item["chapter_title"]))
        else:
            chapter_path = os.path.join(filename_path, "{}.txt".format(item["chapter_title"]))

        with open(chapter_path, "w", encoding="utf-8") as f:
            f.write(item["content"])

        return item


class InsertMongoDBPipeline(object):
    """将盗墓笔记保存到mongodb数据库"""

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DB")
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[item.collections].insert_one(dict(item))

        return item

    def close_spider(self, spider):
        self.client.close()


class AsyncInsertMySQLPipeline(object):
    """将盗墓笔记保存以异步方式写入到mysql数据库"""

    def __init__(self, table):
        data_params = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "qcl123",
            "database": "daomubiji",
            "charset": "utf8",
            "cursorclass": pymysql.cursors.DictCursor
        }
        self.logger = logging.getLogger(__name__)
        self.db_pool = adbapi.ConnectionPool("pymysql", **data_params)
        self._sql = None

        self.table = table

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            table=crawler.settings.get("MYSQL_TABLE")
        )

    def process_item(self, item, spider):
        defer = self.db_pool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error, item, spider)

    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (item["name"], item["chapter_nums"], item["chapter_title"], item["content"]))

    def handle_error(self, error, item, spider):
        self.logger.warning(error)

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into {}(id, name, chapter_nums, chapter_title, content) values(null, %s, %s, %s, %s);
            """.format(self.table)
            return self._sql
        return self._sql




