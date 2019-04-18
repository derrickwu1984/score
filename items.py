# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScoreItem(scrapy.Item):
    pcdm = scrapy.Field()
    kldm = scrapy.Field()
    pxfs = scrapy.Field()
    yxdh = scrapy.Field()

    order_seq = scrapy.Field()
    item_subject = scrapy.Field()
    school_name = scrapy.Field()

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

    # fill= scrapy.Field()
    # max= scrapy.Field()
    # min= scrapy.Field()
    # enroll= scrapy.Field()
    pass
