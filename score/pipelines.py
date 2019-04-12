# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook  # 写入Excel表所用
from openpyxl import load_workbook

class ScorePipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['批次', '科类', '院校名称', '填报次序', '最高分', '最低分', '录取人数',
                        '专业代号', '专业名称', '填报次序', '延期有效期',
                        '最高分', '最低分', '最低分位数','录取人数'])

    def process_item(self, item, spider):
        a = item['cert_no'][0]
        line = [item['cert_no'][0], item['corp_name'][0], item['corp_repr'][0], item['admi_code'][0],
                item['regi_addr'][0], item['econ_type'][0], item['prom_rang'][0], item['prom_cell'][0],
                item['chek_date'][0], item['last_chek'][0], item['post_chek'][0]]
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('C:\\Users\\Administrator\\Desktop\\nm.xls')  # 保存xlsx文件
        return item
