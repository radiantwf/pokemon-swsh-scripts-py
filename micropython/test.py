import regirock
import poke_swsh_common
import get_watts_for_bug
import get_watts
import hatching_eggs
import get_eggs
import three_days_forward_raid
import three_days_forward
import days_forward
import ntptime
import time
import ubinascii
import machine
from umqtt import MQTTClient

# Publish test messages e.g. with:
# mosquitto_pub -t foo_topic -m hello

SERVER = "192.168.1.35"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
PORT = 1833
USER = "wangfeng"
TOPIC = b"pokemon"

# Received messages from subscriptions will be delivered to this callback


def sub_cb(topic, msg):
    print((topic, msg))


def main(server="localhost"):
    c = MQTTClient(client_id=CLIENT_ID, server=SERVER,
                   port=1883, user=USER, password=PASSWORD)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()


if __name__ == "__main__":
    main()

ntptime.settime()

days_forward.run(frames=32446, date=1, maxDate=30,)

three_days_forward.run(date=1, maxDate=30, isSecondary=True)

three_days_forward_raid.run(date=1, maxDate=30, isSecondary=True)

get_eggs.run(isSecondary=False)  # 需要身上放满宝可梦

hatching_eggs.run(initCol=0, maxBox=8, maxCol=1, eggCycle=20,
                  flamebody=True, isSecondary=False, delay=3)

get_watts.run(date=1, maxDate=31)
get_watts_for_bug.run(date=1, maxDate=31)

machine.reset()


uart = poke_swsh_common.uart()
poke_swsh_common.send(uart, 'Button A', 1)
poke_swsh_common.send(uart, 'LX MIN', 1)


poke_swsh_common.send(uart, 'LY MAX', 0.5)
poke_swsh_common.send(uart, 'LX MAX', 0.5)
poke_swsh_common.send(uart, 'LY MIN', 0.6)
poke_swsh_common.send(uart, 'LX MIN', 0.5)

uart = poke_swsh_common.uart()
poke_swsh_common.send(uart, 'Button HOME', 0.1)
time.sleep(1)
poke_swsh_common.send(uart, 'Button A', 0.1)
time.sleep(0.5)
poke_swsh_common.send(uart, 'Button A', 0.1)
time.sleep(1)
poke_swsh_common.send(uart, 'Button A', 0.1)
poke_swsh_common.enterBattleAndCheckShiny(uart, 7)

poke_swsh_common.send(uart, 'Button A', 0.1)

poke_swsh_common.send(uart, 'LX MIN', 1.5)

regirock.run()


poke_swsh_common.send(uart, 'LY MAX', 1.76)
time.sleep(0.5)
poke_swsh_common.send(uart, 'LX MAX', 2.5)
time.sleep(0.5)
poke_swsh_common.send(uart, 'LY MIN', 0.45)
time.sleep(0.5)
poke_swsh_common.send(uart, 'LX MIN', 2.5)
time.sleep(0.5)
poke_swsh_common.send(uart, 'LY MIN', 0.45)
time.sleep(0.5)
poke_swsh_common.send(uart, 'LX MAX', 2.5)
time.sleep(3)
poke_swsh_common.send(uart, 'Button A', 0.1)
time.sleep(1)
poke_swsh_common.send(uart, 'LY MIN', 1)
time.sleep(0.2)
