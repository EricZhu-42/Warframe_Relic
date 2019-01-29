from aip import AipOcr

""" APPID AK SK """
APP_ID = YOUR APP_ID
API_KEY = YOUR API_KEY
SECRET_KEY = YOUR SECRET_KET

client = AipOcr(APP_ID, API_KEY, SECRET_KEY) #创建OCR实例

def get_image(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def ocr(img_location):
    image = get_image(img_location)
    response = client.basicAccurate(image)
    texts = []
    for k in response['words_result']:
        texts.append(k.get('words'))
        """ To modify the texts in due form """
    def edit(text): #进行格式修改
        text = text.replace('t','')
        text = text.replace(' ','')
        text = text.upper()
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
        if 'forma' in text.lower():continue
        result.append(edit(text))
    return result



