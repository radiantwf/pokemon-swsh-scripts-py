import argparse
import serial
import time
import math
from time import sleep
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('port')
parser.add_argument('--delay', type=int, default=3)
parser.add_argument('--flamebody', type=bool, default=True)
parser.add_argument('--cycles', type=int, default=20)
parser.add_argument('--init-col', type=int, default=0)
parser.add_argument('--max-box', type=int, default=0)
parser.add_argument('--max-col', type=int, default=5)
args = parser.parse_args()

if args.flamebody:
    steps = math.ceil(257 * args.cycles / 2)
    cycles = math.ceil(args.cycles / 2)
else:
    steps = 257 * args.cycles
    cycles = args.cycles

def send(msg, duration=0):
    # now = datetime.datetime.now()
    # print(f'[{now}] {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

# 准备工作
# 选项卡界面 把【宝可梦】图标调整到第一个位置，并把光标移动到【宝可梦】处
# 同行宝可梦带满，并且要孵蛋的箱子起始列必须全部为空的状态

ser = serial.Serial(args.port, 9600)

print(f'[{datetime.datetime.now()}] {args.delay}秒延时（--delay参数设定）')
print(f'[{datetime.datetime.now()}] 孵化周期：{args.cycles}，孵化步数：{steps}')
print(f'[{datetime.datetime.now()}] 起始列：{args.init_col}，终止箱子数：{args.max_box}，终止列：{args.max_col}')
send('Button LCLICK', 0.1)
sleep(args.delay)
send('Button LCLICK', 0.1)
sleep(1)
print(f'[{datetime.datetime.now()}] 启动脚本')

col = args.init_col
try:
    box = 0
    while True:
        # 进入盒子
        send('Button X', 0.1)
        sleep(1)
        send('Button A', 0.1)
        sleep(1.4)
        send('Button R', 0.1)
        sleep(1.6)
        
        # 选择范围移动
        send('Button Y', 0.1)
        sleep(0.2)
        send('Button Y', 0.1)
        sleep(0.2)
        
        # 移动光标到同行第二只宝可梦，然后选择2-6宝可梦
        send('LX MIN', 0.1)
        sleep(0.15)
        send('LY MAX', 0.1)
        sleep(0.15)
        send('Button A', 0.1)
        sleep(0.3)
        send('LY MAX', 0.1)
        sleep(0.15)
        send('LY MAX', 0.1)
        sleep(0.15)
        send('LY MAX', 0.1)
        sleep(0.15)
        send('LY MAX', 0.1)
        sleep(0.15)
        send('Button A', 0.1)
        sleep(0.5)

        # 移动光标到0行col列
        send('LY MIN', 0.1)
        sleep(0.15)
        for num in range(0, col + 1): 
            send('LX MAX', 0.1)
            sleep(0.15)
        # 放下移动宝可梦
        send('Button A', 0.1)
        sleep(0.5)
        
        # 光标移动到要孵的蛋的位置
        col = col + 1
        if col > 5 :
            col = 0
            send('Button R', 0.1)
            sleep(0.5)
            send('LX MIN', 0.1)
            sleep(0.15)
            send('LX MIN', 0.1)
            sleep(0.15)
            send('LX MIN', 0.1)
            sleep(0.15)
            send('LX MIN', 0.1)
            sleep(0.15)
            send('LX MIN', 0.1)
            sleep(0.15)
            box = box + 1
        else:
            send('LX MAX', 0.1)
            sleep(0.15)

        # 选中要孵的蛋
        send('Button A', 0.1)
        sleep(0.15)
        send('LY MAX', 0.1)
        sleep(0.15)
        send('LY MAX', 0.1)
        sleep(0.15)
        send('LY MAX', 0.1)
        sleep(0.15)
        send('LY MAX', 0.1)
        sleep(0.15)
        send('Button A', 0.1)
        sleep(0.5)

        # 移动光标到同行第二只宝可梦，然后放下宝可梦
        for num in range(0, col + 1): 
            send('LX MIN', 0.1)
            sleep(0.15)
        send('LY MAX', 0.1)
        sleep(0.15)
        send('Button A', 0.1)
        sleep(0.3)

        # 退出盒子
        send('Button B', 0.1)
        sleep(1.6)
        send('Button B', 0.1)
        sleep(1.4)
        send('Button B', 0.1)
        sleep(1.2)

        # 人物移动
        for num in range(0, cycles): 
            send('LX MAX', 3.8)
            sleep(0.2)
            send('LX MIN', 3.8)
            sleep(0.2)
            
        # 孵化
        for num in range(0, 5): 
            if num % 2 == 0:
                send('LX MAX', 0.3)
            else:
                send('LX MIN', 0.3)
            sleep(0.5)
            for delay in range(0, 18): 
                send('Button B', 0.1)
                sleep(1)

        # 调整人物位置
        send('LX MIN', 3.8)
        sleep(0.5)
        send('LY MIN', 0.3)
        sleep(0.2)

        if col == 0:
            print(f'[{datetime.datetime.now()}] 脚本运行中，孵蛋到第{box}箱，共{args.max_box}箱，{args.max_col}列')
            if box % 3 == 2:
                # 保存进度
                send('Button X', 0.1)
                sleep(1.5)
                send('Button R', 0.1)
                sleep(1.5)
                send('Button A', 0.1)
                sleep(4)
                # 切换互联网，防止副机强制退出游戏
                send('Button Y', 0.1)
                sleep(1)
                send('Button START', 0.1)
                sleep(60)
                send('Button A', 0.1)
                sleep(1)
                send('Button START', 0.1)
                sleep(0.5)
                send('Button A', 0.1)
                sleep(5)
                send('Button B', 0.1)
                sleep(0.5)
                send('Button B', 0.1)
                sleep(1.5)

        # 判断是否完成
        if box > args.max_box or (box == args.max_box and col >= args.max_col):
            break
        
except KeyboardInterrupt:
    send('RELEASE')

print(f'[{datetime.datetime.now()}] 脚本运行结束，成功孵蛋到第{box}箱，{col}列')
ser.close()
