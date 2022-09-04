import pokemon.poke_swsh_common
import customize.datetime


def run(isSecondary=True, delay=3):
    uart = pokemon.poke_swsh_common.uart()
    try:
        pokemon.poke_swsh_common.delay(uart, delay)
        times = 0
        while True:
            pokemon.poke_swsh_common.openGame(uart, isSecondary=isSecondary)
            pokemon.poke_swsh_common.onlineModel(uart)
            pokemon.poke_swsh_common.gotoRaid(uart)
            pokemon.poke_swsh_common.setRaidPassword(uart)
            pokemon.poke_swsh_common.waitForRaid(uart)
            pokemon.poke_swsh_common.raid(uart)
            pokemon.poke_swsh_common.closeGame(uart)
            times = times + 1
            print("[%s] 脚本运行中，已开启了%d次团战" % (customize.datetime.now(), times))
    except KeyboardInterrupt:
        pokemon.poke_swsh_common.send(uart, 'RELEASE')
