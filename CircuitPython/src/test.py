import hid.joystick
import usb_hid
import time

joystick = hid.joystick.JoyStick(usb_hid.devices)

line = "A"
print(line)
joystick.send(line)
time.sleep(0.1)
joystick.release()
time.sleep(15)

line = "B"
print(line)
joystick.send(line)
time.sleep(0.1)
joystick.release()
time.sleep(1)

line = "A|LStick@100,-100"
print(line)
joystick.send(line)
time.sleep(0.1)
joystick.release()
time.sleep(1)

line = "A|Plus"
print(line)
joystick.send(line)
time.sleep(0.1)
joystick.release()
time.sleep(1)

line = "Top|Minus"
print(line)
joystick.send(line)
time.sleep(0.1)
joystick.release()
time.sleep(1)

line = "TOPLEFT|B|HOME"
print(line)
joystick.send(line)
time.sleep(0.1)
joystick.release()
time.sleep(1)

line = "A|B|X|Y"
print(line)
joystick.send(line)
time.sleep(0.1)
joystick.release()
time.sleep(1)
