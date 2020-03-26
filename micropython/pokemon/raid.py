import poke_swsh_common, datetime

def raid(delay=3):
    uart = poke_swsh_common.uart()
    try:
        poke_swsh_common.delay(uart,second)
        times = 0
        while True:
            poke_swsh_common.openGame(uart)
            poke_swsh_common.online(uart)
            poke_swsh_common.gotoRaid(uart)
            poke_swsh_common.setRaidPassword(uart)
            poke_swsh_common.waitForRaid(uart)
            poke_swsh_common.raid(uart)
            poke_swsh_common.closeGame(uart)
            times = times + 1
            print("[%s] 脚本运行中，已开启了%d次团战" % (datetime.now(),times))
    except KeyboardInterrupt:
        poke_swsh_common.send(uart,'RELEASE')
