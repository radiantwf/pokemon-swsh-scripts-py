import poke_swsh_common, datetime
from time import sleep

def threeDaysForwardAndRaid(isSecondary=True,second=3.0):
    date = 1
    uart = poke_swsh_common.uart()
    try:
        poke_swsh_common.delay(uart,second)

        while(True):
            poke_swsh_common.openGame(uart,isSecondary)

            for times in range(0, 4): 
                if times == 0:
                    poke_swsh_common.gotoRaid(uart,isOnline=False,hasWatts=False)
                elif times == 3:
                    poke_swsh_common.onlineModel(uart)
                    poke_swsh_common.gotoRaid(uart,isOnline=True,hasWatts=True)
                else:
                    poke_swsh_common.gotoRaid(uart,isOnline=False,hasWatts=True)

                if times != 3:
                    # 点击 大家一起挑战
                    poke_swsh_common.send(uart,'Button A', 0.1)
                    sleep(3)

                    poke_swsh_common.gotoHome(uart)
                    poke_swsh_common.gotoDatetimeSettingFromHome(uart)
                    poke_swsh_common.initialAddOneDay(uart)

                    date = date + 1
                    if date > 30 :
                        date = 1
                        times = times - 1
                    
                    poke_swsh_common.returnGame(uart)

                    # 取消团战
                    poke_swsh_common.send(uart,'Button B', 0.1)
                    sleep(1)
                    poke_swsh_common.send(uart,'Button A', 0.1)
                    sleep(5)
                else:
                    poke_swsh_common.setRaidPassword(uart)
                    poke_swsh_common.waitForRaid(uart)
                    poke_swsh_common.raid(uart)
                    
            poke_swsh_common.closeGame(uart)
    except KeyboardInterrupt:
        poke_swsh_common.send(uart,'RELEASE')