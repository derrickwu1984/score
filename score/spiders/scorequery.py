# -*- coding: utf-8 -*-
import scrapy,logging
from lxml import etree
from scrapy.http import Request


class ScorequerySpider(scrapy.Spider):
    name = 'scorequery'
    allowed_domains = ['www1.nm.zsks.cn']
    start_urls = ['http://www1.nm.zsks.cn/']
    post_url="http://www1.nm.zsks.cn/xxcx/gkcx/lqmaxmin_18.jsp"
    refer = "http://www.nm.zsks.cn/ptgxzs/xxcx/"
    host="www1.nm.zsks.cn"
    user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"

    def __init__(self):
        pass

    def start_requests(self):

        yield scrapy.FormRequest(url=self.post_url, method="POST", headers=self.get_headers(),
                             callback=self.parse_first, dont_filter=True)

    def get_headers(self):
        headers = {
            'referer': self.refer,
            'Host':self.host,
            'User-Agent':self.user_agent
        }
        return headers



    def parse_first(self, response):
        # second_url=""
        # logging.warning(response.body.decode("gbk"))
        # html=etree.HTML(response.body.decode("gbk"))
        # m_pcdm=html.xpath("//option/@value")
        # for i in range(len(m_pcdm)):
        #
        #     yield scrapy.FormRequest(url=self.post_url, method="POST",formdata=self.pcdm_dataForm(m_pcdm[i]), headers=self.get_headers(),
        #                      callback=self.parse_second, dont_filter=True,meta={"m_pcdm":m_pcdm[i]})
        yield scrapy.FormRequest(url=self.post_url, method="POST", formdata=self.pcdm_dataForm("1"),
                                 headers=self.get_headers(), callback=self.parse_second, dont_filter=True)

    def parse_second(self, response):
        # logging.warning(response.meta["m_pcdm"])
        # logging.warning(response.body.decode("gbk"))
        # m_pcdm=response.meta["m_pcdm"]
        # html=etree.HTML(response.body.decode("gbk"))
        # options_temp=html.xpath("//form[@name='form2']/select/option/@value")
        # 去除options中的重复项
        # m_kldm=list(set(options_temp))
        # for i in range(len(m_kldm)):
        #     yield scrapy.FormRequest(url=self.post_url, method="POST", formdata=self.m_kldm_dataForm("m_kldm[i],m_pcdm),
        #                          headers=self.get_headers(), callback=self.parse_third, dont_filter=True,
        #                          meta={"m_pcdm":m_pcdm,"m_kldm":m_kldm[i]})
        yield scrapy.FormRequest(url=self.post_url, method="POST", formdata=self.m_kldm_dataForm("@","1"),
                                 headers=self.get_headers(), callback=self.parse_third, dont_filter=True,
                                 )

        pass

    def parse_third(self,response):
        # logging.warning(response.body.decode("gbk"))
        # m_pcdm = response.meta["m_pcdm"]
        # m_kldm = response.meta["m_kldm"]
        # html=etree.HTML(response.body.decode("gbk"))
        # m_pxfs=html.xpath("//form[@name='form4']/select/option/@value")
        # for i in range(len(m_pxfs)):
            # yield scrapy.FormRequest(url=self.post_url, method="POST", formdata=self.m_pxfs_dataForm(m_kldm,m_pcdm,m_pxfs[i]),
        #                          headers=self.get_headers(), callback=self.parse_forth, dont_filter=True,
        #                          meta={"m_pcdm":m_pcdm,"m_kldm":m_kldm,"m_pxfs":m_pxfs[i]})
        yield scrapy.FormRequest(url=self.post_url, method="POST", formdata=self.m_pxfs_dataForm("@","1","1"),
                                 headers=self.get_headers(), callback=self.parse_forth, dont_filter=True,
                                 )
        pass

    def parse_forth(self, response):
        # logging.warning(response.body.decode("gbk"))
        # m_pcdm = response.meta["m_pcdm"]
        # m_kldm = response.meta["m_kldm"]
        # m_pxfs = response.meta["m_pxfs"]
        # html=etree.HTML(response.body.decode("gbk"))
        # m_yxdh=html.xpath("//form[@name='form3']/select/option/@value")
        # for i in range(len(m_yxdh)):
            # yield scrapy.FormRequest(url=self.post_url, method="POST", formdata=self.m_yxdh_dataForm(m_kldm,m_pcdm,m_pxfs,m_yxdh[i]),
        #                          headers=self.get_headers(), callback=self.parse_forth, dont_filter=True,
        #                          meta={"m_pcdm":m_pcdm,"m_kldm":m_kldm,"m_pxfs":m_pxfs,"m_yxdh":m_yxdh[i]})
        yield scrapy.FormRequest(url=self.post_url, method="POST", formdata=self.m_yxdh_dataForm("@","1","1","018","提交"),
                                 headers=self.get_headers(), callback=self.parse_fifth, dont_filter=True,
                                 )
    def parse_fifth(self, response):
        logging.warning(response.body.decode("gbk"))
        html = etree.HTML(response.body.decode("gbk"))
        # 批次
        order_seq =html.xpath("//font[3]/text()")[0].strip()
        # 科类
        item_class = html.xpath("//font[3]/text()")[1].strip()
        # 院校名称
        school_name = html.xpath("//font[3]/text()")[2].strip()
        # 填报次序
        write_order = html.xpath("//table[1]/tr[2]/td/p/text()")[0]
        # 最高分
        max_score= html.xpath("//table[1]/tr[2]/td/p/text()")[1]
        # 最低分
        min_score = html.xpath("//table[1]/tr[2]/td/p/text()")[2]
        # 录取人数
        enroollment_no = html.xpath("//table[1]/tr[2]/td/p/text()")[3]
        # 专业代号
        pro_code = html.xpath("//table[2]/tr[2]/td/p/text()")[0]
        # 专业名称
        pro_name = html.xpath("//table[2]/tr/td/p/text()")[1]
        # 填报次序
        write_order_detail= html.xpath("//table[2]/tr[2]/td/p/text()")[1]
        # 最高分
        pro_max_score = html.xpath("//table[2]/tr[2]/td/p/text()")[2]
        # 最低分
        pro_min_score=""
        # 最低分位次
        min_score_order=""
        #录取人数
        enroollment_no_detail=""
        pass
    # 报文格式
    # 第一次下拉请求
    def pcdm_dataForm(self,pcdm):
        data={
            "m_pcdm": pcdm,
        }
        return data
    # 第二次下拉请求
    def m_kldm_dataForm(self,m_kldm,pcdm):
        data={
            "pcdm": pcdm,
            "m_kldm":m_kldm
        }
        return data
    # 第三次下拉请求
    def m_pxfs_dataForm(self,kldm,pcdm,m_pxfs):
        data={
            "pcdm": pcdm,
            "kldm":kldm,
            "m_pxfs":m_pxfs
        }
        return data
    # 第四次下拉请求
    def m_yxdh_dataForm(self,kldm,pcdm,m_pxfs,m_yxdh,query):
        data={
            "pcdm": pcdm,
            "kldm":kldm,
            "pxfs":m_pxfs,
            "m_yxdh":m_yxdh,
            "query":query
        }
        return data