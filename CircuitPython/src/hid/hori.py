import usb_hid

# This is only one example of a gamepad descriptor, and may not suit your needs.
_HORIPAD_S_DESCRIPTOR = bytes((
    0x05, 0x01,             # Generic desktop controls
    0x09, 0x05,             # Joystick
    0xA1, 0x01,             # Application
    # Buttons (2 bytes)
    0x15, 0x00,             # button off state
    0x25, 0x01,             # button on state
    0x35, 0x00,             # button off state
    0x45, 0x01,             # button on state
    0x75, 0x01,             # 1 bit per report field
    0x95, 0x0E,             # 14 report fields (14 buttons)
    0x05, 0x09,             # Buttons (section 12)
    0x19, 0x01,
    0x29, 0x0E,
    0x81, 0x02,             # Variable input
    0x95, 0x02,             # 2 report fields (empty 2 bits)
    0x81, 0x01,             # Array input
    # HAT switch
    0x05, 0x01,             # Generic desktop controls
    0x25, 0x07,             # 8 valid HAT states, sending 0x08 = nothing pressed
    0x46, 0x3B, 0x01,       # HAT "rotation"
    0x75, 0x04,             # 4 bits per report field
    0x95, 0x01,             # 1 report field (a nibble containing entire HAT state)
    0x65, 0x14,             # unit degrees
    0x09, 0x39,             # Hat switch (section 4.3)
    0x81, 0x42,             # Variable input, null state
    0x65, 0x00,             # No units
    0x95, 0x01,             # 1 report field (empty upper nibble)
    0x81, 0x01,             # Array input
    # Joystick (4 bytes)
    0x26, 0xFF, 0x00,       # 0-255 for analog sticks
    0x46, 0xFF, 0x00,
    0x09, 0x30,             # X (left X)
    0x09, 0x31,             # Y (left Y)
    0x09, 0x32,             # Z (right X)
    0x09, 0x35,             # Rz (right Y)
    0x75, 0x08,             # 1 byte per report field
    0x95, 0x04,             # 4 report fields (left X, left Y, right X, right Y)
    0x81, 0x02,             # Variable input
    0x75, 0x08,             # 1 byte per report field
    0x95, 0x01,             # 1 report field
    0x81, 0x01,             # Array input
    0xC0,
))

gamepad = usb_hid.Device(
    report_descriptor=_HORIPAD_S_DESCRIPTOR,
    usage_page=0x01,           # Generic Desktop Control
    usage=0x05,                # Gamepad
    report_ids=(4,),           # Descriptor uses report ID 4.
    in_report_lengths=(6,),    # This gamepad sends 6 bytes in its report.
    out_report_lengths=(0,),   # It does not receive any reports.
)


# echo 0x0f0d > idVendor
# echo 0x00c1 > idProduct
# echo 0x0572 > bcdDevice
# echo 0x0200 > bcdUSB
# echo 0x00 > bDeviceClass
# echo 0x00 > bDeviceSubClass
# echo 0x00 > bDeviceProtocol

# mkdir -p strings/0x409
# echo "" > strings/0x409/serialnumber
# echo "HORI CO.,LTD." > strings/0x409/manufacturer
# echo "HORIPAD S" > strings/0x409/product

# mkdir -p configs/c.1/strings/0x409
# echo "HORI Controller" > configs/c.1/strings/0x409/configuration
# echo 500 > configs/c.1/MaxPower
# echo 0x80 > configs/c.1/bmAttributes

# mkdir -p functions/hid.usb0
# echo 1 > functions/hid.usb0/protocol
# echo 0 > functions/hid.usb0/subclass
# echo 64 > functions/hid.usb0/report_length
# echo -ne \\x5\\x1\\x9\\x5\\xa1\\x1\\x15\\x0\\x25\\x1\\x35\\x0\\x45\\x1\\x75\\x1\\x95\\xe\\x5\\x9\\x19\\x1\\x29\\xb\\x81\\x2\\x95\\x2\\x81\\x1\\x5\\x1\\x25\\x7\\x46\\x3b\\x1\\x75\\x4\\x95\\x1\\x65\\x14\\x9\\x39\\x81\\x42\\x65\\x0\\x95\\x1\\x81\\x1\\x26\\xff\\x0\\x46\\xff\\x0\\x9\\x30\\x9\\x31\\x9\\x32\\x9\\x35\\x75\\x8\\x95\\x4\\x81\\x2\\x75\\x8\\x95\\x1\\x81\\x1\\xc0 > functions/hid.usb0/report_desc
