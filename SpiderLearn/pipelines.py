from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
import re


# pillow

class AoisolasPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接 yield
        for image_url in item['ImgUrl']:
            # meta里面的数据是从 spider 获取，然后通过 meta 传递给下面方法：file_path
            yield Request(image_url, meta={'item': item['name']})

    # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):
        """
        :param request: 每一个图片下载管道请求
        :param response:
        :param info:
        :return: 每套图的分类目录
        """
        # 接收上面meta传递过来的图片名称
        name = request.meta['item']

        # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
        name = re.sub(r'[？\\*|“<>:/()0123456789]', '', name)

        # 提取url前面名称作为图片名。
        image_guid = request.url.split('/')[-1]

        # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        filename = u'full/{0}/{1}'.format(name, image_guid)
        return filename

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_path
        return item
