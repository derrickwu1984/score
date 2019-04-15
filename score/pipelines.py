# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
from openpyxl import Workbook  # 写入Excel表所用
from openpyxl import load_workbook



class ScorePipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active

        # self.ws.append(['批次', '科类', '院校名称', '填报次序', '最高分', '最低分', '录取人数',
        #                 '专业代号', '专业名称', '填报次序', '延期有效期',
        #                 '最高分', '最低分', '最低分位数','录取人数'])
        self.ws.append(['选择批次','选择科类','院校排序方式','选择院校',
                        '专业代码', '专业名称',
                        '填报次序表2', '最高分表2', '最低分表2', '最低分位数'])

    def process_item(self, item, spider):
        line = []
        for i in range(len(item['fill_order_table2'])):
            line = [ str(item['pcdm'][i]),str(item['kldm'][i]), str(item['pxfs'][i]),
                     str(item['yxdh'][i]),
                     str(item['pro_code'][i]),str(item['pro_name'][i]),
                     str(item['fill_order_table2'][i]),str(item['max_score_table2'][i]), str(item['min_score_table2'][i]),
                     str(item['min_score_order'][i])]

        # line = [item['order_seq'][0], item['item_subject'][0], item['school_name'][0], item['fill_order'][0],
        #         item['max_score'][0], item['min_score'][0], item['enroll_no'][0]]
            self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('D:\\nm.xlsx')  # 保存xlsx文件
        return item

    def __str__(self):
        return ""
