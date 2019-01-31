import sys,os
currentpath = sys.path[0]
basic_path = currentpath + "\\basic"
sys.path.append(basic_path)

import region,screenshot,output,out_GUI
from get_sentence import get_sentence
from ocr import ocr
from time import time

pre_time = time()

def print_time(message):
    global pre_time
    cur_time = time.time()
    print(message + " takes " + str(cur_time-pre_time) + ' sec')
    pre_time = cur_time

def main():
    #screenshot.snapscreen() #截图，保存到Steam目录
    #print_time('Screenshot')
    raw_location = screenshot.get_raw_location() #原图片的位置
    #print(raw_location)
    region.region(raw_location) #处理截图，保存到cache文件夹
    #print_time('Region')
    img_location = region.get_img_location() #bar图的位置
    #print(img_location)
    items = ocr(img_location) #物品名称列表
    #print_time('OCR')
    info = output.get_info(items) #获得价格列表
    #print_time('Get_info')

    out_GUI.popwindow(info) #输出到窗口中
    #print_time('Pop GUI')

    #sentence = get_sentence(info) #获得编辑后的价格字符串
    #print(info)
    #settext(sentence)

if __name__ == '__main__':
    main()

