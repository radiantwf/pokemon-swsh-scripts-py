import time
import ubinascii
import machine
from umqtt import MQTTClient

# Publish test messages e.g. with:
# mosquitto_pub -t foo_topic -m hello

SERVER = "192.168.1.35"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
PORT=1833
USER="wangfeng"
PASSWORD="wf1984"
TOPIC = b"pokemon"

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))

def main(server="localhost"):
    c = MQTTClient(client_id=CLIENT_ID, server=SERVER, port=1883, user=USER, password=PASSWORD)
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














import ntptime
ntptime.settime()

import days_forward
days_forward.run(frames=32446,date=1,maxDate=30,)

import three_days_forward
three_days_forward.run(date=1,maxDate=30,isSecondary=True)

import three_days_forward_raid
three_days_forward_raid.run(date=1,maxDate=30,isSecondary=True)

import get_eggs
get_eggs.run(isSecondary=False)   #需要身上放满宝可梦

import hatching_eggs
hatching_eggs.run(initCol=0,maxBox=8,maxCol=1,eggCycle=20,flamebody=True,isSecondary=False,delay=3)

import get_watts
get_watts.run(date=1,maxDate=31)
import get_watts_for_bug
get_watts_for_bug.run(date=1,maxDate=31)

import machine
machine.reset()
