import poke_swsh_common, datetime, math
from time import sleep

def run(initCol=0, maxBox=0, maxCol=5, eggCycle=20, flamebody=True, isSecondary=True, delay=3):
    if flamebody:
        steps = math.ceil(257.0 * eggCycle / 2.0)
        cycles = math.ceil(eggCycle / 2.0)
    else:
        steps = 257 * eggCycle
        cycles = eggCycle
    col = initCol
    box = 0
    print("[%s] 孵化周期：%d，孵化步数：%d" % (datetime.now(),eggCycle,steps))
    print("[%s] 起始列：%d，终止箱子数：%d，终止列：%d" % (datetime.now(),initCol,maxBox,maxCol))
    uart = poke_swsh_common.uart()
    try:
        poke_swsh_common.delay(uart,delay)
        while True:
            # 进入盒子
            poke_swsh_common.send(uart,'Button X', 0.1)
            sleep(1)
            poke_swsh_common.send(uart,'Button A', 0.1)
            sleep(1.4)
            poke_swsh_common.send(uart,'Button R', 0.1)
            sleep(1.6)
            
            # 选择范围移动
            poke_swsh_common.send(uart,'Button Y', 0.1)
            sleep(0.2)
            poke_swsh_common.send(uart,'Button Y', 0.1)
            sleep(0.2)
            
            # 移动光标到同行第二只宝可梦，然后选择2-6宝可梦
            poke_swsh_common.send(uart,'LX MIN', 0.1)
            sleep(0.15)
            poke_swsh_common.send(uart,'LY MAX', 0.1)
            sleep(0.15)
            poke_swsh_common.send(uart,'Button A', 0.1)
            sleep(0.3)
            poke_swsh_common.send(uart,'LY MIN', 0.1)
            sleep(0.15)
            poke_swsh_common.send(uart,'LY MIN', 0.1)
            sleep(0.15)
            # poke_swsh_common.send(uart,'LY MAX', 0.1)
            # sleep(0.15)
            # poke_swsh_common.send(uart,'LY MAX', 0.1)
            # sleep(0.15)
            # poke_swsh_common.send(uart,'LY MAX', 0.1)
            sleep(0.15)
            poke_swsh_common.send(uart,'Button A', 0.1)
            sleep(0.5)

            # 移动光标到0行col列
            poke_swsh_common.send(uart,'LY MIN', 0.1)
            sleep(0.15)
            for num in range(0, col + 1): 
                poke_swsh_common.send(uart,'LX MAX', 0.1)
                sleep(0.15)
            # 放下移动宝可梦
            poke_swsh_common.send(uart,'Button A', 0.1)
            sleep(0.5)
            
            # 光标移动到要孵的蛋的位置
            col = col + 1
            if col > 5 :
                col = 0
                poke_swsh_common.send(uart,'Button R', 0.1)
                sleep(0.5)
                # poke_swsh_common.send(uart,'LX MIN', 0.1)
                # sleep(0.15)
                # poke_swsh_common.send(uart,'LX MIN', 0.1)
                # sleep(0.15)
                # poke_swsh_common.send(uart,'LX MIN', 0.1)
                # sleep(0.15)
                # poke_swsh_common.send(uart,'LX MIN', 0.1)
                # sleep(0.15)
                # poke_swsh_common.send(uart,'LX MIN', 0.1)
                # sleep(0.15)
                poke_swsh_common.send(uart,'LX MAX', 0.1)
                sleep(0.15)
                poke_swsh_common.send(uart,'LX MAX', 0.1)
                sleep(0.15)
                box = box + 1
            else:
                poke_swsh_common.send(uart,'LX MAX', 0.1)
                sleep(0.15)

            # 选中要孵的蛋
            poke_swsh_common.send(uart,'Button A', 0.1)
            sleep(0.1)
            # poke_swsh_common.send(uart,'LY MAX', 0.1)
            # sleep(0.15)
            # poke_swsh_common.send(uart,'LY MAX', 0.1)
            # sleep(0.15)
            # poke_swsh_common.send(uart,'LY MAX', 0.1)
            # sleep(0.15)
            poke_swsh_common.send(uart,'LY MIN', 0.1)
            sleep(0.15)
            poke_swsh_common.send(uart,'Button A', 0.1)
            sleep(0.5)

            # 移动光标到同行第二只宝可梦，然后放下宝可梦
            for num in range(0, col + 1): 
                poke_swsh_common.send(uart,'LX MIN', 0.1)
                sleep(0.15)
            poke_swsh_common.send(uart,'LY MAX', 0.1)
            sleep(0.15)
            poke_swsh_common.send(uart,'Button A', 0.1)
            sleep(0.3)

            # 退出盒子
            poke_swsh_common.send(uart,'Button B', 0.1)
            sleep(1.6)
            poke_swsh_common.send(uart,'Button B', 0.1)
            sleep(1.4)
            poke_swsh_common.send(uart,'Button B', 0.1)
            sleep(1.2)

            # 人物移动
            for num in range(0, cycles): 
                poke_swsh_common.send(uart,'LX MAX', 3.8)
                sleep(0.2)
                poke_swsh_common.send(uart,'LX MIN', 3.8)
                sleep(0.2)
                
            # 孵化
            for num in range(0, 5): 
                if num % 2 == 0:
                    poke_swsh_common.send(uart,'LX MAX', 0.3)
                else:
                    poke_swsh_common.send(uart,'LX MIN', 0.3)
                sleep(0.5)
                for delay in range(0, 18): 
                    poke_swsh_common.send(uart,'Button B', 0.1)
                    sleep(1)

            # 调整人物位置
            poke_swsh_common.send(uart,'LX MIN', 3.8)
            sleep(0.5)
            poke_swsh_common.send(uart,'LY MIN', 0.3)
            sleep(0.2)

            if col == 0:
                print("[%s] 脚本运行中，孵蛋到第%d箱，共%d箱，%d列" % (datetime.now(),box,maxBox,maxCol))

                if box % 3 == 2:
                    # 保存进度
                    poke_swsh_common.save(uart)
                    if isSecondary:
                        poke_swsh_common.switchNetMode(uart)

            # 判断是否完成
            if box > maxBox or (box == maxBox and col >= maxCol):
                break
    except KeyboardInterrupt:
        poke_swsh_common.send(uart,'RELEASE')
    print("[%s] 脚本运行结束，成功孵蛋到第%d箱，%d列" % (datetime.now(),box,col))
