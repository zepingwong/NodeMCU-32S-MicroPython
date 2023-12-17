# 导入Microdot
from lib.microdot import Microdot, send_file, Request
from lib.microdot_websocket import with_websocket

# 连接wifi
from common.connect_wifi import do_connect
# 导入引脚
from machine import Pin

# 不加报错
Request.socket_read_timeout = None

light = Pin(2, Pin.OUT)
# 开始连接wifi
do_connect()
# 实例化这个类
app = Microdot()


# 返回一个网页
@app.route('/')
def index(request):
    return send_file('public/websocket.html')


@app.route('/ws')
@with_websocket
def echo(request, ws):
    while True:
        data = ws.receive()
        if data == '1':
            light.value(1)
            ws.send('开灯了')
        elif data == '0':
            light.value(0)
            ws.send('关灯了')


# 端口号为5000
app.run(host='0.0.0.0', port=5000, debug=False, ssl=None)
