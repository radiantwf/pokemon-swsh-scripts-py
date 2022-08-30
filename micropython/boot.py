# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

# esp.osdebug(None)

import webrepl
import wifi
webrepl.start()
wifi.connect(ssd="WangFeng", pwd="radiantwf")
wifi.connect("NETGERR-JY", "19840618")

# wifi.ap(ssd="micropython-esp32-wf", pwd="radiantwf")
# wifi.connect("NETGERR-JY", "19840618")
# wifi.connect("WangFeng", "radiantwf")
