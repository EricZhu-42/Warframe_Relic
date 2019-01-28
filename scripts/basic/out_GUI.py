from tkinter import *
import time, threading

def popwindow(dic):
    root = Tk()
    screen_width = root.winfo_screenmmwidth()
    screen_height = root.winfo_screenheight() #获取当前显示器分辨率    
    root.overrideredirect(True)
    root.wm_attributes('-topmost',1) #置顶
    root.attributes('-alpha',0.8)
    root_width, root_height = 900, 200 #窗口大小
    global root_x, root_y #必须声明位置是全局变量
    root_x, root_y = 10, 10 #初始窗口位置
    root.geometry(str(root_width)+'x'+str(root_height)+'+'+str(root_x)+'+'+str(root_y)) #主窗口参数

    global closetime
    closetime = config.get_config("disappear_time") #关闭时间，单位：秒

    def autoClose():
        for i in range(closetime):
            clock = Label(root, text=str(closetime-i), font=('Microsoft YaHei',12))
            clock.place(x=10, y=5)
            time.sleep(1)    
            clock.destroy()       
        #root.destroy() #Don't use this!
        root.quit()

    def click(event):
        global mouse_x, mouse_y
        mouse_x, mouse_y = event.x, event.y
    def release(event):
        global mouse_x, mouse_y
        global root_x, root_y
        root_x += event.x-mouse_x
        root_y += event.y-mouse_y
        root.geometry(str(root_width)+'x'+str(root_height)+'+'+str(root_x)+'+'+str(root_y))
    root.bind('<Button-1>',click)
    root.bind('<ButtonRelease-1>',release)#拖动功能

    n = len(dic) #物品个数

    box_height = int(root_height*0.85)
    box_width = int(root_width/5)
    if n==0:
        gap_width = 0
    else:
        gap_width = int(box_width/5)
    side_margin = int((root_width-n*box_width-(n-1)*gap_width)/2)
    head_margin = int((root_height-box_height)/2)
    box_color_common = 'wheat'
    box_color_recommend = 'SandyBrown'#box参数

    item_ft =('Microsoft YaHei', 11)
    price_ft =('Microsoft YaHei', 11)
    text_color_common = 'Grey'
    text_color_recommend = 'Black'#label参数

    box = [None for i in range(n)]
    lb = [[None for i in range(3)] for j in range(n)]#初始化box和label的列表

    box_coordinate = [side_margin,head_margin]#初始化坐标

    for i in range(n):
        item = dic[i]
        if item['recommend']:
            text_color = text_color_recommend
            box_color = box_color_recommend
        else:
            text_color = text_color_common
            box_color = box_color_common
        label_color = box_color
        box[i] = Canvas(root, width=box_width, height=box_height, bg=box_color)
        box[i].place(x=box_coordinate[0], y=box_coordinate[1], anchor=NW)
        for j in range(3):
            lb_x = int(0.075*box_width)+box_coordinate[0]
            lb_y = int((0.125+0.3125*j)*box_height)+box_coordinate[1] 
            if j==0 : word, ft = item['name'], item_ft
            if j==1 : word, ft = item['advicePrice']+' 白金', price_ft
            if j==2 : word, ft = item['ducats']+' 奸商币', price_ft
            
            lb[i][j] = Label(root, text = word, bg=label_color, font=ft, foreground=text_color)
            lb[i][j].place(x=lb_x, y=lb_y, anchor=NW)

        box_coordinate[0] += box_width
        box_coordinate[0] += gap_width
    
    t = threading.Thread(target=autoClose)
    t.start()
    root.mainloop()
    
test = False #测试用

if test:
    dic = [
        {'ducats': '15', 'advicePrice': '5', 'name': '食人鱼 PRIME 枪管', 'valid': True, 'recommend': False}, 
        {'ducats': '15', 'advicePrice': '5', 'name': '食人鱼 PRIME 枪管', 'valid': True, 'recommend': False}, 
        {'ducats': '45', 'advicePrice': '9', 'name': 'BANSHEE PRIME 蓝图', 'valid': True, 'recommend': True}, 
        {'ducats': '15', 'advicePrice': '3', 'name': '布莱顿 PRIME 枪托', 'valid': True, 'recommend': False}
    ]

    popwindow(dic)
