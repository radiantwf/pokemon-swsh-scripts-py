import poke_swsh_common, datetime
uart = poke_swsh_common.uart()
try:
    poke_swsh_common.delay(uart)
    poke_swsh_common.gotoDatetimeSettingFromHome(uart)
    times = 0
    day = 1
    limit = 1000
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
        # /// 保存进度
        # /// </summary>
        # internal void Save() {
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonX, 100);
        #     Thread.Sleep(1500);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonR, 100);
        #     Thread.Sleep(1500);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 100);
        #     Thread.Sleep(4000);
        # }

        # /// <summary>
        # /// 从Home界面进入时间设置界面
        # /// </summary>
        # internal void GotoDatetimeSettingFromHome() {
        #     // 进入设置界面
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LYMax, 100);
        #     Thread.Sleep(100);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LXMax, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LXMax, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LXMax, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LXMax, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 100);
        #     Thread.Sleep(2000);

        #     // 进入时间设置界面
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LYMax, 3000);
        #     Thread.Sleep(100);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 100);
        #     Thread.Sleep(1000);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LYMax, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LYMax, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LYMax, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LYMax, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 100);
        #     Thread.Sleep(1000);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LYMax, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LYMax, 80);
        #     Thread.Sleep(80);
        # }

        # /// <summary>
        # /// 首次调整一天（光标从左向右）
        # /// </summary>
        # internal void InitialAddOneDay() {
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 100);
        #     Thread.Sleep(500);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LYMin, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 80);
        #     Thread.Sleep(300);
        # }

        # /// <summary>
        # /// 后续调整一天（光标从右向左）
        # /// </summary>
        # internal void FollowingAddOneDay() {
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 100);
        #     Thread.Sleep(500);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LXMin, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LXMin, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LXMin, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.LYMin, 80);
        #     Thread.Sleep(80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 80);
        #     Thread.Sleep(80);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 80);
        #     Thread.Sleep(300);
        # }

        # /// <summary>
        # /// 开启团战界面
        # /// </summary>
        # /// <param name="isOnline">是否是互联网模式</param>
        # /// <param name="hasWatts">是否有未领取瓦特</param>
        # internal void StartRaid(bool isOnline, bool hasWatts) {
        #     // 需要领取 瓦特
        #     if (hasWatts) {
        #         Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 100);
        #         Thread.Sleep(800);
        #         Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 100);
        #         Thread.Sleep(800);
        #     }

        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 100);
        #     if (!isOnline) {
        #         Thread.Sleep(2500);
        #     } else {
        #         Thread.Sleep(8000);
        #     }
        # }

        # /// <summary>
        # /// 关闭游戏
        # /// </summary>
        # internal void CloseGame() {
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonHome, 100);
        #     Thread.Sleep(1500);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonX, 100);
        #     Thread.Sleep(500);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 100);
        #     Thread.Sleep(5000);
        # }

        # /// <summary>
        # /// 开启游戏
        # /// </summary>
        # /// <param name="secondary">是否位副机</param>
        # internal void OpenGame(bool isSecondary) {
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 100);
        #     Thread.Sleep(1500);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 100);
        #     if (isSecondary) {
        #         Thread.Sleep(5000);
        #     }
        #     Thread.Sleep(15000);
        #     Joystick.Instance.SyncButtonPress(JoystickButtonEnumType.ButtonA, 100);
        #     Thread.Sleep(6000);
        # }

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