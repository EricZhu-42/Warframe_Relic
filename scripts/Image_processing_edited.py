import os
import time

import win32con
from aip import AipOcr
from PIL import Image, ImageGrab

import win32api

win32api.keybd_event(123,0,0,0) #Press F12
win32api.keybd_event(123,0,win32con.KEYEVENTF_KEYUP,0)
time.sleep(1)
ctime = time.strftime('%Y_%m_%d_%H%M%S',time.localtime(time.time()))

direc = 'C:\\Program Files (x86)\\Steam\\userdata\\186550984\\760\\remote\\230410\\screenshots' #Change it
img_name = 'D:/Desk/Coding/Py/Warframe_Relic/xp/resources/' + ctime +'.jpg' #Change it too

re = os.listdir(direc)
if 'thumbnails' in re:
    re.remove('thumbnails')
max_name = max(re)

#-----------------------edited above-----------------------

""" APPID AK SK """
APP_ID = '15481337'
API_KEY = 'Bha5Y1MuXGLc9CgEymiLdbwE'
SECRET_KEY = 'fZTLuIdjPX4rKPS3HeWCTPR2uWxY75rn'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" To grab the image """
im = Image.open(direc + '\\' + max_name)

""" To cut the image """
img_size = im.size

percentage = {
    'x':0/1980,
    'y':455/1080,
    'width':1920/1920,
    'height':27/1080
}

x = percentage['x']*img_size[0]
y = percentage['y']*img_size[1]
width = percentage['width']*img_size[0]
height = percentage['height']*img_size[1]
region_coordinates = (int(x),int(y),int(x+width),int(y+height))

region = im.crop(region_coordinates)
region.save(img_name) #Change it

""" To get the text """
def get_image(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_image(img_name)

response = client.basicAccurate(image)
texts = []
for k in response['words_result']:
    texts.append(k.get('words'))
 
""" To modify the texts in due form """
def edit(text):
    text = text.replace(' ','')
    if 'prme' in text.lower():
        idx = text.lower().index('prme')
        text = text[:idx]+'PRIME'+text[idx+4:]
    text = text.replace('PRIME',' PRIME ')
    if '蓝图' in text:
        if text[text.index('蓝图')-1] == ' ':
            pass
        else:
            text = text.replace('蓝图','')
    return(text)

result = []
for text in texts:
    if 'FORMA' in text:continue
    result.append(edit(text))
print(result)
