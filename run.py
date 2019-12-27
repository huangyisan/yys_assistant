import win32gui

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if 'Xshell 6 (Free for Home/School)' in win32gui.GetWindowText(hwnd):
            print(hwnd)
        # win32gui.MoveWindow(199202, 0, 0, 760, 500, True)

# def EnumWindows(*args, **kwargs): # real signature unknown
#     pass
#
# EnumWindows(enumHandler, None)

win32gui.EnumWindows(enumHandler, None)