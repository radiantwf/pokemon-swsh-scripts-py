import poke_swsh_common
from time import sleep


def run(delay=3):
    uart = poke_swsh_common.uart()
    try:
        poke_swsh_common.delay(uart, delay)
        sleep(1)
        while True:
            poke_swsh_common.send(uart, 'Button A', 0.1)
            sleep(1)
            poke_swsh_common.send(uart, 'Button A', 0.1)
            sleep(1.2)
            poke_swsh_common.send(uart, 'Button A', 0.1)
            poke_swsh_common.enterBattleAndCheckShiny(uart, 7)
            poke_swsh_common.send(uart, 'Button A', 0.1)
            sleep(0.5)
            poke_swsh_common.send(uart, 'LX MIN', 3)
            sleep(1)
            poke_swsh_common.send(uart, 'LY MIN', 3)
            sleep(0.5)
            poke_swsh_common.send(uart, 'LY MIN', 0.3)
            sleep(1)
            poke_swsh_common.send(uart, 'LX MIN', 0.3)
            sleep(2)
            poke_swsh_common.send(uart, 'LY MAX', 1.72)
            sleep(1)
            poke_swsh_common.send(uart, 'LX MAX', 2.5)
            sleep(2)
            poke_swsh_common.send(uart, 'LY MIN', 0.52)
            sleep(1)
            poke_swsh_common.send(uart, 'LX MIN', 2.5)
            sleep(2)
            poke_swsh_common.send(uart, 'LY MIN', 0.52)
            sleep(1)
            poke_swsh_common.send(uart, 'LX MAX', 2.5)
            sleep(3)
            poke_swsh_common.send(uart, 'Button A', 0.1)
            sleep(1)
            poke_swsh_common.send(uart, 'LY MIN', 1)
            sleep(0.2)
    except KeyboardInterrupt:
        poke_swsh_common.send(uart, 'RELEASE')
