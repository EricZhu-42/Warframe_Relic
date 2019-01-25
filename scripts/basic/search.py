import verification
import requests

token = verification.get_token()

ver_type = token['token_type']
ver_token = token['access_token']
header = {
    'Authorization' : ver_type + ' ' + ver_token
}

def search_in_wm(name):
    url = 'https://api.richasy.cn/wfa/basic/pc/wm/' + name
    response = requests.get(url,headers=header)
    response = response.json()
    info = response['info']
    del info['tradingTax']
    return info







