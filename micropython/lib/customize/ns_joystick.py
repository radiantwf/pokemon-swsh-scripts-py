from machine import UART
from time import sleep
import customize.datetime
import uasyncio


class NSJoystick:
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        pass

    _uart = None

    def uart(self, uart_num=1, tx=17, rx=16):
        self._uart = UART(uart_num, baudrate=9600, tx=tx, rx=rx)
        return

    async def send(self, msg, duration=0, debug=False):
        self._uart.write("%s\r\n" % (msg))
        await uasyncio.sleep(duration)
        self._uart.write(b'RELEASE\r\n')
        if debug:
            print("[%s] %s" % (customize.datetime.now(), msg))
