import os,sys,json

currentpath = sys.path[0]
root = os.path.dirname(currentpath)
re = os.listdir(root)
if 'json' in re:
    json_path = root + '\\json'
else:
    json_path = os.path.dirname(root) + '\\json'

def set_config(key,value):
    with open(json_path + '\\config.json','r') as config_file:
        config = json.loads(config_file.read())
    config[key]=value
    with open(json_path + '\\config.json','w+') as config_file:
        config_file.write(json.dumps(config,indent=4))
		
def get_config(keyword):
    config_file = open(json_path + '\\config.json','r')
    config = eval(config_file.read())
    config_file.close()
    return config.get(keyword)

