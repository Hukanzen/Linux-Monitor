#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ipaddress
import configparser

class ReadMountConfig:
	__config_FILE_NAME='/config.conf' # Configファイル
	
	def __init__(self, location):
		self.__location_DIR=location # /procのをマウントしている場所
		
		self.__config = configparser.ConfigParser() # Configをパースするインスタンス
		self.__config.read(self.__location_DIR+self.__config_FILE_NAME) # 読み込む
		
	def GetIpAddr_str(self):
		return self.__config.get('HostInfo','ipaddr_str') 
	
	def GetIpAddr_uint(self):
		return int(ipaddress.ip_address(self.GetIpAddr_str()))
		