import poke_swsh_common
uart = poke_swsh_common.getUart()
poke_swsh_common.delay(uart)
poke_swsh_common.enterTimeSetting(uart)
poke_swsh_common.firstAddDate(uart,1)