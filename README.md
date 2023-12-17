# 安可信 NodeMCU-32S MicroPython 开发入门

## 准备工作

- 硬件资料: [安可信 NodeMCU-32S 核心开发板](https://docs.ai-thinker.com/esp32/boards/nodemcu_32s)
- Python环境: 推荐使用虚拟环境
- 驱动安装: [芯片制造商网站](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=overview) ； 或者使用此项目 development/driver 下的Windows或Mac的驱动程序
- 固件: [MicroPython官网](https://micropython.org/download/ESP32_GENERIC/) ；或者使用此项目 develop/firmware 目录下的固件

## 工具

- esptool: 用于与ESP32微控制器中的ROM引导加载程序通信,允许访问闪存固件，读回固件，查询芯片参数等
- adafruit-ampy: 用于通过串口连接操作文件并在CircuitPython或MicroPython板上运行代码。使用ampy，您可以将文件从计算机发送到电路板的文件系统，将文件从电路板下载到计算机，甚至可以将Python脚本发送到电路板上执行
- Thonny: [Thonny官网](https://thonny.org/) ；如果官网下载太慢可以使用此项目 development/software 下的 thonny 安装程序

## 刷写固件

### 安装依赖

```shell
pip install -r requirements.txt
```

### 擦除原 ESP32

> 下面两步使用的COM3需要根据设备管理器中的端口号进行修改

```shell
esptool --chip esp32 --port COM3 erase_flash
```

### 烧录 MicroPython

```shell
esptool --chip esp32 --port COM3 --baud 115200 write_flash -z 0x1000 ./firmware/ESP32_GENERIC-20231005-v1.21.0.bin
```

## 参考

- [太极创客](http://www.taichi-maker.com/homepage/download/)
- [MicroPython ESP32/WROOM](https://micropython.org/download/ESP32_GENERIC/)
- [nodemcu-pyflasher](https://gitcode.com/mirrors/marcelstoer/nodemcu-pyflasher/tree/master?init=initRepo)