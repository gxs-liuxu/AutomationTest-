#coding:utf-8
import md5
import json
from ..common.log import *
    
#字符串md5加密
def get_md5(need_str):
    md = md5.new()
    md.update(need_str)
    return md.hexdigest()

#处理字符串为json格式
def str_to_json(result_str):

    RST = ''
    try:
        RST = json.loads(result_str)
    except:
        try:
            #处理可能包含在()内的json字符串
            temp_str = result_str.split('(')[1].split(')')[0]
            RST = json.loads(temp_str)
        except:
            logging.error("字符串处理Json失败".decode('utf-8'))
            return False
        
    return RST


#获取dict指定的字段数据
def dict_filter_columns(dict_data, array_need = ['*']):

    if type(dict_data) != dict:
        logging.error("Dict数据格式不正确.\n\t当前Dict数据:\t".decode('utf-8')  + str(dict_data) + '\n\t当前数据类型为:\t'.decode('utf-8') + str(type(dict_data)))
        return False
    else:
        if type(array_need) == list:            
            temp = len(array_need)
            if temp == 0:
                logging.error("处理Dict数据，未提供需求字段".decode('utf-8'))
                return False
            #array_need为['*']时返回整个json
            elif temp == 1 and array_need[0] == '*':
                return dict_data
            else:
                return_json = {}
                for i in range(0, temp):
                    if array_need[i] in dict_data.keys():
                        return_json[array_need[i]] = dict_data[array_need[i]]
                    else:
                        logging.warning("处理Dict数据警告，Keys不包含".decode('utf-8') + str(array_need[i]) + '字段.\n\t提供的Dict数据为\t'.decode('utf-8') + str(dict_data))
                return return_json
        else:
            logging.error("提供需求字段错误,需list格式数据.\n\t当前Dict数据:\t".decode('utf-8')  + str(array_need) + "\n\t当前数据格式为:\t".decode('utf-8') + str(type(array_need)))
            return False