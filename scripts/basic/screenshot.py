import os,sys,time,json
import win32api,win32con
import config

steam_screenshot_dir = config.get_config('steam_screenshot_dir')

def snapscreen():
    win32api.keybd_event(123,0,0,0) #Press F12
    win32api.keybd_event(123,0,win32con.KEYEVENTF_KEYUP,0) #Key F12 up
    ctime = time.strftime('%Y_%m_%d_%H%M%S',time.localtime(time.time()))

def get_raw_location():
    re = os.listdir(steam_screenshot_dir)
    if 'thumbnails' in re:
        re.remove('thumbnails')
    max_name = max(re)
    return steam_screenshot_dir + '\\' + max_name

if __name__ == '__main__':
    time.sleep(3)
    snapscreen()
    time.sleep(0.5)
    print(get_raw_location())
