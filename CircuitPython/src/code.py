import macros

import asyncio
print("hello hori")


async def task1():
    await macros.run("pokemon.swsh.regirock.regirock", True)


def main():
    print('准备中，15s后运行')
    asyncio.sleep(15)

    print('开始运行')
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(task1())
    loop.run_until_complete(task1)
    loop.close()


if __name__ == '__main__':
    main()
