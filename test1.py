# _*_coding:utf-8_*_
__author__ = 'wmx'
__date__ = '2019/4/12 15:14'
import  string,logging
def get_dict_loop():
    # 批次字典：order_seq_dict
    order_seq_dict = ['1', '2', '3', '4', '6', '7', 'C', 'E']
    # 拿到大小写字母
    letter_list = string.ascii_letters
    # 拿到大写字母
    uppser_letter_str = letter_list[26:]
    uppser_str = " ".join(uppser_letter_str)
    item_class_dict=[]
    # 科类字典：item_class_dict
    item_class_dict =uppser_str.split(" ")
    item_class_dict.insert(26,'@')
    item_class_dict.insert(27, '0')
    item_class_dict.insert(28, '1')
    # 院校排序方式字典
    school_type=['1','2']
    list=[]
    list_temp=[]
    for i in range(len(order_seq_dict)):
        for j in range(len(item_class_dict)):
            for k in range(len(school_type)):
                list_temp=[order_seq_dict[i],item_class_dict[j],school_type[k]]
                list.append(list_temp)
    logging.warning(list)
    logging.warning (len(list))
    return list

get_dict_loop()