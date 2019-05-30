# coding: utf-8
import win32gui
import win32ui
import win32con
import win32api

hdesktop = win32gui.GetDesktopWindow()

width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)

desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFromHandle(desktop_dc)

mem_dc = img_dc.CreateCompatibleDC()

screengrab = win32ui.CreateBitmap()
screengrab.CreateCompatibleBitmap(
    img_dc,
    width,
    height
)
mem_dc.SelectObject(screengrab)

mem_dc.BitBlt(
    (0, 0),
    (width, height),
    img_dc,
    (left, top),
    win32con.SRCOPY
)

screengrab.SaveBitmapFile(
    mem_dc,
    'c:\\WINDOWS\\Temp\\screengrab.bmp'
)

mem_dc.DeleteDC()
win32gui.DeleteObject(
    screengrab.GetHandle()
)
