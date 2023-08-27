# Micropython_IOT_Sensors_lib
Some sensors' micropython lib, including BH1750, JW01 and a Capacitive Soil Moisture Sensor.Demo is included.Code are tested on a esp32 board.Written by myself.<br>
一些自己写的传感器的micropython库,包含BH1750,JW01和一个电容式土壤湿度传感器,并含有示例程序.本文中的图片仅作示例,无购买引导倾向,若有侵权请联系我删除!谢谢🙏代码在esp32板上测试可行.

## BH1750 light sensor
<img src="https://github.com/sszzz830/Micropython_IOT_Sensors_lib/assets/32834442/1e328ac6-46da-453d-b036-9133445a9aca" width="250"><br>
First, copy BH1750.py to the root folder of your device. 首先把BH1750.py拷贝到单片机的根目录下.<br>
Then connect the BH1750 to the gpios. 然后连接BH1750到指定引脚.
```micropython
import BH1750
from machine import SoftI2C

s = BH1750.BH1750(SoftI2C(Pin(19),Pin(23))) #Initialize BH1750 sensor with SoftI2C(Pin(19),Pin(23)) 初始化传感器,在SoftI2C(Pin(19),Pin(23))上
print(s.luminance(0x20)) #Measure in ONCE_HIRES_1 mode once and print result on terminal 在高精度模式1下测量一次并且打印到终端 
```
This demo initializes a BH1750 instance, and measured once and printed the result to terminal. 这个示例初始化了一个BH1750实例,并且使用其读取了一次然后打印.<br>
Other methods and mode are listed here 其他的全部方法和模式如下:
```micropython
#modes 所有可选的模式
PWR_OFF = 0x00
PWR_ON = 0x01
RESET = 0x07
CONT_LOWRES = 0x13
CONT_HIRES_1 = 0x10
CONT_HIRES_2 = 0x11
ONCE_HIRES_1 = 0x20
ONCE_HIRES_2 = 0x21
ONCE_LOWRES = 0x23

#methods 方法
#assuming s an instance of BH1750 class 假设s是BH1750类的一个实例
s.on() #Turn on the sensor 打开传感器
s.off() #Turn off the sensor 关闭传感器
s.reset() #Reset the sensor 重置传感器
s.set_mode(mode) #Set mode 设置模式
s.luminance(mode) #Read with mode and return result 以指定模式读取并且返回结果
```
## JW01 CO2 sensor
<img src="https://github.com/sszzz830/Micropython_IOT_Sensors_lib/assets/32834442/2e4849d7-1ae1-47b4-8d59-44f8badf9e3e" width="250"><br>
First, copy JW01.by to the root folder of your device. 首先把JW01.py拷贝到单片机的根目录下.<br>
Then connect the JW01 to the gpios. 然后连接JW01到指定引脚.<br>
JW01 works on 5v electric level while most devices work on 3.3v, so make sure you have done the conversion. JW01工作在5v电平而大部分单片机是3.3v电平,所以请确保做好了电平转换.
```micropython
from machine import UART
from JW01 import JW01

uart1 = UART(1,baudrate=JW01.BAUDRATE,bits=JW01.BITS,parity=JW01.PARITY,stop=JW01.STOP,tx=17,rx=16)
jw01_sensor = JW01(uart1) #Initialize JW01 sensor on gpio 16 and 17, using UART resource 1 在gpio16和17上初始化JW01,使用UART1资源

print(jw01_sensor.measure()) #Read and print 读取并显示
```

## Capacitive Soil Moisture Sensor
<img src="https://github.com/sszzz830/Micropython_IOT_Sensors_lib/assets/32834442/e7b3437a-df92-4fab-9421-146120b41056" width="250"><br>
Demo is work in progress.

## MQTT subscribe with tls certificate demo
Work in progress

## License 授权
This repository is licensed under the MIT License. 本仓库使用MIT License授权.
