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
send('Button LCLICK', 0.1)
sleep(1)
print(f'[{datetime.datetime.now()}] 启动脚本')

try:
    # 连接网络
    send('Button Y', 0.1)
    sleep(1)
    send('Button START', 0.1)
    sleep(30)
    send('Button A', 0.1)
    sleep(1)
    send('Button B', 0.1)
    sleep(1)

    # 团战
    send('Button A', 0.1)
    sleep(8)
    send('Button START', 0.1)
    sleep(1)
    # 设置密码2233
    send('LX MAX', 0.1)
    sleep(0.5)
    send('Button A', 0.1)
    sleep(0.4)
    send('Button A', 0.1)
    sleep(0.4)
    send('LX MAX', 0.1)
    sleep(0.5)
    send('Button A', 0.1)
    sleep(0.4)
    send('Button A', 0.1)
    sleep(0.4)
    send('Button START', 0.1)
    sleep(1)
    send('Button A', 0.1)
    sleep(1)

    # 大家一起挑战
    send('Button A', 0.1)
    sleep(10)
    send('LY Min', 0.1)
    sleep(90)

    # 开始
    for num in range(0,17):
        send('Button A', 0.1)
        sleep(1)
    
    # 休眠
    send('Button HOME', 2)
    sleep(0.5)
    send('Button A', 0.1)
    
except KeyboardInterrupt:
    send('RELEASE')

ser.close()
