import sys,os
currentpath = sys.path[0]
basic_path = currentpath + "\\basic"
sys.path.append(basic_path)

import region,screenshot,output
from get_sentence import get_sentence
from ocr import ocr

def main():
    screenshot.snapscreen() #截图，保存到Steam目录
    raw_location = screenshot.get_raw_location() #原图片的位置
    #print(raw_location)
    region.region(raw_location) #处理截图，保存到cache文件夹
    img_location = region.get_img_location() #bar图的位置
    #print(img_location)
    items = ocr(img_location) #物品名称列表
    info = output.get_info(items) #获得价格列表
    sentence = get_sentence(info) #获得编辑后的价格字符串
    print(sentence)
    #settext(sentence)

if __name__ == '__main__':
    main()

