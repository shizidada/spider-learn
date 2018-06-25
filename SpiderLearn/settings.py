# -*- coding: utf-8 -*-

# Scrapy settings for SpiderLearn project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'SpiderLearn'

SPIDER_MODULES = ['SpiderLearn.spiders']
NEWSPIDER_MODULE = 'SpiderLearn.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'SpiderLearn (+http://www.yourdomain.com)'

# 这个文件中规定了本站点允许的爬虫机器爬取的范围，因为默认 scrapy 遵守 robot 协议
# 会先请求这个文件查看自己的权限，出错是因为使用的爬虫爬取内容违背这个 robot.txt
# 所以只要让爬虫不遵守该协议就好了，具体做法是找到settings文件里的ROBOTSTXT_OBEY设置成False
# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# 配置当前请求处理最大数
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

# 中间件 越小优先级越高
# Enable or disable spider middlewares
# SPIDER_MIDDLEWARES = {
#    'SpiderLearn.middlewares.SpiderLearnMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'SpiderLearn.middlewares.AoisolasMiddleware': 1,
}

# 插件
# Enable or disable extensions
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# pipelines 处理数据
# Configure item pipelines
# 设置图片存储路径
IMAGES_STORE = 'D:\meizi'

# 启动pipeline中间件
ITEM_PIPELINES = {
    'SpiderLearn.pipelines.AoisolasPipeline': 300,
}

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
