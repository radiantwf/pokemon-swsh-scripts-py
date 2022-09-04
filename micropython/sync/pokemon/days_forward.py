import pokemon.poke_swsh_common
import customize.datetime


def run(frames=1000, date=1, maxDate=31, delay=3.0):
    times = 0
    uart = pokemon.poke_swsh_common.uart()
    try:
        pokemon.poke_swsh_common.delay(uart, delay)

        while (True):
            if times >= frames:
                break

            if times > 0:
                print("[%s] 任务进行中，已经跳过%d帧" % (customize.datetime.now(), times))
                pokemon.poke_swsh_common.returnGame(uart)
                pokemon.poke_swsh_common.save(uart)
                pokemon.poke_swsh_common.gotoHome(uart)
            pokemon.poke_swsh_common.gotocustomize.datetimeSettingFromHome(
                uart)
            pokemon.poke_swsh_common.initialAddOneDay(uart)
            date += 1
            if date > maxDate:
                date = 1
            else:
                times += 1

            for num in range(0, 999):
                if times >= frames:
                    break
                pokemon.poke_swsh_common.followingAddOneDay(uart)
                date += 1
                if date > maxDate:
                    date = 1
                else:
                    times += 1

        print("[%s] 任务完成，已经跳过%d帧" % (customize.datetime.now(), times))
    except KeyboardInterrupt:
        pokemon.poke_swsh_common.send(uart, 'RELEASE')
