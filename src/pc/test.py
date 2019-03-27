# -*- coding: utf-8 -*-
import serial

# 打开串口
serialPort = "COM5"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0.05)
print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))

# 收发数据
while 1:
	str = input("请输入要发送的数据（非中文）并同时接收数据: ")
	ser.write((str + '\r\n').encode())
	#print(ser.readline())  # 可以接收中文

ser.close()

