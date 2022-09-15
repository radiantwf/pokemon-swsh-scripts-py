#!/bin/bash
esptool.py --port /dev/cu.SLAB_USBtoUART --chip esp32s3 --baud 921600 \
    erase_flash && \
esptool.py --port /dev/cu.SLAB_USBtoUART --chip esp32s3 --baud 921600 \
    --before=default_reset --after=hard_reset \
    write_flash --flash_mode qio --flash_freq 80m --flash_size 16MB \
    0x0 build/firmware.bin