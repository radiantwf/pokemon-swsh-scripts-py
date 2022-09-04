import pokemon.poke_swsh_common
import customize.datetime
from time import sleep


def run(date=1, maxDate=31, isSecondary=True, delay=3.0):
    uart = pokemon.poke_swsh_common.uart()
    try:
        pokemon.poke_swsh_common.delay(uart, delay)

        while (True):
            pokemon.poke_swsh_common.openGame(uart, isSecondary)

            times = 0
            invalidDate = False
            while (times < 4):
                if (times == 0) or invalidDate:
                    pokemon.poke_swsh_common.gotoRaid(
                        uart, isOnline=False, hasWatts=False)
                else:
                    pokemon.poke_swsh_common.gotoRaid(
                        uart, isOnline=False, hasWatts=True)

                if times != 3:
                    # 点击 大家一起挑战
                    pokemon.poke_swsh_common.send(uart, 'Button A', 0.1)
                    sleep(3)

                    pokemon.poke_swsh_common.gotoHome(uart)
                    pokemon.poke_swsh_common.gotocustomize.datetimeSettingFromHome(
                        uart)
                    pokemon.poke_swsh_common.initialAddOneDay(uart)

                    date += 1
                    if date > maxDate:
                        date = 1
                        invalidDate = True
                    else:
                        times += 1
                        invalidDate = False

                    pokemon.poke_swsh_common.returnGame(uart)

                    # 取消团战
                    pokemon.poke_swsh_common.send(uart, 'Button B', 0.1)
                    sleep(1)
                    pokemon.poke_swsh_common.send(uart, 'Button A', 0.1)
                    sleep(5)
                else:
                    times += 1
                    sleep(15)
            pokemon.poke_swsh_common.closeGame(uart)
    except KeyboardInterrupt:
        pokemon.poke_swsh_common.send(uart, 'RELEASE')
