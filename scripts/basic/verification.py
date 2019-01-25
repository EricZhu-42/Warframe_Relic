import json

import requests


def get_token():
    payload = {
        'client_id' : 'YOUR CLIENT_ID',
        'client_secret' : 'YOUR CLIENT_SECRE',
        'grant_type' : 'client_credentials'
    } 
    token = requests.post('https://api.richasy.cn/connect/token', data=payload)
    token = token.json()
    return token
