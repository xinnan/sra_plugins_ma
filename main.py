from . import *

import re
import time
import orjson

from get_width import get_width
from utils.calculated import calculated
from utils.log import log
from subprocess import run, DEVNULL
from utils.config import read_json_file, modify_json_file, CONFIG_FILE_NAME

calculated1 = None

def main(e=None):
    global calculated1
    get_width("崩坏：星穹铁道")
    calculated1 = calculated()
    calculated1.switch_window()
    import pyautogui # 缩放纠正
    
    f = open("D:\\ma.txt")
    lines = f.readlines()
    f.close()

    print( "load %d" % len(lines))
    i = 0

    for ma in lines:
        print ("left %d to redeem" % (len(lines)-i))
        # 点击...
        calculated1.relative_click([92, 11])
        time.sleep(0.5)
        # 点击兑换码
        calculated1.relative_click([84, 28])
        time.sleep(0.5)
        # 点击兑换码输入框
        calculated1.relative_click([34, 52])
        time.sleep(0.5)
        # 输入兑换码
        calculated1.keyboard.type(ma)
        time.sleep(0.8)
        # 点击确认
        calculated1.relative_click([61, 64])
        time.sleep(1.3)
        # 点击确认
        calculated1.relative_click([52, 60])
        time.sleep(0.5)
        i += 1

@hookimpl
def add_option(SRA):
    return SRA.add_option("兑换码兑换", main, 0)
