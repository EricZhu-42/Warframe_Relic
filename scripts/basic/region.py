import os,sys,time
import config
from PIL import Image, ImageFilter

ctime = time.strftime('%Y_%m_%d_%H%M%S',time.localtime(time.time()))

def get_img_location():
    img_location =  config.root + '\\cache\\'+ ctime + '.jpg'
    return img_location

def region(raw_location):
    im = Image.open(raw_location)
    #im = im.convert("L")
    #im = im.filter(ImageFilter.FIND_EDGES)
    """ To cut the image """
    img_size = im.size
    percentage = {
        'x':0/1980,
        'y':460/1080,
        'width':1920/1920,
        'height':27/1080
    }

    x = percentage['x']*img_size[0]
    y = percentage['y']*img_size[1]
    width = percentage['width']*img_size[0]
    height = percentage['height']*img_size[1]
    region_coordinates = (int(x),int(y),int(x+width),int(y+height))
    region = im.crop(region_coordinates)
    region.save(get_img_location())