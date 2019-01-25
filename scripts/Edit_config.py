import sys,os
currentpath = sys.path[0]
basic_path = currentpath + "\\basic"
sys.path.append(basic_path)

import config

#config.set_config('steam_screenshot_dir','C:\\Program Files (x86)\\Steam\\userdata\\186550984\\760\\remote\\230410\\screenshots')
config.set_config('test','res')