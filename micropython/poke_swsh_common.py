from machine import UART
from time import sleep
import datetime

def send(uart, msg, duration=0):
    uart.write("%s\r\n"%(msg))
    sleep(duration)
    uart.write(b'RELEASE\r\n')
    print("[%s] %s" % (datetime.now(),msg))

def getUart():
    uart = UART(2, baudrate=9600)
    return uart
    
def delay(uart,second=3.0):
    print("[%s] %d秒延时" % (datetime.now(),second))
    send(uart,'Button LCLICK', 0.05)
    sleep(second)
    send(uart,'Button LCLICK', 0.05)
    sleep(0.05)

def enterTimeSetting(uart):
    # 进入设置界面
    send(uart,'LY MAX', 0.05)
    sleep(0.05)
    send(uart,'LX MAX', 0.05)
    sleep(0.05)
    send(uart,'LX MAX', 0.05)
    sleep(0.05)
    send(uart,'LX MAX', 0.05)
    sleep(0.05)
    send(uart,'LX MAX', 0.05)
    sleep(0.05)
    send(uart,'Button A', 0.05)
    sleep(1)

    # 进入时间设置界面
    for num in range(0,14):
        send(uart,'LY MAX', 0.05)
        sleep(0.05)
    sleep(0.05)
    send(uart,'Button A', 0.05)
    sleep(1)
    send(uart,'LY MAX', 0.05)
    sleep(0.05)
    send(uart,'LY MAX', 0.05)
    sleep(0.05)
    send(uart,'LY MAX', 0.05)
    sleep(0.05)
    send(uart,'LY MAX', 0.05)
    sleep(0.05)
    send(uart,'Button A', 0.05)
    sleep(1)
    send(uart,'LY MAX', 0.05)
    sleep(0.05)
    send(uart,'LY MAX', 0.05)
    sleep(0.05)

def firstAddDate(uart,day):
    # 进入设置界面
    send(uart,'Button A', 0.05)
    sleep(0.5)

    # 首次修改日期
    send(uart,'Button A', 0.05)
    sleep(0.05)
    send(uart,'Button A', 0.05)
    sleep(0.05)
    send(uart,'LY MIN', 0.05)
    sleep(0.05)
    send(uart,'Button A', 0.05)
    sleep(0.05)
    send(uart,'Button A', 0.05)
    sleep(0.05)
    send(uart,'Button A', 0.05)
    sleep(0.05)
    send(uart,'Button A', 0.05)
    sleep(0.3)
    day[0] += 1