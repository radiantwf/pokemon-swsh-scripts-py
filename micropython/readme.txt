
下载固件
http://www.micropython.org/download#esp32


烧录固件
esptool.py --chip esp32 --port /dev/tty.wchusbserial* erase_flash
esptool.py --chip esp32 --port /dev/tty.wchusbserial* write_flash -z 0x1000 esp32-*.bin

链接设备
screen /dev/tty.wchusbserial* 115200

>>> help()
Welcome to MicroPython on the ESP32!

For generic online docs please visit http://docs.micropython.org/

For access to the hardware use the 'machine' module:

import machine
pin12 = machine.Pin(12, machine.Pin.OUT)
pin12.value(1)
pin13 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
print(pin13.value())
i2c = machine.I2C(scl=machine.Pin(21), sda=machine.Pin(22))
i2c.scan()
i2c.writeto(addr, b'1234')
i2c.readfrom(addr, 4)

Basic WiFi configuration:

import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()                             # Scan for available access points
sta_if.connect("<AP_name>", "<password>") # Connect to an AP
sta_if.isconnected()                      # Check for successful connection

Control commands:
  CTRL-A        -- on a blank line, enter raw REPL mode
  CTRL-B        -- on a blank line, enter normal REPL mode
  CTRL-C        -- interrupt a running program
  CTRL-D        -- on a blank line, do a soft reset of the board
  CTRL-E        -- on a blank line, enter paste mode

For further help on a specific object, type help(obj)
For a list of available modules, type help('modules')


>>> import  webrepl_setup
WebREPL daemon auto-start status: disabled

Would you like to (E)nable or (D)isable it running on boot?
(Empty line to quit)
> e
To enable WebREPL, you must set password for it
New password (4-9 chars): ******
Confirm password: ******
Changes will be activated after reboot
Would you like to reboot now? (y/n) y

import network


ap(ssd="micropython-esp32-wf", pwd="radiantwf")
connect(ssd="NETGERR-JY", pwd="19840618")

wifi.py
import network
def connect(ssd,pwd,force=False):
    sta_if = network.WLAN(network.STA_IF)
    if force or not sta_if.isconnected():
        if sta_if.isconnected():
            sta_if.disconnect()
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssd, pwd) 
    if sta_if.isconnected(): 
        print("network config:", sta_if.ifconfig())
        return True
    return False
def ap(ssd,pwd='',active=1):
    ap=network.WLAN(network.AP_IF)
    ap.active(active)
    if pwd=='':
        ap.config(essid=ssd, authmode=network.AUTH_OPEN)
        return
    ap.config(essid=ssd, authmode=network.AUTH_WPA_WPA2_PSK, password=pwd)



串口

UART构造器：
ESP32自身只有两个UART资源
导入UART 模块：from machine import UART

UART对象的构造器函数：UART(id, baudrate, bits, parity, rx, tx, stop, timeout)

id : 串口编号：ESP32的UART资源只有两个， id有效取值范围为1,2
bandrate: 波特率(时钟频率)：常用波特率为：9600 （默认），115200，信息接受双方的波特率必须一致，否则会乱码。
bits：单个字节的位数(比特数)：8 (默认)，7，9
parity： 校验方式：None 不进行校验（默认），0 偶校验，1 奇校验
rx：接收口的GPIO编号
tx：发送口的GPIO编号
stop: 停止位个数：1 （默认），2
timerout: 超时时间：取值范围： 0 < timeout ≤ 2147483647

from machine import UART
uart = UART(2, baudrate=115200, rx=13,tx=12,timeout=10)

字符串读写：

uart.read(10)       # read 10 characters, returns a bytes object
                    # 读入10个字符， 返回一个比特对象

uart.read()         # read all available characters
                    # 读取所有的有效字符

uart.readline()     # read a line
                    # 读入一行

uart.readinto(buf)  # read and store into the given buffer
                    # 读入并且保存在缓存中

uart.write('abc')   # write the 3 characters
                    # 向串口写入3个字符abc

字符读写：

uart.readchar()     # read 1 character and returns it as an integer
                    # 读入一个字符

uart.writechar(42)  # write 1 character
                    # 写入ASCALL码为42的字符

uart.writechar(ord('*')) # 等同于uart.writechar(42)

检测串口是否有数据：

uart.any()          # returns the number of characters waiting