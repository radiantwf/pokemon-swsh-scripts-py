import pokemon.poke_swsh_common
from time import sleep


def run(restart_game=False, delay=3):
    uart = pokemon.poke_swsh_common.uart()
    try:
        pokemon.poke_swsh_common.delay(uart, delay)
        sleep(1)
        if restart_game:
            pokemon.poke_swsh_common.restart_game(uart)
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
            pokemon.poke_swsh_common.send(uart, 'LX MAX', 3)
            sleep(3)
            pokemon.poke_swsh_common.send(uart, 'Button A', 0.1)
            sleep(1)
            pokemon.poke_swsh_common.send(uart, 'LX MIN', 0.5)
            sleep(0.2)
            pokemon.poke_swsh_common.send(uart, 'LY MIN', 1)
            sleep(0.2)
    except KeyboardInterrupt:
        pokemon.poke_swsh_common.send(uart, 'RELEASE')
