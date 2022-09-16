import usb_hid
import hid.device.hori

usb_hid.enable((hid.device.hori.HoriPadS,))
import wifi
wifi.radio.connect("WangFeng","radiantwf")
# wifi.radio.connect("NETGERR-JY","19840618")