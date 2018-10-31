#!/usr/bin/env python3

import configparser

class SystemAnalyzer:
	__config_FILE_NAME='config.conf' # Configファイル
	
	def __init__(self,location):
		self.__location_DIR=location # /procのをマウントしている場所
		
		self.__config = configparser.ConfigParser() # Configをパースするインスタンス
		self.__config.read(location+self.__config_FILE_NAME) # 読み込む
	
	def GetIpAddr_str(self):
		return self.__config.get('HostInfo','ipaddr_str') 
		