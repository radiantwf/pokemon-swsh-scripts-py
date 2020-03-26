import poke_swsh_common, datetime
uart = poke_swsh_common.uart()
try:
    times = 0
    day = 1
    limit = 1000
    poke_swsh_common.delay(uart)
    poke_swsh_common.gotoDatetimeSettingFromHome(uart)
    poke_swsh_common.initialAddOneDay(uart)
    times += 1
    day += 1
    if day > 30:
        day = 1
    if times >= limit:
        print("[%s] 任务完成，已经跳过%d帧" % (datetime.now(),times))
    if times % 100 == 0:
        print("[%s] 任务进行中，已经跳过%d帧" % (datetime.now(),times))
    for num in range(0,800):
        poke_swsh_common.followingAddOneDay(uart)
        times += 1
        day += 1
        if day > 30:
            day = 1
        if times >= limit:
            print("[%s] 任务完成，已经跳过%d帧" % (datetime.now(),times))
            break
        if times % 100 == 0:
            print("[%s] 任务进行中，已经跳过%d帧" % (datetime.now(),times))
except KeyboardInterrupt:
    poke_swsh_common.send(uart,'RELEASE')














import machine
machine.reset()


        # /// <summary>
        # /// 切换到互联网模式
        # /// </summary>
        # internal void SwitchToOnlineMode() {
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonY, 100);
        #     Thread.Sleep(1000);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonStart, 100);
        #     Thread.Sleep(30000);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonB, 100);
        #     Thread.Sleep(1000);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonB, 100);
        #     Thread.Sleep(1000);
        # }

        # /// <summary>
        # /// 切换到本地模式
        # /// </summary>
        # internal void SwitchToLocalMode() {
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonY, 100);
        #     Thread.Sleep(1000);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonStart, 100);
        #     Thread.Sleep(500);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 100);
        #     Thread.Sleep(5000);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonB, 100);
        #     Thread.Sleep(500);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonB, 100);
        #     Thread.Sleep(1500);
        # }