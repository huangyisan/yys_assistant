# pip3 install pywin32
# pip3 install pyautogui
# pip install keyboard

import win32gui,win32api, win32con
import pyautogui as pag
import keyboard
import time

# hwnd = win32gui.FindWindow(None,'live-Bigdata-jumpbox')
hwnd = win32gui.FindWindow(None,'安全整改')
# print(win32gui.GetActiveWindow())

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
    left+=8
    right-=8
    bottom-=8
    return left, top, right, bottom


def get_window_size()->tuple or 0:
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

def window_move_left()->tuple:
    '''
    将窗体等比例缩放后移动至左上角,且宽度不超过屏幕分辨率的1/2
    :return:
    '''
    resolution = get_screen_resolution()
    size = get_window_size()

    # size为0，则不进行任何处理
    if size:
        x,y = resolution
        w,h = size

        half_x = int(x/2)

        ratio_w = half_x / w

        h = int(ratio_w*h)

        win32gui.MoveWindow(hwnd, -8, 0, half_x, h, True)
        return -8, 0, half_x, h
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
    # im = pag.screenshot(region=size)
    img = pag.screenshot()
    pos = get_mouse_axis()
    r, g, b = img.getpixel(pos)
    return r,g,b

def record_pixel()->dict:
    '''
    按下热键，录制鼠标指定坐标像素
    :return:
    '''
    count = 1
    pixel_dict = {}
    while True:
        if keyboard.is_pressed('ctrl+w'):
            pixel_dict[count] = get_mouse_pos_pixel()
            count += 1
            time.sleep(1)


        if keyboard.is_pressed('ctrl+q'):
            return pixel_dict



