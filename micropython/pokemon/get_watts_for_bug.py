import poke_swsh_common, datetime
from time import sleep

def run(date=1,maxDate=31,delay=3):
    uart = poke_swsh_common.uart()
    try:
        poke_swsh_common.delay(uart,delay)
        times = 0
        invalidDate = False
        while True:
            poke_swsh_common.gotoHome(uart)
            poke_swsh_common.gotoDatetimeSettingFromHome(uart)
            poke_swsh_common.initialAddOneDay(uart)

            date += 1
            if date > maxDate:
                date = 1
                poke_swsh_common.followingAddOneDay(uart)
                date += 1
                invalidDate = False
            else:
                times += 1
                invalidDate = False
                    
            poke_swsh_common.returnGame(uart)

            poke_swsh_common.gotoRaid(uart,isOnline=False,hasWatts=True)

            # 取消团战
            poke_swsh_common.send(uart,'Button B', 0.1)
            sleep(2)
    except KeyboardInterrupt:
        poke_swsh_common.send(uart,'RELEASE')
