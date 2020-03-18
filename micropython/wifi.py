import network
def connect(ssd,pwd):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssd, pwd) 
    if sta_if.isconnected(): 
        import ntptime
        ntptime.host = '0.cn.pool.ntp.org'
        ntptime.settime()
        print("network config:", sta_if.ifconfig())
def disconnect():
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.isconnected():
        sta_if.disconnect()
def ap(ssd,pwd='',active=1,hidden=False):
    ap=network.WLAN(network.AP_IF)
    ap.active(active)
    if pwd=='':
        ap.config(essid=ssd, authmode=network.AUTH_OPEN)
        return
    ap.config(essid=ssd, authmode=network.AUTH_WPA_WPA2_PSK, password=pwd, hidden=hidden)
