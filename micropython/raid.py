from machine import UART
from time import sleep
import datetime
print(datetime.now())
def send(uart, msg, duration=0):
    uart.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    uart.write(b'RELEASE\r\n')

def raid(delay=3):
    uart = UART(2, baudrate=115200, rx=13,tx=12,timeout=10)
    print(f'[{datetime.now()}] {delay}秒延时（--delay参数设定）')
    send('Button LCLICK', 0.1)
    sleep(delay)
    send('Button LCLICK', 0.1)
    sleep(1)
    print(f'[{datetime.now()}] 启动脚本')

    times = 0
    try:
        while True:
            # 启动游戏
            send('Button A', 0.1)
            sleep(1.5)
            send('Button A', 0.1)
            sleep(20)
            send('Button A', 0.1)
            sleep(6)

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
            for num in range(0,20):
                send('Button A', 0.1)
                sleep(1)

            # 关闭游戏
            send('Button HOME', 0.1)
            sleep(1.5)
            send('Button X', 0.1)
            sleep(0.5)
            send('Button A', 0.1)
            sleep(5)

            times = times + 1
            print(f'[{datetime.now()}] 脚本运行中，已开启了{times}次团战')
            
    except KeyboardInterrupt:
        send('RELEASE')