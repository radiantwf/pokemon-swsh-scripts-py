import poke_swsh_common, datetime
from time import sleep

def threeDaysForward(date=1, maxDate=30, isSecondary=True, second=3.0):
    uart = poke_swsh_common.uart()
    try:
        poke_swsh_common.delay(uart,second)

        while(True):
            poke_swsh_common.openGame(uart,isSecondary)

            times = 0
            invalidDate = False
            while(times < 4): 
                if (times == 0) or invalidDate:
                    poke_swsh_common.gotoRaid(uart,isOnline=False,hasWatts=False)
                else:
                    poke_swsh_common.gotoRaid(uart,isOnline=False,hasWatts=True)

                if times != 3:
                    # 点击 大家一起挑战
                    poke_swsh_common.send(uart,'Button A', 0.1)
                    sleep(3)

                    poke_swsh_common.gotoHome(uart)
                    poke_swsh_common.gotoDatetimeSettingFromHome(uart)
                    poke_swsh_common.initialAddOneDay(uart)

                    date += 1
                    if date > maxDate:
                        date = 1
                        invalidDate = True
                    else:
                        times += 1
                        invalidDate = False
                    
                    poke_swsh_common.returnGame(uart)

                    # 取消团战
                    poke_swsh_common.send(uart,'Button B', 0.1)
                    sleep(1)
                    poke_swsh_common.send(uart,'Button A', 0.1)
                    sleep(5)
                else:
                    times += 1
                    sleep(15)
            poke_swsh_common.closeGame(uart)
    except KeyboardInterrupt:
        poke_swsh_common.send(uart,'RELEASE')