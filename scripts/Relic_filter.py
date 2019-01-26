'''用于过滤出遗物奖励列表'''

import sys,os,json
currentpath = sys.path[0]
basic_path = currentpath + "\\basic"
sys.path.append(basic_path)

import config

with open(config.json_path + '\\full_dic.json','r',encoding='utf-8') as full_dic_file:
    full_dic = json.loads(full_dic_file.read())

relic_dic = {}
for key in full_dic:
    if ('PRIME' in key) and not ('一套' in key) and not ('primed' in full_dic[key]):
        relic_dic[key] = full_dic[key]

with open(config.json_path + '\\relic_dic.json','w+',encoding='utf-8') as relic_dic_file:
    relic_dic_file.write(json.dumps(relic_dic,indent=4,ensure_ascii=False))