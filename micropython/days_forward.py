import poke_swsh_common, datetime

def daysForwart(frames=1000,second=3.0):
    times = 0
    day = 1
    uart = poke_swsh_common.uart()
    try:
        poke_swsh_common.delay(uart,second)

        while(True):
            if times >= frames:
                break

            if times > 0:
                print("[%s] 任务进行中，已经跳过%d帧" % (datetime.now(),times))
                poke_swsh_common.returnGame(uart)
                poke_swsh_common.save(uart)
                poke_swsh_common.gotoHome(uart)
                poke_swsh_common.gotoDatetimeSettingFromHome(uart)
            
            poke_swsh_common.initialAddOneDay(uart)
            day += 1
            if day > 30:
                day = 1
            else:
                times += 1

            for num in range(0,999):
                if times >= frames:
                    break
                poke_swsh_common.followingAddOneDay(uart)
                day += 1
                if day > 30:
                    day = 1
                else:
                    times += 1

        print("[%s] 任务完成，已经跳过%d帧" % (datetime.now(),times))
    except KeyboardInterrupt:
        poke_swsh_common.send(uart,'RELEASE')
