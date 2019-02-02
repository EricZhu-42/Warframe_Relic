import json,threading
import config,search
from fuzzywuzzy import process


fil = open(config.json_path +'\\local_sales.json', 'r', encoding='utf-8')
tab = json.loads(fil.read())
choices = [item for item in tab]

fil.close()
info = []

def regularize(search_list):
    for i in range(len(search_list)):
        search_list[i] = process.extractOne(search_list[i],choices)[0]
    return(search_list)

def invalid_print(name): #无效情况下
    #print(name + 'Begin')
    global info
    new_dict = {}
    new_dict['ducats'] = 0
    new_dict['advicePrice'] = 0
    new_dict['name'] = name
    new_dict['valid'] = False
    info.append(new_dict)
    #print(name + 'Ready')

test_list = ['雷克斯 PRIME 枪管', 'SLIMBO PRIME 系统', 'OBERON PRIME 蓝图','螺钉双枪 PRIME 枪管']

def get_info(search_list):
    #print(search_list)
    search_list = regularize(search_list)
    for item in search_list:
        if item in tab:
            item_info = {}
            item_info['ducats'] = eval(tab[item]['ducats'])
            item_info['advicePrice'] = eval(tab[item]['advicePrice'])
            item_info['name'] = item
            item_info['valid'] = True
            info.append(item_info)
        else:
            invalid_print(item)

    def make_recommend(info):
        recommend_list = sorted(info, reverse = True, key = lambda x:(x['advicePrice'],x['ducats']))
        recommend_name = recommend_list[0]['name']
        for item in info:
            if item['name']==recommend_name:
                item['recommend'] = True
            else:
                item['recommend'] = False

    make_recommend(info)
    return info #返回价格信息列表
    
if __name__ == '__main__':
    print(get_info(test_list))