from wireless import wifi
from microchip.winc1500 import winc1500 as wifi_driver

def init():
    drv.auto_init()

OPEN = wifi.WIFI_OPEN
WEP = wifi.WIFI_WEP
WPA = wifi.WIFI_WPA
WPA2 = wifi.WIFI_WPA2


def link(ssid,password,sec=WPA2, attempts=5,delay=2000):
    exc = None
    for _ in range(attempts):
        try:
            wifi.link(ssid, sec, password)
            break
        except Exception as e:
            exc = e
            sleep(delay)
    else:
        raise exc


