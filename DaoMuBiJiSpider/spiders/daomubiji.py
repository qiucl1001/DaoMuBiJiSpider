# -*- coding: utf-8 -*-
import scrapy
from DaoMuBiJiSpider.items import DaomubijispiderItem


class DaomubijiSpider(scrapy.Spider):
    name = 'daomubiji'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']  # "http://seputu.com/"

    def parse(self, response):
        """
        提取盗墓笔记全集的url地址
        :param response: 盗墓笔记全集所在的网页源代码
        :return:
        """
        fiction_urls = response.xpath('//article[@class="article-content"]/p/a/@href').extract()

        for fiction_url in fiction_urls:
            yield scrapy.Request(
                url=fiction_url,
                callback=self.parse_chapter
            )

    def parse_chapter(self, response):
        """
        提取盗墓笔记每集中的相关数据信息
        :param response: 每集网页源代码
        :return:
        """
        # 每集中所有章节
        articles = response.xpath('//article')
        for article in articles:
            item = DaomubijispiderItem()
            chapter_detail_url = article.xpath('./a/@href').extract_first()
            infos = article.xpath('./a/text()').extract_first().split()
            if 3 == len(infos):
                item["name"] = infos[0]
                item["chapter_nums"] = infos[1]
                item["chapter_title"] = infos[2]
            else:
                item["name"] = infos[0]
                item["chapter_title"] = infos[1]
                item["chapter_nums"] = ''

            yield scrapy.Request(
                url=chapter_detail_url,
                callback=self.parse_detail_chapter,
                meta={"item": item}
            )

    @staticmethod
    def parse_detail_chapter(response):
        """
        获取章节详情内容数据
        :param response: 详情页源代码
        :return:
        """
        item = response.meta.get("item")

        contents = response.xpath('//article[@class="article-content"]/p/text()').extract()
        item["content"] = "\r\n".join(list(map(lambda x: x.replace("\u3000|\n|\n    \t\t\t", "").strip(), contents)))

        yield item


