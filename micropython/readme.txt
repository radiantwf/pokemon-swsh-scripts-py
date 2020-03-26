
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

import wifi
wifi.ap(ssd="micropython-esp32-wf", pwd="radiantwf")
wifi.connect("NETGERR-JY", "19840618")
wifi.connect("WangFeng", "radiantwf") 
