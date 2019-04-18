# _*_coding:utf-8_*_
__author__ = 'wmx'
__date__ = '2019/4/18 10:52'

import  pymysql,uuid,logging,copy
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings #导入setting文件


class DBHelper():

    def __init__(self):
        settings = get_project_settings()

        dbparam = dict (
            host = settings['MYSQL_HOST'],
            db = settings['MYSQL_DBNAME'],
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWD'],
            charset = 'utf8',#编码要加上，否则可能出现中文乱码问题
            cursorclass = pymysql.cursors.DictCursor,
            use_unicode = False,
        )
        # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        dbpool = adbapi.ConnectionPool('pymysql',**dbparam)
        self.dbpool = dbpool

    def connect(self):
        return self.dbpool

    #插入数据
    def insert_score(self,line):
        insert_sql = """
        insert into score(uuid,pcdm,kldm,pxfs,
                           fill_order,max_score,min_score,enroll_no,
                           pro_code,pro_name,fill_order_table2,max_score_table2,
                            min_score_table2,min_score_order,enroll_no_table2)
                       values (%s,%s,%s,%s,
                                %s,%s,%s,%s,
                                %s,%s,%s,%s,
                                %s,%s,%s)
            """
        # 对象拷贝   深拷贝
        asynItem = copy.deepcopy(line)
        # 调用插入的方法
        query = self.dbpool.runInteraction(self._score_insert(self.dbpool.connect().cursor(),insert_sql,line),insert_sql,asynItem)
        # 调用异常处理方法
        query.addErrback(self._handle_error)
        return line

    # 写入数据库中
    def _score_insert(self,canshu,sql,line):
        # 取出要存入的数据，这里item就是爬虫代码爬下来要存入items内的数据
        params = (str(uuid.uuid1()),line[0], line[1], line[2],
                  line[3],line[4],line[5], line[6],
                  line[7],line[8], line[9], line[10],
                  line[11],line[12], line[13])
        canshu.execute(sql, params)

    def _handle_error(self,failure):
        logging.warning("--------------database operation exception!!----------------")
        logging.warning(failure)


