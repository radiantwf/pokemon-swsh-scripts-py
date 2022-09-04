import pokemon.poke_swsh_common
from time import sleep


def run(delay=3):
    uart = pokemon.poke_swsh_common.uart()
    try:
        pokemon.poke_swsh_common.delay(uart, delay)
        sleep(1)
        while True:
            pokemon.poke_swsh_common.send(uart, 'Button A', 0.1)
            sleep(1)
            pokemon.poke_swsh_common.send(uart, 'Button A', 0.1)
            sleep(1.2)
            pokemon.poke_swsh_common.send(uart, 'Button A', 0.1)
            pokemon.poke_swsh_common.enterBattleAndCheckShiny(uart, 7)
            pokemon.poke_swsh_common.send(uart, 'Button A', 0.1)
            sleep(0.5)
            pokemon.poke_swsh_common.send(uart, 'LX MIN', 3)
            sleep(1)
            pokemon.poke_swsh_common.send(uart, 'LY MIN', 3)
            sleep(0.5)
            pokemon.poke_swsh_common.send(uart, 'LY MIN', 0.3)
            sleep(1)
            pokemon.poke_swsh_common.send(uart, 'LX MIN', 0.3)
            sleep(2)
            pokemon.poke_swsh_common.send(uart, 'LY MAX', 1.72)
            sleep(1)
            pokemon.poke_swsh_common.send(uart, 'LX MAX', 2.5)
            sleep(2)
            pokemon.poke_swsh_common.send(uart, 'LY MIN', 0.52)
            sleep(1)
            pokemon.poke_swsh_common.send(uart, 'LX MIN', 2.5)
            sleep(2)
            pokemon.poke_swsh_common.send(uart, 'LY MIN', 0.52)
            sleep(1)
            pokemon.poke_swsh_common.send(uart, 'LX MAX', 2.5)
            sleep(3)
            pokemon.poke_swsh_common.send(uart, 'Button A', 0.1)
            sleep(1)
            pokemon.poke_swsh_common.send(uart, 'LY MIN', 1)
            sleep(0.2)
    except KeyboardInterrupt:
        pokemon.poke_swsh_common.send(uart, 'RELEASE')
