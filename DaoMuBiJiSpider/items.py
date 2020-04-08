# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomubijispiderItem(scrapy.Item):
    # MongoDB集合的名称
    collections = "dao_mu_bi_ji"

    # 集名
    name = scrapy.Field()

    # 章节数
    chapter_nums = scrapy.Field()

    # 章节所属标题
    chapter_title = scrapy.Field()

    # 章节内容
    content = scrapy.Field()



