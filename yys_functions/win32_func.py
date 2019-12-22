import win32gui,win32api, win32con
import pyautogui as pag
from configparser import ConfigParser
import random
import pyautogui
import keyboard
import os
import signal
import time
from project_settings import yys_config_path


def get_screen_resolution()->tuple:
    '''
    获取屏幕分辨率
    :return: x轴 y轴
    '''
    x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    return x,y

def get_window_pos(hwnd:object)->tuple:
    '''
    获取指定句柄窗口的位置
    :param hwnd:  句柄对象
    :return: 左上,右下坐标值
    '''
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    # left+=8
    # right-=8
    # bottom-=8
    return left, top, right, bottom


def get_window_size(hwnd)->tuple or 0:
    '''
    获取窗口宽高
    :return: 宽高
    '''
    pos = get_window_pos(hwnd)
    left, top, right, bottom = pos

    # 判断窗体左上角是否为(0,0),如果是(0,0)，则返回0
    if left == top == 0:
        return 0
    else:
        w = right - left
        h = bottom - top
        return w,h

def window_move_left(file_name)->tuple:
    hwnd = win32gui.FindWindow(None, file_name)
    '''
    将窗体等比例缩放后移动至左上角,且宽度不超过屏幕分辨率的1/2
    :return:
    '''
    resolution = get_screen_resolution()
    size = get_window_size(hwnd)

    # size为0，则不进行任何处理
    if size:
        x,y = resolution
        w,h = size

        half_x = int(x/2)

        ratio_w = half_x / w

        h = int(ratio_w*h)

        win32gui.MoveWindow(hwnd, 0, 0, half_x, h, True)
        return 0, 0, half_x, h
    else:
        pass

def window_move_right(file_name)->tuple:
    hwnd = win32gui.FindWindow(None,file_name)
    '''
    将窗体等比例缩放后移动至右上角,且宽度不超过屏幕分辨率的1/2
    :return:
    '''
    resolution = get_screen_resolution()
    size = get_window_size(hwnd)

    # size为0，则不进行任何处理
    if size:
        x,y = resolution
        w,h = size

        half_x = int(x/2)

        ratio_w = half_x / w

        h = int(ratio_w*h)

        win32gui.MoveWindow(hwnd, half_x, 0, half_x, h, True)
        return half_x, 0, half_x, h
    else:
        pass

def get_mouse_axis()->tuple:
    '''
    获取鼠标当前指向坐标
    :return:
    '''
    return win32api.GetCursorPos()

def get_mouse_pos_pixel()->tuple:
    '''
    获取鼠标指向坐标的像素
    :return:
    '''
    img = pag.screenshot()
    pos = get_mouse_axis()
    r, g, b = img.getpixel(pos)
    return r,g,b,pos

def compare_rgb(pos_name:str)->bool:
    '''
    比较截图rgb和配置rgb是否符合
    :param pos_name:  英文pos_name    single_simhun_fire_pos
    :return:
    '''
    cfg = ConfigParser()
    config_file = yys_config_path
    cfg.read(config_file, encoding='utf-8')

    # 根据pos_name参数获取config.ini中的pixel_info配置
    pixel_info = eval(cfg.get('pixel_info',cfg.get('pos_name',pos_name)))

    # config.ini中的配置rgb信息
    config_rgb = pixel_info[0:3]

    # config.ini中配置的坐标信息
    pos = pixel_info[-1]

    # 截图根据坐标获取到的rgb信息
    img = pag.screenshot()
    rgb= img.getpixel(pos)

    # 判断截图获取的rgb信息和配置中的rgb信息是否一致
    if rgb == config_rgb:
        return True
    return False

def click_mouse(pos_name:str,random_num:int=4):
    '''

    :param pos_name: 鼠标点击的位置
    :param random_num: 随机数最大值，用来构造新的坐标区间，设定不要过大
    :return:
    '''

    cfg = ConfigParser()
    config_file = yys_config_path
    cfg.read(config_file, encoding='utf-8')
    pixel_info = eval(cfg.get('pixel_info',cfg.get('pos_name',pos_name)))
    pos = pixel_info[-1]

    # 给予xy四个随机区间,获得一个新的坐标
    random_x = pos[0] + random.randint(0, random_num)
    random_y = pos[1] + random.randint(0, random_num)

    # 鼠标进行移动, 并且左单击
    pyautogui.moveTo(random_x, random_y, duration=0.1)
    pyautogui.click(button='left')

def stop_child_process(ppid):
    while True:
        if keyboard.is_pressed('ctrl+c'):
            os.kill(ppid, signal.SIGTERM)
            time.sleep(1)



