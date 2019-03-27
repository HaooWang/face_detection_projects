#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
PC使用PySerial发送数据
负责与ESP32主控的舵机云台进行通信
------------------------------------
## 注意
运行此程序的时候，需要修改设备的权限，
sudo chmod 777 /dev/ttyUSB?  ，其中 ? = 0,1,2,...
或者使用管理员权限运行脚本
sudo python xxxxx.py

'''
import struct
import time
import string

import serial

# 串口号 默认为 com6 Arduino
ser_dev = 'com6'
# 创建一个串口实例
ser = serial.Serial(ser_dev, 9600, timeout=1, bytesize=8)


def pack_bin_data(bottom_degree, top_degree):
	'''
	h: unsigned short bit=2
	b: unsigned char (byte): bit =1
	'''
	
	bin_data = "#1P"+bottom_degree+"#2P"+top_degree+"T100\r\n"
	
	return bin_data


def set_cloud_platform_degree(bottom_degree, top_degree):
	global ser
	# 生成二进制序列
	byte_str = pack_bin_data(bottom_degree, top_degree)
	# 通过串口发送
	ser.write(byte_str)
	print("Send: " + byte_str + "\n")


def main():
	i = 100
	while (i > 1):
		# 测试角度
		set_cloud_platform_degree(100, 100)
		# 每隔10ms发送一次数据
		time.sleep(10)


if __name__ == "__main__":
	main()
