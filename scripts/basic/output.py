import json,threading
import config,search

fil = open(config.json_path +'\\local_sales.json', 'r', encoding='utf-8')
tab = json.loads(fil.read())
fil.close()
info = []

def invalid_print(name): #无效情况下
    #print(name + 'Begin')
    global info
    new_dict = {}
    new_dict['ducats'] = '0'
    new_dict['advicePrice'] = '0'
    new_dict['name'] = name
    new_dict['valid'] = False
    info.append(new_dict)
    #print(name + 'Ready')

''' 多线程版
def get_info(search_list):
    threadlist = [] #线程列表
    for item in search_list:
        if item in tab:
            t = threading.Thread(target = vaild_print, args = (item,tab[item],))
        else:
            t = threading.Thread(target = invalid_print, args = (item,))
        threadlist.append(t)
    for t in threadlist:
        t.start()
    for t in threadlist:
        t.join()
    return info #返回价格信息列表
'''

def get_info(search_list):
    for item in search_list:
        if item in tab:
            item_info = tab[item]
            item_info['name'] = item
            item_info['valid'] = True
            info.append(item_info)
        else:
            invalid_print(item)

    def make_recommend(info):
        max_price = 0
        for item_info in info:
            if int(item_info['advicePrice']) > max_price:
                max_price = int(item_info['advicePrice'])
        for item_info in info:
            if int(item_info['advicePrice']) == max_price:
                item_info['recommend'] = True
            else:
                item_info['recommend'] = False

    make_recommend(info)
    return info #返回价格信息列表
    
