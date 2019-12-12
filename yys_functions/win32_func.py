# pip3 install pywin32
# pip3 install pyautogui
# pip install keyboard

import win32gui,win32api, win32con
import pyautogui as pag
import keyboard

# hwnd = win32gui.FindWindow(None,'live-Bigdata-jumpbox')
hwnd = win32gui.FindWindow(None,'安全整改')

def get_screen_resolution():
    x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    return x,y

def get_window_pos(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    left+=8
    top+=8
    right-=8
    bottom-=8
    return left, top, right, bottom

def get_window_size(pos):
    left, top, right, bottom = pos
    w = right - left
    h = bottom - top
    return w,h

def window_move_left(resolution, size):
    x,y = resolution
    w,h = size

    half_x = int(x/2)

    ratio_w = half_x / w

    h = int(ratio_w*h)

    win32gui.MoveWindow(hwnd, -8, 0, half_x, h, True)

    return -8, 0, half_x, h

def get_mouse_axis():
    return win32api.GetCursorPos()

def get_pos_pixel(pos):
    # im = pag.screenshot(region=size)
    img = pag.screenshot()
    (r, g, b) = img.getpixel(pos)
    return r,g,b

def record_pixel():
    while True:
        try:
            if keyboard.is_pressed('q'):
                on_triggered()
                break
        except:
            break

def hot_key():
    hotkey = 'q'
    keyboard.add_hotkey(hotkey, on_triggered)
    # if hotkey == 'q':
    #     on_triggered()

def on_triggered():
    print("Triggered!")


# win32gui.MoveWindow(hwnd, -8, 0, 937, 545, True)

# print(win32api.GetSystemMetrics(win32con.SM_CXSCREEN))
# print(win32api.GetSystemMetrics(win32con.SM_CYSCREEN))


