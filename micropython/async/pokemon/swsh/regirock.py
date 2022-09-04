from customize.ns_joystick import NSJoystick
import pokemon.swsh.swsh_common
import pokemon.common
import uasyncio


async def run(restart=False, delay=3):
    try:
        joystick = NSJoystick()
        joystick.uart()
        try:
            await pokemon.common.delay(joystick, delay)
            print("开始运行控制器脚本")
            if restart:
                await pokemon.swsh.swsh_common.restart_game(joystick)
            while True:
                await joystick.send('Button A', 0.1)
                await uasyncio.sleep(1)
                await joystick.send('Button A', 0.1)
                await uasyncio.sleep(1.2)
                await joystick.send('Button A', 0.1)
                await pokemon.swsh.swsh_common.enterBattleAndCheckShiny(joystick, delay=7)
                await joystick.send('Button A', 0.1)
                await uasyncio.sleep(0.5)
                await joystick.send('LX MIN', 3)
                await uasyncio.sleep(1)
                await joystick.send('LY MIN', 3)
                await uasyncio.sleep(0.5)
                await joystick.send('LY MIN', 0.3)
                await uasyncio.sleep(1)
                await joystick.send('LX MIN', 0.3)
                await uasyncio.sleep(2)
                await joystick.send('LY MAX', 1.72)
                await uasyncio.sleep(1)
                await joystick.send('LX MAX', 2.5)
                await uasyncio.sleep(2)
                await joystick.send('LY MIN', 0.52)
                await uasyncio.sleep(1)
                await joystick.send('LX MIN', 2.1)
                await uasyncio.sleep(2)
                await joystick.send('LY MIN', 0.52)
                await uasyncio.sleep(1)
                await joystick.send('LX MAX', 2.7)
                await uasyncio.sleep(3)
                await joystick.send('Button A', 0.1)
                await uasyncio.sleep(1)
                await joystick.send('LX MIN', 0.5)
                await uasyncio.sleep(0.2)
                await joystick.send('LY MIN', 1)
                await uasyncio.sleep(0.2)
        except KeyboardInterrupt as e:
            await joystick.send('RELEASE')
            raise e
    except Exception as e:
        raise e
