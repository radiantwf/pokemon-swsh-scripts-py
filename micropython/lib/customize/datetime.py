import time


def now():
    now = time.localtime()
    str = "%02d/%02d/%02d %02d:%02d:%02d" % (
        now[0], now[1], now[2], now[3], now[4], now[5])
    return str

def ntpSync():
    import ntptime
    ntptime.host = '0.cn.pool.ntp.org'
    ntptime.settime()
    return now()
