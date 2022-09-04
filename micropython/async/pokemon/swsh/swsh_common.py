import uasyncio
import pokemon.common


async def restart_game(joystick):
    await pokemon.common.closeGame(joystick)
    await openGame(joystick, isSecondary=True)


# 启动游戏


async def openGame(joystick, isSecondary=False):
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(1.5)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(15)
    if isSecondary:
        await uasyncio.sleep(5)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(1)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(1)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(7)

# 保存进度


async def save(joystick):
    await joystick.send('Button X', 0.1)
    await uasyncio.sleep(1.5)
    await joystick.send('Button R', 0.1)
    await uasyncio.sleep(1.5)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(4)

# 开启团战界面


async def gotoRaid(joystick, isOnline=True, hasWatts=False):
    if hasWatts:
        await joystick.send('Button A', 0.1)
        if isOnline:
            await uasyncio.sleep(1)
        await uasyncio.sleep(0.8)
        await joystick.send('Button A', 0.1)
        await uasyncio.sleep(0.8)
    await joystick.send('Button A', 0.1)
    if isOnline:
        await uasyncio.sleep(7)
    await uasyncio.sleep(2.5)

# 设置团战密码22223333


async def setRaidPassword(joystick):
    await joystick.send('Button START', 0.1)
    await uasyncio.sleep(1)
    # 设置密码2233
    await joystick.send('LX MAX', 0.1)
    await uasyncio.sleep(0.5)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(0.4)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(0.4)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(0.4)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(0.4)
    await joystick.send('LX MAX', 0.1)
    await uasyncio.sleep(0.5)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(0.4)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(0.4)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(0.4)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(0.4)
    await joystick.send('Button START', 0.1)
    await uasyncio.sleep(1)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(1)

# 开启团战并等待其他玩家加入


async def waitForRaid(joystick):
    # 大家一起挑战
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(10)
    # 等待
    await joystick.send('LY Min', 0.1)
    await uasyncio.sleep(90)

# 进行团战


async def raid(joystick):
    for num in range(0, 20):
        await joystick.send('Button A', 0.1)
        await uasyncio.sleep(1)

# 切换到互联网模式


async def onlineModel(joystick):
    await joystick.send('Button Y', 0.1)
    await uasyncio.sleep(1)
    await joystick.send('Button START', 0.1)
    await uasyncio.sleep(30)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(1)
    await joystick.send('Button B', 0.1)
    await uasyncio.sleep(2)

# 切换到本地模式


async def localModel(joystick):
    await joystick.send('Button Y', 0.1)
    await uasyncio.sleep(1)
    await joystick.send('Button START', 0.1)
    await uasyncio.sleep(0.5)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(5)
    await joystick.send('Button B', 0.1)
    await uasyncio.sleep(0.5)
    await joystick.send('Button B', 0.1)
    await uasyncio.sleep(1)

# 切换互联网，防止副机强制退出游戏


async def switchNetMode(joystick):
    await joystick.send('Button Y', 0.1)
    await uasyncio.sleep(1)
    await joystick.send('Button START', 0.1)
    await uasyncio.sleep(60)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(1)
    await joystick.send('Button START', 0.1)
    await uasyncio.sleep(0.5)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(5)
    await joystick.send('Button B', 0.1)
    await uasyncio.sleep(0.5)
    await joystick.send('Button B', 0.1)
    await uasyncio.sleep(1.5)

# 进入时间设置界面


async def gotoDatetimeSettingFromHome(joystick):
    # 进入设置界面
    await joystick.send('LY MAX', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('LX MAX', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('LX MAX', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('LX MAX', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('LX MAX', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('LX MAX', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(1)

    # 进入时间设置界面
    for num in range(0, 14):
        await joystick.send('LY MAX', 0.05)
        await uasyncio.sleep(0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(1)
    await joystick.send('LY MAX', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('LY MAX', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('LY MAX', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('LY MAX', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(1)
    await joystick.send('LY MAX', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('LY MAX', 0.05)
    await uasyncio.sleep(0.05)

# 首次修改日期


async def initialAddOneDay(joystick):
    # 进入设置界面
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(0.5)

    # 首次修改日期
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('LY MIN', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(0.12)

# 后续修改日期


async def followingAddOneDay(joystick):
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(0.12)
    await joystick.send('LX MIN', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('LX MIN', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('LX MIN', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('LY MIN', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(0.05)
    await joystick.send('Button A', 0.05)
    await uasyncio.sleep(0.12)

# 进入战斗并且检查闪（必须使用不闪逃跑特性高敏精灵）


async def enterBattleAndCheckShiny(joystick, delay=0):
    await uasyncio.sleep(delay)
    await uasyncio.sleep(7.5)
    await joystick.send('LY MAX', 0.1)
    await uasyncio.sleep(0.1)
    await joystick.send('LY MAX', 0.1)
    await uasyncio.sleep(1.6)
    await joystick.send('LY MAX', 0.1)
    await uasyncio.sleep(0.5)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(1.5)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(0.8)
    await joystick.send('LY MAX', 0.1)
    await uasyncio.sleep(0.3)
    await joystick.send('Button A', 0.1)
    await uasyncio.sleep(5)
