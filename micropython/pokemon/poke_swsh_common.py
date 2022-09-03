from machine import UART
from time import sleep
import datetime


def send(uart, msg, duration=0, debug=False):
    uart.write("%s\r\n" % (msg))
    sleep(duration)
    uart.write(b'RELEASE\r\n')
    if debug:
        print("[%s] %s" % (datetime.now(), msg))


def uart():
    import datetime
    datetime.ntpSync()
    from machine import Pin
    u = UART(1, baudrate=9600, tx=17, rx=16)
    return u


def delay(uart, delay=3.0):
    if delay == 0:
        return
    print("[%s] %d秒延时" % (datetime.now(), delay))
    send(uart, 'Button LCLICK', 0.05)
    sleep(delay)
    send(uart, 'Button LCLICK', 0.05)
    sleep(0.05)


def restart_game(uart):
    closeGame(uart)
    openGame(uart, isSecondary=True)

# 进入Home界面


def gotoHome(uart):
    send(uart, 'Button HOME', 0.1)
    sleep(2)

# 返回游戏界面


def returnGame(uart):
    send(uart, 'Button HOME', 0.1)
    sleep(2)
    send(uart, 'Button A', 0.1)
    sleep(1.5)

# 启动游戏


def openGame(uart, isSecondary=False):
    send(uart, 'Button A', 0.1)
    sleep(1.5)
    send(uart, 'Button A', 0.1)
    sleep(15)
    if isSecondary:
        sleep(5)
    send(uart, 'Button A', 0.1)
    sleep(1)
    send(uart, 'Button A', 0.1)
    sleep(1)
    send(uart, 'Button A', 0.1)
    sleep(7)

# 关闭游戏


def closeGame(uart):
    send(uart, 'Button HOME', 0.1)
    sleep(1.5)
    send(uart, 'Button X', 0.1)
    sleep(0.5)
    send(uart, 'Button A', 0.1)
    sleep(5)

# 保存进度


def save(uart):
    send(uart, 'Button X', 0.1)
    sleep(1.5)
    send(uart, 'Button R', 0.1)
    sleep(1.5)
    send(uart, 'Button A', 0.1)
    sleep(4)

# 开启团战界面


def gotoRaid(uart, isOnline=True, hasWatts=False):
    if hasWatts:
        send(uart, 'Button A', 0.1)
        if isOnline:
            sleep(1)
        sleep(0.8)
        send(uart, 'Button A', 0.1)
        sleep(0.8)
    send(uart, 'Button A', 0.1)
    if isOnline:
        sleep(7)
    sleep(2.5)

# 设置团战密码22223333


def setRaidPassword(uart):
    send(uart, 'Button START', 0.1)
    sleep(1)
    # 设置密码2233
    send(uart, 'LX MAX', 0.1)
    sleep(0.5)
    send(uart, 'Button A', 0.1)
    sleep(0.4)
    send(uart, 'Button A', 0.1)
    sleep(0.4)
    send(uart, 'Button A', 0.1)
    sleep(0.4)
    send(uart, 'Button A', 0.1)
    sleep(0.4)
    send(uart, 'LX MAX', 0.1)
    sleep(0.5)
    send(uart, 'Button A', 0.1)
    sleep(0.4)
    send(uart, 'Button A', 0.1)
    sleep(0.4)
    send(uart, 'Button A', 0.1)
    sleep(0.4)
    send(uart, 'Button A', 0.1)
    sleep(0.4)
    send(uart, 'Button START', 0.1)
    sleep(1)
    send(uart, 'Button A', 0.1)
    sleep(1)

# 开启团战并等待其他玩家加入


def waitForRaid(uart):
    # 大家一起挑战
    send(uart, 'Button A', 0.1)
    sleep(10)
    # 等待
    send(uart, 'LY Min', 0.1)
    sleep(90)

# 进行团战


def raid(uart):
    for num in range(0, 20):
        send(uart, 'Button A', 0.1)
        sleep(1)

# 切换到互联网模式


def onlineModel(uart):
    send(uart, 'Button Y', 0.1)
    sleep(1)
    send(uart, 'Button START', 0.1)
    sleep(30)
    send(uart, 'Button A', 0.1)
    sleep(1)
    send(uart, 'Button B', 0.1)
    sleep(2)

# 切换到本地模式


def localModel(uart):
    send(uart, 'Button Y', 0.1)
    sleep(1)
    send(uart, 'Button START', 0.1)
    sleep(0.5)
    send(uart, 'Button A', 0.1)
    sleep(5)
    send(uart, 'Button B', 0.1)
    sleep(0.5)
    send(uart, 'Button B', 0.1)
    sleep(1)

# 切换互联网，防止副机强制退出游戏


def switchNetMode(uart):
    send(uart, 'Button Y', 0.1)
    sleep(1)
    send(uart, 'Button START', 0.1)
    sleep(60)
    send(uart, 'Button A', 0.1)
    sleep(1)
    send(uart, 'Button START', 0.1)
    sleep(0.5)
    send(uart, 'Button A', 0.1)
    sleep(5)
    send(uart, 'Button B', 0.1)
    sleep(0.5)
    send(uart, 'Button B', 0.1)
    sleep(1.5)

# 进入时间设置界面


def gotoDatetimeSettingFromHome(uart):
    # 进入设置界面
    send(uart, 'LY MAX', 0.05)
    sleep(0.05)
    send(uart, 'LX MAX', 0.05)
    sleep(0.05)
    send(uart, 'LX MAX', 0.05)
    sleep(0.05)
    send(uart, 'LX MAX', 0.05)
    sleep(0.05)
    send(uart, 'LX MAX', 0.05)
    sleep(0.05)
    send(uart, 'LX MAX', 0.05)
    sleep(0.05)
    send(uart, 'Button A', 0.05)
    sleep(1)

    # 进入时间设置界面
    for num in range(0, 14):
        send(uart, 'LY MAX', 0.05)
        sleep(0.05)
    sleep(0.05)
    send(uart, 'Button A', 0.05)
    sleep(1)
    send(uart, 'LY MAX', 0.05)
    sleep(0.05)
    send(uart, 'LY MAX', 0.05)
    sleep(0.05)
    send(uart, 'LY MAX', 0.05)
    sleep(0.05)
    send(uart, 'LY MAX', 0.05)
    sleep(0.05)
    send(uart, 'Button A', 0.05)
    sleep(1)
    send(uart, 'LY MAX', 0.05)
    sleep(0.05)
    send(uart, 'LY MAX', 0.05)
    sleep(0.05)

# 首次修改日期


def initialAddOneDay(uart):
    # 进入设置界面
    send(uart, 'Button A', 0.05)
    sleep(0.5)

    # 首次修改日期
    send(uart, 'Button A', 0.05)
    sleep(0.05)
    send(uart, 'Button A', 0.05)
    sleep(0.05)
    send(uart, 'LY MIN', 0.05)
    sleep(0.05)
    send(uart, 'Button A', 0.05)
    sleep(0.05)
    send(uart, 'Button A', 0.05)
    sleep(0.05)
    send(uart, 'Button A', 0.05)
    sleep(0.05)
    send(uart, 'Button A', 0.05)
    sleep(0.12)

# 后续修改日期


def followingAddOneDay(uart):
    send(uart, 'Button A', 0.05)
    sleep(0.12)
    send(uart, 'LX MIN', 0.05)
    sleep(0.05)
    send(uart, 'LX MIN', 0.05)
    sleep(0.05)
    send(uart, 'LX MIN', 0.05)
    sleep(0.05)
    send(uart, 'LY MIN', 0.05)
    sleep(0.05)
    send(uart, 'Button A', 0.05)
    sleep(0.05)
    send(uart, 'Button A', 0.05)
    sleep(0.05)
    send(uart, 'Button A', 0.05)
    sleep(0.05)
    send(uart, 'Button A', 0.05)
    sleep(0.12)

# 进入战斗并且检查闪（必须使用不闪逃跑特性高敏精灵）


def enterBattleAndCheckShiny(uart, delay=0):
    sleep(delay)
    sleep(7.5)
    send(uart, 'LY MAX', 0.1)
    sleep(0.1)
    send(uart, 'LY MAX', 0.1)
    sleep(1.6)
    send(uart, 'LY MAX', 0.1)
    sleep(0.5)
    send(uart, 'Button A', 0.1)
    sleep(1.5)
    send(uart, 'Button A', 0.1)
    sleep(0.8)
    send(uart, 'LY MAX', 0.1)
    sleep(0.3)
    send(uart, 'Button A', 0.1)
    sleep(5)
