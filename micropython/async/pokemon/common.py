import customize.datetime
import uasyncio


async def delay(joystick, delay=3.0):
    if delay == 0:
        return
    print("[%s] %d秒延时" % (customize.datetime.now(), delay))
    await joystick.send('Button LCLICK', 0.05)
    await uasyncio.sleep(delay)
    await joystick.send('Button LCLICK', 0.05)
    await uasyncio.sleep(0.05)


# 进入Home界面


async def gotoHome(joystick):
    await joystick.send('Button HOME', 0.1)
    await uasyncio.sleep(2)

# 返回游戏界面


async def returnGame(joystick):
    await joystick.send('Button HOME', 0.1)
    await uasyncio.sleep(2)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(1.5)

# 关闭游戏


async def closeGame(joystick):
    await joystick.send('Button HOME', 0.1)
    await uasyncio.sleep(1.5)
    await joystick.send('Button X', 0.1)
    await uasyncio.sleep(0.5)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(5)
