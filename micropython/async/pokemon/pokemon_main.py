
import uasyncio
from pokemon.swsh import regirock


async def run():
    try:
        await regirock.run(restart=True)
    except Exception as e:
        print(e)
        raise e
