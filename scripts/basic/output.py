import json,threading
import config,search

fil = open(config.json_path +'\\Dic.json', 'r', encoding='utf-8')
tab = json.loads(fil.read())
info = []

def vaild_print(name,query): #有效情况下
    #print(name + 'Begin')
    global info
    new_dict = search.search_in_wm(query)
    new_dict['ducats'] = str(new_dict['ducats'])
    new_dict['advicePrice'] = str(new_dict['advicePrice'])
    new_dict['name'] = name
    new_dict['valid'] = True
    info.append(new_dict)
    #print(name + 'Ready')

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

