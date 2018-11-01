#!/usr/bin/env python3

import configparser
import re

class SystemAnalyzer:
	__config_FILE_NAME='/config.conf' # Configファイル
	__cpuinfo={} # /proc/cpuinfo の情報
	__meminfo={} # /proc/cpuinfo の情報

	def __init__(self,location):
		self.__location_DIR=location # /procのをマウントしている場所
		self.__proc_DIR=location+'/proc' # /procファイル
		
		self.__config = configparser.ConfigParser() # Configをパースするインスタンス
		self.__config.read(self.__location_DIR+self.__config_FILE_NAME) # 読み込む
		
	def GetIpAddr_str(self):
		return self.__config.get('HostInfo','ipaddr_str') 
	
	#####
	# /proc/+Itype+infoを読み取る．ただし，1つ分のコアのみ
	#####
	def ReadInfo(self,Itype):
		with open(self.__proc_DIR+'/'+Itype+'info','r') as f:
			for oneline in f:
				oneline_list=oneline.split(':')
				
				try:
					key=oneline_list[0]
					val=oneline_list[1]
				except: # スプリットした結果，値がなかった場合
					break # for文を終了する
				
				key=re.sub('\t$','',key)
				val=re.sub('^ ','',val)
				val=re.sub('\n$','',val)
				
				if Itype == 'cpu':
					self.__cpuinfo[key]=val
				elif Itype == 'mem':
					self.__meminfo[key]=val
		
		
	#####
	# __cpuinfo,__meminfoのゲッター
	#####
	def GetterInfo(self,Itype):
		if Itype == 'cpu':
			print(self.__cpuinfo['processor'])
			print(self.__cpuinfo)
		elif Itype == 'mem':
			print(self.__meminfo['MemTotal'])
			print(self.__meminfo)
