import umqtt.robust


class MQTTClient:
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        pass

    _client = None

    def init(self,
             client_id,
             server,
             port=0,
             user=None,
             password=None,
             keepalive=0,
             ssl=False,
             ssl_params={},):
        self._client = umqtt.robust.MQTTClient(
            client_id,
            server,
            port,
            user,
            password,
            keepalive,
            ssl,
            ssl_params)

    def log(self, in_reconnect, e):
        return self._client.log(in_reconnect, e)

    def connect(self, clean_session=True):
        return self._client.connect(clean_session)

    def reconnect(self):
        return self._client.reconnect()

    def publish(self, topic, msg, retain=False, qos=0):
        return self._client.publish(topic, msg, retain, qos)

    def wait_msg(self):
        return self._client.wait_msg()

    def check_msg(self):
        try:
            msg = self._client.check_msg()
        except Exception as e:
            print(e)
            self._client.reconnect()

    def set_callback(self, f):
        return self._client.set_callback(f)

    def set_last_will(self, topic, msg, retain=False, qos=0):
        return self._client.set_last_will(topic, msg, retain, qos)

    def disconnect(self):
        return self._client.disconnect()

    def ping(self):
        return self._client.ping()

    def subscribe(self, topic, qos=0):
        return self._client.subscribe(topic, qos)
