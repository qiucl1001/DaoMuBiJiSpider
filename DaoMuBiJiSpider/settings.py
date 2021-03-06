# -*- coding: utf-8 -*-

# Scrapy settings for DaoMuBiJiSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'DaoMuBiJiSpider'

SPIDER_MODULES = ['DaoMuBiJiSpider.spiders']
NEWSPIDER_MODULE = 'DaoMuBiJiSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'DaoMuBiJiSpider (+http://www.yourdomain.com)'

# 设置日志等级
LOG_LEVEL = "WARNING"
# 日志文件
LOG_FILE = "daoMBJ.log"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    # "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en,en-US;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "__gads=ID=7a0ab76924d7b86e:T=1586260183:S=ALNI_MY5-Hk3iwuzQqGeooOl16VARYZ8Xw",
    "Host": "www.daomubiji.com",
    "Upgrade-Insecure-Requests": "1",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    #               "Chrome/80.0.3987.132 Safari/537.36",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'DaoMuBiJiSpider.middlewares.DaomubijispiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'DaoMuBiJiSpider.middlewares.DaomubijispiderDownloaderMiddleware': 543,

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'DaoMuBiJiSpider.pipelines.SaveLocalPipeline': 300,
    'DaoMuBiJiSpider.pipelines.InsertMongoDBPipeline': 301,
    'DaoMuBiJiSpider.pipelines.AsyncInsertMySQLPipeline': 302,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# MongoDB数据库相关配置信息
MONGO_URI = "mongodb://127.0.0.1:27017"
MONGO_DB = "DaoMuBiJi"

# mysql数据库表的名称
MYSQL_TABLE = "dao_mu_bi_ji"

# 绝对路径
BASE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "daomubiji")
