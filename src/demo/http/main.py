# 导入Microdot
from lib.microdot import Microdot, send_file
# 连接wifi
from common.connect_wifi import do_connect
# 导入引脚
from machine import Pin
# esp32 引脚2是一颗自带的 led的灯
light = Pin(2,Pin.OUT)
# 开始连接wifi
do_connect()
# 实例化这个类
app = Microdot()

# 返回一个网页
@app.route('/')
def index(request):
    return send_file('public/http.html')

# 设置一个get请求 如果
@app.get('/on')
def index(request):
    # 如果收到get请求on就开灯
    light.value(1)
    return "开灯了"

@app.get('/off')
def index(request):
    # 如果收到get请求off就关灯
    light.value(0)
    return "关灯了"
# 端口号为5000
app.run(host='0.0.0.0', port=5000, debug=False, ssl=None)
