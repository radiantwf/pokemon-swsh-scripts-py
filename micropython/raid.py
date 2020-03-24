from machine import UART
from time import sleep
import datetime

def send(uart, msg, duration=0):
    uart.write("%s\r\n"%(msg))
    sleep(duration)
    uart.write(b'RELEASE\r\n')
    print("[%s] %s" % (datetime.now(),msg))

def raid(delay=3):
    uart = UART(2, baudrate=9600)
    print("[%s] %d秒延时（--delay参数设定）" % (datetime.now(),delay))
    send(uart,'Button LCLICK', 0.1)
    sleep(delay)
    send(uart,'Button LCLICK', 0.1)
    sleep(1)
    print("[%s] 启动脚本" % (datetime.now()))

    times = 0
    try:
        while True:
            # 启动游戏
            send(uart,'Button A', 0.1)
            sleep(1.5)
            send(uart,'Button A', 0.1)
            sleep(20)
            send(uart,'Button A', 0.1)
            sleep(6.5)

            # 连接网络
            send(uart,'Button Y', 0.1)
            sleep(1)
            send(uart,'Button START', 0.1)
            sleep(30)
            send(uart,'Button A', 0.1)
            sleep(1)
            send(uart,'Button B', 0.1)
            sleep(1)

            # 团战
            send(uart,'Button A', 0.1)
            sleep(8)
            send(uart,'Button START', 0.1)
            sleep(1)
            # 设置密码2233
            send(uart,'LX MAX', 0.1)
            sleep(0.5)
            send(uart,'Button A', 0.1)
            sleep(0.4)
            send(uart,'Button A', 0.1)
            sleep(0.4)
            send(uart,'LX MAX', 0.1)
            sleep(0.5)
            send(uart,'Button A', 0.1)
            sleep(0.4)
            send(uart,'Button A', 0.1)
            sleep(0.4)
            send(uart,'Button START', 0.1)
            sleep(1)
            send(uart,'Button A', 0.1)
            sleep(1)

            # 大家一起挑战
            send(uart,'Button A', 0.1)
            sleep(10)
            send(uart,'LY Min', 0.1)
            sleep(90)

            # 开始
            for num in range(0,20):
                send(uart,'Button A', 0.1)
                sleep(1)

            # 关闭游戏
            send(uart,'Button HOME', 0.1)
            sleep(1.5)
            send(uart,'Button X', 0.1)
            sleep(0.5)
            send(uart,'Button A', 0.1)
            sleep(5)

            times = times + 1
            print("[%s] 脚本运行中，已开启了%d次团战" % (datetime.now(),times))
            
    except KeyboardInterrupt:
        send(uart,'RELEASE')