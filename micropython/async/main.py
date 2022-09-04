from time import sleep
from mqtt_as import MQTTClient, config
from customize.datetime import ntpSync
from pokemon import pokemon_main
import uasyncio

SERVER1 = "192.168.50.1"
SERVER2 = "192.168.1.100"
TOPIC1 = "Controller1"
TOPIC2 = "Controller2"
CLIENT_ID1 = "ESP32_No.1"
CLIENT_ID2 = "ESP32_No.2"
# CLIENT_ID = ubinascii.hexlify(machine.unique_id())
KEEPALIVE = 30


async def connect_coro(client):
    await client.subscribe(TOPIC1, 0)


def callback(topic, msg, retained):
    print((topic, msg, retained))


async def mqtt_conn():
    client = MQTTClient(config)
    try:
        await client.connect()
        while True:
            await uasyncio.sleep(5)
    finally:
        client.close()

config['client_id'] = CLIENT_ID1
config['subs_cb'] = callback
config['connect_coro'] = connect_coro
config['server'] = SERVER1
config['ssid'] = 'WangFeng'
config['wifi_pw'] = 'radiantwf'


def main():
    print('准备中，15s后运行')
    sleep(15)
    print('开始运行')
    try:
        print(ntpSync())
    except:
        print('时间同步发生错误')

    loop = uasyncio.get_event_loop()
    task1 = loop.create_task(mqtt_conn())
    task2 = loop.create_task(pokemon_main.run())
    loop.run_until_complete(task1)
    loop.run_until_complete(task2)
    loop.close()


if __name__ == '__main__':
    main()
