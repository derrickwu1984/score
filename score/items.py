# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScoreItem(scrapy.Item):
    # define the fields for your item here like:
    fill_order = scrapy.Field()
    max_score = scrapy.Field()
    min_score = scrapy.Field()
    enroll_no = scrapy.Field()

    pro_code = scrapy.Field()
    fill_order_table2 = scrapy.Field()
    max_score_table2 = scrapy.Field()
    min_score_table2 = scrapy.Field()
    min_score_order = scrapy.Field()
    enroll_no_table2 = scrapy.Field()

    pro_name = scrapy.Field()
    pass
