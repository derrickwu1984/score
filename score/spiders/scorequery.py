# -*- coding: utf-8 -*-
import scrapy,logging,string
from lxml import etree
from scrapy.http import Request
from scrapy.loader import  ItemLoader

from score.items import ScoreItem
class ScorequerySpider(scrapy.Spider):
    name = 'scorequery'
    allowed_domains = ['www1.nm.zsks.cn']
    start_urls = ['http://www1.nm.zsks.cn/']
    post_url="http://www1.nm.zsks.cn/xxcx/gkcx/lqmaxmin_18.jsp"
    refer = "http://www.nm.zsks.cn/ptgxzs/xxcx/"
    host="www1.nm.zsks.cn"
    user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    count = 0
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

    def parse_first(self,response):
        params_list = self.get_dict_loop()
        for i in range(len(params_list)):
            m_pcdm = params_list[i][0]
            m_kldm = params_list[i][1]
            m_pxfs = params_list[i][2]
            yield scrapy.FormRequest(url=self.post_url, method="POST", formdata=self.m_pxfs_dataForm(m_kldm,m_pcdm,m_pxfs),
                                 headers=self.get_headers(), callback=self.parse_second, dont_filter=True,
                                 meta={"m_pcdm":m_pcdm,"m_kldm":m_kldm,"m_pxfs":m_pxfs})
        # yield scrapy.FormRequest(url=self.post_url, method="POST", formdata=self.m_pxfs_dataForm("@","1","1"),
        #                          headers=self.get_headers(), callback=self.parse_forth, dont_filter=True,
        #                          )
    def parse_second(self, response):
        # logging.warning(response.body.decode("gbk"))
        m_pcdm = response.meta["m_pcdm"]
        m_kldm = response.meta["m_kldm"]
        m_pxfs = response.meta["m_pxfs"]
        html=etree.HTML(response.body.decode("gbk"))
        m_yxdh=html.xpath("//form[@name='form3']/select/option/@value")
        param_dict_temp=[]
        param_dict = []
        for i in range(len(m_yxdh)):
            param_dict_temp=[m_pcdm,m_kldm,m_pxfs,m_yxdh[i]]
            param_dict.append(param_dict_temp)
        # count_temp = len(param_dict)
        # self.count+=count_temp
        for i in range(len(param_dict)):
            pcdm = param_dict[i][0]
            kldm = param_dict[i][1]
            pxfs = param_dict[i][2]
            yxdh = param_dict[i][3]
            yield scrapy.FormRequest(url=self.post_url, method="POST", formdata=self.m_yxdh_dataForm(kldm,pcdm,pxfs,yxdh,"提交"),
                                 headers=self.get_headers(), callback=self.parse_third, dont_filter=True,
                                 meta={"m_pcdm":pcdm,"m_kldm":kldm,"m_pxfs":pxfs,"m_yxdh":yxdh})
        # yield scrapy.FormRequest(url=self.post_url, method="POST", formdata=self.m_yxdh_dataForm("@","1","1","018","提交"),
        #                          headers=self.get_headers(), callback=self.parse_fifth, dont_filter=True,
        #                          )
    def parse_third(self, response):
        # logging.warning(response.body.decode("gbk"))
        html=etree.HTML(response.body.decode("gbk"))
        kldm = html.xpath("//input[@name='kldm']/@value")[1]
        # 科类标识集合：只有kldm=普通文科 A、普通理科 B、蒙授文科 C 、蒙授理科 D table2中的最低分位数才有值
        kldm_in = ['A', 'B', 'C', 'D']
        # 批次
        try :
            order_seq = html.xpath(".//font[2]/text()")[0].strip()
        except:
            # order_seq = html.xpath(".//font[3]/text()")[0].strip()
            order_seq = ""
        # 科类
        try:
            item_subject = html.xpath(".//font[2]/text()")[1].strip()
        except:
            # item_subject = html.xpath(".//font[3]/text()")[1].strip()
            item_subject = ""
        # 批次
        try:
            school_name = html.xpath(".//font[2]/text()")[2].strip()
        except:
            # school_name = html.xpath(".//font[3]/text()")[2].strip()
            school_name = ""
        # table1 tr 下的td值 每个td生成一个list
        table1_result = html.xpath("//table[1]/tr[position()>1]")
        table1_result_len = len(table1_result)
        scoreItemItemLoader = ItemLoader(item=ScoreItem(), response=response)
        scoreItemItemLoader.add_value("order_seq",order_seq)
        scoreItemItemLoader.add_value("item_subject", item_subject)
        scoreItemItemLoader.add_value("school_name", school_name)
        for i in range(table1_result_len):
            # print(table1_result[i].xpath("./td/p/text()"))
            #     填报次序
            fill_order = table1_result[i].xpath("./td/p/text()")[0]
            # 最高分
            max_score = table1_result[i].xpath("./td/p/text()")[1]
            # 最低分
            min_score = table1_result[i].xpath("./td/p/text()")[2]
            # 录取人数
            enroll_no = table1_result[i].xpath("./td/p/text()")[3]

            scoreItemItemLoader.add_value("fill_order",fill_order)
            scoreItemItemLoader.add_value("max_score", max_score)
            scoreItemItemLoader.add_value("min_score", min_score)
            scoreItemItemLoader.add_value("enroll_no", enroll_no)

        # table2 tr 下的td值 每个td生成一个list
        table2_result = html.xpath("//table[2]/tr[position()>1]")
        # logging.warning(html.xpath("//table[2]/tr[position()>1]/td/p/text()"))
        table2_result_len = len(table2_result)
        for i in range(table2_result_len):
            # tables中每个从tr抽取出来的list的长度
            table2_tr_result_len = len(table2_result[i].xpath("./td/p/text()"))
            # 科类属于 普通文科 A、普通理科 B、蒙授文科 C 、蒙授理科 D 则有六项指标
            if kldm in kldm_in:
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
            # logging.warning(pro_code)
            # logging.warning(fill_order_table2)
            # logging.warning(max_score_table2)
            # logging.warning(min_score_table2)
            # logging.warning(min_score_order)
            # logging.warning(enroll_no_table2)
            scoreItemItemLoader.add_value("pro_code", pro_code)
            scoreItemItemLoader.add_value("fill_order_table2", fill_order_table2)
            scoreItemItemLoader.add_value("max_score_table2", max_score_table2)
            scoreItemItemLoader.add_value("min_score_table2", min_score_table2)
            scoreItemItemLoader.add_value("min_score_order", min_score_order)
            scoreItemItemLoader.add_value("enroll_no_table2", enroll_no_table2)
        # 获取tables中的专业名称
        pro_name_result = html.xpath("//table[2]/tr[position()>1]")
        pro_name_result_len = len(pro_name_result)
        for i in range(pro_name_result_len):
            pro_name = pro_name_result[i].xpath("./td/p/a/text()")
            scoreItemItemLoader.add_value("pro_name", pro_name)
            pass
        scoreItem = scoreItemItemLoader.load_item()

        yield scoreItem

    def get_dict_loop(self):
        # 批次字典：order_seq_dict
        # order_seq_dict = ['1', '2', '3', '4', '6', '7', 'C', 'E']
        order_seq_dict = ['1', '2']
        # 拿到大小写字母
        letter_list = string.ascii_letters
        # 拿到大写字母
        uppser_letter_str = letter_list[26:]
        uppser_str = " ".join(uppser_letter_str)
        item_class_dict = []
        # 科类字典：item_class_dict
        # item_class_dict = uppser_str.split(" ")
        # item_class_dict.insert(26, '@')
        # item_class_dict.insert(27, '0')
        # item_class_dict.insert(28, '1')
        item_class_dict=['A','B']
        # 院校排序方式字典
        school_type = ['1', '2']
        list = []
        list_temp = []
        for i in range(len(order_seq_dict)):
            for j in range(len(item_class_dict)):
                for k in range(len(school_type)):
                    list_temp = [order_seq_dict[i], item_class_dict[j], school_type[k]]
                    list.append(list_temp)
        # logging.warning(list)
        # logging.warning(len(list))
        return list

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