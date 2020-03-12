import argparse
import serial
import time
from time import sleep
import datetime

# 启动脚本前把系统时间调整到4月1日

parser = argparse.ArgumentParser()
parser.add_argument('port')
parser.add_argument('--delay', type=int, default=3)
args = parser.parse_args()

def send(msg, duration=0):
    # now = datetime.datetime.now()
    # print(f'[{now}] {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

ser = serial.Serial(args.port, 9600)

print(f'[{datetime.datetime.now()}] {args.delay}秒延时（--delay参数设定）')
send('Button LCLICK', 0.1)
sleep(args.delay)
date = 1
times = 0
print(f'[{datetime.datetime.now()}] 启动脚本')
try:
    while True:
        if date > 1:
            # 获取瓦特
            send('Button A', 0.1)
            sleep(0.8)
            send('Button A', 0.1)
            sleep(0.8)
            send('Button A', 0.1)
            sleep(2.5)
            send('Button B', 0.1)
            sleep(2)

        # 进入主菜单
        send('Button HOME', 0.1)
        sleep(2)

        # 进入设置界面
        send('LY MAX', 0.1)
        sleep(0.1)
        send('LX MAX', 0.08)
        sleep(0.08)
        send('LX MAX', 0.08)
        sleep(0.08)
        send('LX MAX', 0.08)
        sleep(0.08)
        send('LX MAX', 0.08)
        sleep(0.08)
        send('Button A', 0.1)
        sleep(2)

        # 进入时间设置界面
        send('LY MAX', 3)
        sleep(0.1)
        send('Button A', 0.1)
        sleep(1)
        send('LY MAX', 0.1)
        sleep(0.08)
        send('LY MAX', 0.1)
        sleep(0.08)
        send('LY MAX', 0.1)
        sleep(0.08)
        send('LY MAX', 0.1)
        sleep(0.08)
        send('Button A', 0.1)
        sleep(1)
        send('LY MAX', 0.1)
        sleep(0.08)
        send('LY MAX', 0.1)
        sleep(0.08)
        send('Button A', 0.1)
        sleep(0.5)

        # 修改日期
        send('Button A', 0.08)
        sleep(0.08)
        send('Button A', 0.08)
        sleep(0.08)
        send('LY MIN', 0.08)
        sleep(0.08)
        send('Button A', 0.08)
        sleep(0.08)
        send('Button A', 0.08)
        sleep(0.08)
        send('Button A', 0.08)
        sleep(0.08)
        send('Button A', 0.08)
        sleep(0.3)
        date = date + 1
        if date > 30:
            date = 1

            # 后续修改日期
            send('Button A', 0.1)
            sleep(0.5)
            send('LX MIN', 0.08)
            sleep(0.08)
            send('LX MIN', 0.08)
            sleep(0.08)
            send('LX MIN', 0.08)
            sleep(0.08)
            send('LY MIN', 0.08)
            sleep(0.08)
            send('Button A', 0.08)
            sleep(0.08)
            send('Button A', 0.08)
            sleep(0.08)
            send('Button A', 0.08)
            sleep(0.08)
            send('Button A', 0.08)
            sleep(0.3)
            times = times + 1
            date = date + 1
        
        # 返回游戏
        send('Button HOME', 0.1)
        sleep(2)

        send('Button A', 0.1)
        sleep(1)

        if times > 1 and date == 2:
            # 保存进度
            send('Button X', 0.1)
            sleep(1.5)
            send('Button R', 0.1)
            sleep(1.5)
            send('Button A', 0.1)
            sleep(4)

except KeyboardInterrupt:
    send('RELEASE')

ser.close()
