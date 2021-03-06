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
        dict_pcdm={'1':'本科提前A','2':'本科提前B','3':'本科一批','4':'本科二批','6':'专科提前','7':'高职高专','C':'本科一批B','E':'本科二批B'}
        dict_kldm = {'@': '汉授编导', '0': '体育类', '1': '采矿类', 'A': '普通文科', 'B': '普通理科', 'C': '蒙授文科', 'D': '蒙授理科',
                     'E': '汉授美术','F': '蒙授美术','G': '汉授音乐','H': '蒙授音乐','I': '其他艺术',
                     'J': '蒙授其他艺术','K': '汉授体育','L': '蒙授体育','M': '计算机类',
                     'N': '农学类', 'O': '牧医类', 'P': '烹饪类', 'Q': '财会类',
                     'R': '美工设计类', 'S': '旅游类', 'T': '汽驾类', 'U': '建筑类',
                     'V': '机电类', 'W': '蒙牧医类', 'X': '化工类', 'Y': '幼师类', 'Z': '医学类'}
        dict_pxfs = {'1':'院校代号','2':'院校名称'}
        pcdm = dict_pcdm[response.meta['m_pcdm']]
        kldm_dict_value = dict_kldm[response.meta['m_kldm']]
        pxfs = dict_pxfs[response.meta['m_pxfs']]
        yxdh = response.meta['m_yxdh']
        # logging.warning(pcdm)
        # logging.warning(kldm_dict_value)
        # logging.warning(pxfs)
        # logging.warning(yxdh)
        html=etree.HTML(response.body.decode("gbk"))
        kldm = html.xpath("//input[@name='kldm']/@value")[1]
        # 科类标识集合：只有kldm in
        # 采矿类,普通文科,普通理科,蒙授文科,蒙授理科,计算机类,农学类,牧医类,财会类,
        # 美工设计类,旅游类,汽驾类,建筑类,机电类,蒙牧医类,化工类,幼师类,医学类
        # table2中的最低分位数才有值
        kldm_in = ['0','1','A', 'B', 'C', 'D', 'M', 'N', 'O', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
        # 批次
        if ('（注意：艺术以综合分排序录取，本处文化课排名仅供参考。）' == html.xpath(".//font[2]/text()")[0].strip()):
            order_seq = html.xpath(".//font[3]/text()")[0].strip()
            item_subject = html.xpath(".//font[3]/text()")[1].strip()
            school_name = html.xpath(".//font[3]/text()")[2].strip()
        else:
            try :
                order_seq = html.xpath(".//font[2]/text()")[0].strip()
                item_subject = html.xpath(".//font[2]/text()")[1].strip()
                school_name = html.xpath(".//font[2]/text()")[2].strip()
            except:

                order_seq = ""
                item_subject=""
                school_name=""
        # table1 tr 下的td值 每个td生成一个list
        if item_subject !="":
            table1_result = html.xpath("//table[1]/tr[position()>1]")
            table1_result_len = len(table1_result)
            # N条记录公用一个pro_code/pro_name时，pro_code、pro_name 存在数据的索引地址
            parent_index = table1_result_len - 1
            scoreItemItemLoader = ItemLoader(item=ScoreItem(), response=response)
            scoreItemItemLoader.add_value("order_seq",order_seq)
            scoreItemItemLoader.add_value("item_subject", item_subject)
            scoreItemItemLoader.add_value("school_name", school_name)
            for i in range(table1_result_len):
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
                scoreItemItemLoader.add_value("min_score",min_score)
                scoreItemItemLoader.add_value("enroll_no", enroll_no)

            # table2 tr 下的td值 每个td生成一个list
            table2_result = html.xpath("//table[2]/tr[position()>1]")
            table2_result_len = len(table2_result)
            for i in range(table2_result_len):
                # tables中每个从tr抽取出来的list的长度
                table2_tr_result_len = len(table2_result[i].xpath("./td/p/text()"))
                # 科类属于非艺术类则有六项指标
                if kldm in kldm_in:
                    # 如有list中只有五项指标，说明缺少"专业代码","专业名称"
                    if (table2_tr_result_len == 5):
                        tr=""
                        tr_1=""
                        tr_2 = ""
                        tr_3 = ""
                        tr_4 = ""
                        tr_5 = ""
                        if i==1:
                            tr = table2_result[i].xpath("./td/p/text()")
                            tr_1 = table2_result[i-1].xpath("./td/p/text()")
                        if i>1:
                            tr = table2_result[i].xpath("./td/p/text()")
                            tr_1 = table2_result[i - 1].xpath("./td/p/text()")
                            tr_2 =table2_result[i-2].xpath("./td/p/text()")
                        if i>2:
                            tr_3 = table2_result[i-3].xpath("./td/p/text()")
                        if i>3:
                            tr_4 = table2_result[i-4].xpath("./td/p/text()")
                        if i>4:
                            tr_5 = table2_result[i-5].xpath("./td/p/text()")
                        idx = self.locate_index(tr,tr_1,tr_2,tr_3,tr_4,tr_5,5)
                        logging.warning("-----------")
                        logging.warning(pcdm)
                        logging.warning(kldm_dict_value)
                        logging.warning(pxfs)
                        logging.warning(yxdh)
                        logging.warning(tr)
                        logging.warning(tr_1)
                        logging.warning(table2_tr_result_len)
                        logging.warning(i)
                        logging.warning(idx)
                        pro_code = table2_result[i - idx].xpath("./td/p/text()")[0]
                        pro_name = table2_result[i - idx].xpath("./td/p/a/text()")[0]
                        fill_order_table2 = table2_result[i].xpath("./td/p/text()")[0]
                        max_score_table2 = table2_result[i].xpath("./td/p/text()")[1]
                        min_score_table2 = table2_result[i].xpath("./td/p/text()")[2]
                        # 最低分位数
                        min_score_order = table2_result[i].xpath("./td/p/text()")[3]
                        enroll_no_table2 = table2_result[i].xpath("./td/p/text()")[4]
                    else:
                        logging.warning("================")
                        pro_code = table2_result[i].xpath("./td/p/text()")[0]
                        pro_name = table2_result[i].xpath("./td/p/a/text()")[0]
                        fill_order_table2 = table2_result[i].xpath("./td/p/text()")[1]
                        max_score_table2 = table2_result[i].xpath("./td/p/text()")[2]
                        min_score_table2 = table2_result[i].xpath("./td/p/text()")[3]
                        # 最低分位数
                        min_score_order = table2_result[i].xpath("./td/p/text()")[4]
                        enroll_no_table2 = table2_result[i].xpath("./td/p/text()")[5]
                # 艺术科类没有最低分位数
                else:
                    # 如有list中只有四项指标，说明缺少"专业代码","专业名称"
                    # 需要调用locate_index，复用有i-idx 索引项的"专业代码","专业名称"
                    # 最低分位数赋值为空
                    if (table2_tr_result_len == 4):
                        tr=""
                        tr_1=""
                        tr_2 = ""
                        tr_3 = ""
                        tr_4 = ""
                        tr_5 = ""
                        if i==1:
                            tr = table2_result[i].xpath("./td/p/text()")
                            tr_1 = table2_result[i-1].xpath("./td/p/text()")
                        if i>1:
                            tr = table2_result[i].xpath("./td/p/text()")
                            tr_1 = table2_result[i - 1].xpath("./td/p/text()")
                            tr_2 =table2_result[i-2].xpath("./td/p/text()")
                        if i>2:
                            tr_3 = table2_result[i-3].xpath("./td/p/text()")
                        if i>3:
                            tr_4 = table2_result[i-4].xpath("./td/p/text()")
                        if i>4:
                            tr_5 = table2_result[i-5].xpath("./td/p/text()")

                        idx = self.locate_index(tr,tr_1,tr_2,tr_3,tr_4,tr_5,4)
                        logging.warning("-----4------")
                        logging.warning(pcdm)
                        logging.warning(kldm_dict_value)
                        logging.warning(pxfs)
                        logging.warning(yxdh)
                        logging.warning(tr)
                        logging.warning(tr_1)
                        logging.warning(table2_tr_result_len)
                        logging.warning(i)
                        logging.warning(idx)
                        pro_code = table2_result[i-idx].xpath("./td/p/text()")[0]
                        pro_name = table2_result[i-idx].xpath("./td/p/a/text()")[0]
                        fill_order_table2 = table2_result[i].xpath("./td/p/text()")[0]
                        max_score_table2 = table2_result[i].xpath("./td/p/text()")[1]
                        min_score_table2 = table2_result[i].xpath("./td/p/text()")[2]
                        # 最低分位数
                        min_score_order = ""
                        enroll_no_table2 = table2_result[i].xpath("./td/p/text()")[3]
                    else:
                        pro_code = table2_result[i].xpath("./td/p/text()")[0]
                        try:
                            pro_name = table2_result[i].xpath("./td/p/a/text()")[0]
                        except:
                            # 如果有数据集中"专业名称"为空，则与index[i-parent_index]公用一个专业名称
                            pro_name = table2_result[i-parent_index].xpath("./td/p/a/text()")[0]
                        fill_order_table2 = table2_result[i].xpath("./td/p/text()")[1]
                        max_score_table2 = table2_result[i].xpath("./td/p/text()")[2]
                        min_score_table2 = table2_result[i].xpath("./td/p/text()")[3]
                        # 最低分位数
                        min_score_order = ""
                        enroll_no_table2 = table2_result[i].xpath("./td/p/text()")[4]
                scoreItemItemLoader.add_value("pcdm", pcdm)
                scoreItemItemLoader.add_value("kldm", kldm_dict_value)
                scoreItemItemLoader.add_value("pxfs", pxfs)
                scoreItemItemLoader.add_value("yxdh", yxdh)
                scoreItemItemLoader.add_value("pro_code", pro_code)
                scoreItemItemLoader.add_value("pro_name", pro_name)
                scoreItemItemLoader.add_value("fill_order_table2", fill_order_table2)
                scoreItemItemLoader.add_value("max_score_table2", max_score_table2)
                scoreItemItemLoader.add_value("min_score_table2", min_score_table2)
                scoreItemItemLoader.add_value("min_score_order", min_score_order)
                scoreItemItemLoader.add_value("enroll_no_table2", enroll_no_table2)
                scoreItem = scoreItemItemLoader.load_item()
            yield scoreItem

    def get_dict_loop(self):
        # 批次字典：order_seq_dict
        order_seq_dict = ['1', '2', '3', '4', '6', '7', 'C', 'E']
        # order_seq_dict = ['1']
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
        # item_class_dict=[order_seq'@','0','1']
        item_class_dict = ['A']
        # 院校排序方式字典
        school_type = ['1']
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

    # 查询结果中会出现N次填报记录复用一条专业代号与专业名称的情况，为此，需要定位pro_code与pro_name的索引
    # tr:table2 中的tr记录  tr_len：table2的tr记录中复用pro_code与pro_name信息的记录长度只能是4或5
    # 最多支持五次填报
    def locate_index(self,tr,tr_1,tr_2,tr_3,tr_4,tr_5,tr_len):
        idx = 0
        if (len(tr) < len(tr_1)) and (len(tr_1)==tr_len+1) and len(tr) == tr_len:
            logging.warning("idx")
            logging.warning("1")
            idx = 1
        if (len(tr) == len(tr_1)) and (len(tr) < len(tr_2)) and (len(tr_2)==tr_len+1) and len(tr) == tr_len:
            logging.warning("idx")
            logging.warning("2")
            idx = 2
        if (len(tr) == len(tr_1)) and (len(tr) == len(tr_2)) and (len(tr) < len(tr_3)) and (len(tr_3)==tr_len+1) and len(tr) == tr_len:
            idx = 3
        if (len(tr) == len(tr_1)) and (len(tr) == len(tr_2)) and (len(tr) == len(tr_3)) and (len(tr) < len(tr_4)) and (len(tr_4)==tr_len+1) and len(tr) == tr_len:
            idx = 4
        if (len(tr) == len(tr_1)) and (len(tr) == len(tr_2)) and (len(tr) == len(tr_3)) and (len(tr) == len(tr_4)) and (len(tr) < len(tr_5)) and (len(tr_5)==tr_len+1) and len(tr) == tr_len:
            idx = 5
        return idx


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