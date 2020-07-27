import poke_swsh_common, datetime
from time import sleep

def run(isSecondary=False,delay=3):
    times = 0
    uart = poke_swsh_common.uart()
    try:
        poke_swsh_common.delay(uart,delay)
        while True:
            if isSecondary and (times % 150 == 149):
                poke_swsh_common.switchNetMode(uart)
                
            for times in range(0, 3): 
                # 人物移动
                poke_swsh_common.send(uart,'LX MIN', 1.7)
                sleep(0.5)
                poke_swsh_common.send(uart,'LX MAX', 1.8)
                # 调整角度
                poke_swsh_common.send(uart,'LY MIN', 0.5)
                sleep(0.1)

            # 取蛋
            poke_swsh_common.send(uart,'Button A', 0.1)
            sleep(0.8)
            poke_swsh_common.send(uart,'Button A', 0.1)
            sleep(0.8)
            delay = 0
            while delay < 8:
                poke_swsh_common.send(uart,'Button B', 0.1)
                sleep(0.9)
                delay = delay + 1
            sleep(1)
            times = times + 1
            if times % 10 == 0:
                print("[%s] 脚本运行中，已执行了%d次取蛋动作" % (datetime.now(),times))
    except KeyboardInterrupt:
        poke_swsh_common.send(uart,'RELEASE')
    print("[%s] 脚本运行结束，共执行了%d次取蛋动作" % (datetime.now(),times))
