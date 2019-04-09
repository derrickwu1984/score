# -*- coding: utf-8 -*-
import scrapy,logging
from lxml import etree
from scrapy.http import Request


class ScorequerySpider(scrapy.Spider):
    name = 'scorequery'
    allowed_domains = ['www1.nm.zsks.cn']
    start_urls = ['http://www1.nm.zsks.cn/']
    post_url="http://www1.nm.zsks.cn/xxcx/gkcx/lqmaxmin_18.jsp"

    def __init__(self):
        pass

    def start_requests(self):

        yield scrapy.FormRequest(url=self.post_url, method="POST", headers=self.get_headers(),
                             callback=self.parse_first, dont_filter=True)

    def get_headers(self):
        headers = {
            'referer': 'http://www.nm.zsks.cn/ptgxzs/xxcx/',
            'Host':'www1.nm.zsks.cn',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        return headers

    def pcdm_dataForm(self,pcdm):
        data={
            "m_pcdm": pcdm,
        }
        return data

    def m_kldm_dataForm(self,m_kldm,pcdm):
        data={
            "m_pcdm": pcdm,
        }
        return data

    def parse_first(self, response):
        # second_url=""
        # logging.warning(response.body.decode("gbk"))
        yield scrapy.FormRequest(url=self.post_url, method="POST",formdata=self.pcdm_dataForm("2"), headers=self.get_headers(),
                             callback=self.parse_second, dont_filter=True)
        pass

    def parse_second(self, response):
        logging.warning(response.body.decode("gbk"))