# coding:utf-8
import sys
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# https://npm.taobao.org/mirrors/chromedriver/
executable_path = r'E:\\Code\\python-workspace\\chromedriver-v86.exe' if (
        sys.platform == 'win32') else r'/Users/taohua/works/Python/chromedriver'

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)

video_url = 'https://www.insiji.com/index.php/vod/play/id/177541/sid/1/nid/1.html'
driver.get(video_url)

driver.maximize_window()
# driver.minimize_window()

iframe = driver.find_element_by_id('fed-play-iframe')
driver.switch_to.frame(iframe)

page_source = driver.page_source

if page_source is not None:
    # https://v4.szjal.cn/20200624/mbefQ1sQ/index.m3u8
    # regular = re.compile(r'[a-zA-Z]+://[^\s]*.m3u8')
    # print(re.findall(regular, page_source))
    root = 'E:\\Code\\python-workspace\\spider-learn\\MooseSpider\\html\\'
    with open(root + "1.html", 'w') as f:
        f.write(page_source)
