import usb_hid
import hid.device.hori

usb_hid.enable((hid.device.hori.HoriPadS,))

# wifi.radio.connect("NETGERR-JY","19840618")
wifi.radio.connect("WangFeng","radiantwf")
print(customize.datetime.ntpSync())
