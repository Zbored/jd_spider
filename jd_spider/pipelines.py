# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#保存到Excel中
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
#添加列标题
ws.append(['用户ID', '评价时间', '商品型号', '用户评价'])

class JdSpiderPipeline(object):
    def process_item(self, item, spider):
        #创建行对象
        line = [item['id'], item['creationTime'], item['referenceName'], item['content']]
        #写入一行
        ws.append(line)
        #保存
        wb.save('jd_spider.xlsx')
        return item