from tkinter import *
import threading,time

def popwindow(dic):
    root = Tk()

    def auto_destory():
        time.sleep(10)
        root.destroy()

    root.overrideredirect(True)
    root.attributes('-alpha',0.8)
    root_width = 900
    root_height = 200
    root.geometry(str(root_width)+'x'+str(root_height)+'+10+10')#主窗口参数

    n = len(dic) #物品个数

    box_height = int(root_height*0.85)
    box_width = int(root_width/5)
    if n==0:
        gap_width = 0
    else:
        gap_width = int(box_width/5)
    side_margin = int((root_width-n*box_width-(n-1)*gap_width)/2)
    head_margin = int((root_height-box_height)/2)
    dfcolor = 'blue'#box参数

    box = [None for i in range(n)]
    lb = [[None for i in range(3)] for j in range(n)]#初始化box和label的列表
    box_coordinate = [side_margin,head_margin]#初始化坐标

    '''
    dic = [
        {'ducats': '15', 'advicePrice': '5', 'name': '食人鱼 PRIME 枪管', 'valid': True}, 
        {'ducats': '15', 'advicePrice': '5', 'name': '食人鱼 PRIME 枪管', 'valid': True}, 
        {'ducats': '45', 'advicePrice': '9', 'name': 'BANSHEE PRIME 蓝图', 'valid': True}, 
        {'ducats': '15', 'advicePrice': '3', 'name': '布莱顿 PRIME 枪托', 'valid': True}
    ]
    '''

    for i in range(n):
        box[i] = Canvas(root, width=box_width, height=box_height, bg=dfcolor)
        box[i].place(x=box_coordinate[0], y=box_coordinate[1], anchor=NW)
        item = dic[i]
        for j in range(3):
            lb_x = int(0.075*box_width)+box_coordinate[0]
            lb_y = int((0.125+0.3125*j)*box_height)+box_coordinate[1] 
            if j==0 : word = item['name']
            if j==1 : word = item['advicePrice']+' 白金'
            if j==2 : word = item['ducats']+' 奸商币'

            lb[i][j] = Label(root, text = word)
            lb[i][j].place(x=lb_x, y=lb_y, anchor=NW)

        box_coordinate[0] += box_width
        box_coordinate[0] += gap_width
		
    t = threading.Thread(target=auto_destory)
    t.start()
    mainloop()