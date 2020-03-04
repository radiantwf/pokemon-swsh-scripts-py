import argparse
import serial
import time
from time import sleep
import datetime

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
times = 0

print(f'[{datetime.datetime.now()}] 启动脚本')
try:
    while True:
        # 人物移动
        send('LX MAX', 3)
        sleep(0.5)
        send('LX MIN', 3.07)
        sleep(0.5)
        # 调整角度
        send('LY MIN', 0.1)
        sleep(0.5)

        # 取蛋
        send('Button A', 0.1)
        sleep(0.8)
        if times % 5 == 0:
            # 拒蛋
            send('Button B', 0.1)
            sleep(0.8)
            send('Button B', 0.1)
            sleep(0.8)
            send('Button B', 0.1)
        else:
            send('Button A', 0.1)
            sleep(0.8)
            delay = 0
            while delay < 8:
                send('Button B', 0.1)
                sleep(0.9)
                delay = delay + 1
        sleep(1)
        times = times + 1
        
except KeyboardInterrupt:
    send('RELEASE')

print(f'[{datetime.datetime.now()}] 脚本运行结束，执行了{times}次取蛋动作')
ser.close()
