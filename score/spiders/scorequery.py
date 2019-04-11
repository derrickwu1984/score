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
        html=etree.HTML(response.body.decode("gbk"))
        kldm = html.xpath("//input[@name='kldm']/@value")[1]
        # 科类标识集合：只有kldm=普通文科 A、普通理科 B、蒙授文科 C 、蒙授理科 D table2中的最低分位数才有值
        kldm_in = ['A', 'B', 'C', 'D']
        # table1 tr 下的td值 每个td生成一个list
        table1_result = html.xpath("//table[1]/tr[position()>1]")
        table1_result_len = len(table1_result)
        for i in range(table1_result_len):
            # print(table1_result[i].xpath("./td/p/text()"))
            #     填报次序
            fill_order = table1_result[i][0]
            # 最高分
            max_score = table1_result[i][1]
            # 最低分
            min_score = table1_result[i][2]
            # 录取人数
            enroll_no = table1_result[i][3]
        # table2 tr 下的td值 每个td生成一个list
        table2_result = html.xpath("//table[2]/tr[position()>1]")
        logging.warning(html.xpath("//table[2]/tr[position()>1]/td/p/text()"))
        table2_result_len = len(table2_result)
        for i in range(table2_result_len):
            # tables中每个从tr抽取出来的list的长度
            table2_tr_result_len = len(table2_result[i].xpath("./td/p/text()"))
            # 科类属于 普通文科 A、普通理科 B、蒙授文科 C 、蒙授理科 D 则有六项指标
            if kldm in kldm_in:
                logging.warning("6")
                # 如有list中只有五项指标，说明缺少"专业代码",那么给专业代码赋值为空
                if (table2_tr_result_len == 5):
                    pro_code = ""
                    fill_order_table2 = table2_result[i].xpath("./td/p/text()")[0]
                    max_score_table2 = table2_result[i].xpath("./td/p/text()")[1]
                    min_score_table2 = table2_result[i].xpath("./td/p/text()")[2]
                    # 最低分位数
                    min_score_order = table2_result[i].xpath("./td/p/text()")[3]
                    enroll_no_table2 = table2_result[i].xpath("./td/p/text()")[4]

                else:
                    pro_code = table2_result[i].xpath("./td/p/text()")[0]
                    fill_order_table2 = table2_result[i].xpath("./td/p/text()")[1]
                    max_score_table2 = table2_result[i].xpath("./td/p/text()")[2]
                    min_score_table2 = table2_result[i].xpath("./td/p/text()")[3]
                    # 最低分位数
                    min_score_order = table2_result[i].xpath("./td/p/text()")[4]
                    enroll_no_table2 = table2_result[i].xpath("./td/p/text()")[5]
            # 艺术科类返回5项指标
            else:
                # logging.warning(table2_result[i].xpath("./td/p/text()"))
                # logging.warning(table2_tr_result_len)
                # 如有list中只有四项指标，说明缺少"专业代码",那么给专业代码赋值为空
                # 最低分位数也赋值为空
                # logging.warning(table2_result[i].xpath("./td/p/text()"))
                # logging.warning(len(table2_result[i]))
                if (table2_tr_result_len == 4):
                    pro_code = ""
                    fill_order_table2 = table2_result[i].xpath("./td/p/text()")[0]
                    max_score_table2 = table2_result[i].xpath("./td/p/text()")[1]
                    min_score_table2 = table2_result[i].xpath("./td/p/text()")[2]
                    # 最低分位数
                    min_score_order = ""
                    enroll_no_table2 = table2_result[i].xpath("./td/p/text()")[3]
                else:
                    pro_code = table2_result[i].xpath("./td/p/text()")[0]
                    fill_order_table2 = table2_result[i].xpath("./td/p/text()")[1]
                    max_score_table2 = table2_result[i].xpath("./td/p/text()")[2]
                    min_score_table2 = table2_result[i].xpath("./td/p/text()")[3]
                    # 最低分位数
                    min_score_order = ""
                    enroll_no_table2 = table2_result[i].xpath("./td/p/text()")[4]
            logging.warning(pro_code)
            logging.warning(fill_order_table2)
            logging.warning(max_score_table2)
            logging.warning(min_score_table2)
            logging.warning(min_score_order)
            logging.warning(enroll_no_table2)
        # 获取tables中的专业名称
        pro_name_result = html.xpath("//table[2]/tr[position()>1]")
        pro_name_result_len = len(pro_name_result)
        for i in range(pro_name_result_len):
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