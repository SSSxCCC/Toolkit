import winreg
import time

KEY_ProxyEnable = "ProxyEnable"
KEY_XPATH = "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings"

key_read = winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEY_XPATH, 0, winreg.KEY_READ)
key_write = winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEY_XPATH, 0, winreg.KEY_WRITE)


def proxy_enable():
    value, _ = winreg.QueryValueEx(key_read, KEY_ProxyEnable)
    return value


def set_proxy_enable(enable):
    winreg.SetValueEx(key_write, KEY_ProxyEnable, 0, winreg.REG_DWORD, enable)


while True:
    time.sleep(1)
    if proxy_enable() != 0:
        print(time.strftime('%F %T'))
        set_proxy_enable(0)
