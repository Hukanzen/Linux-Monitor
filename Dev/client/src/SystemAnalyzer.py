#!/usr/bin/env python3

import configparser
import re

class SystemAnalyzer:
	__config_FILE_NAME='/config.conf' # Configファイル
	__cpuinfo={} # /proc/cpuinfo の情報
	__meminfo={} # /proc/cpuinfo の情報
	__loadave=[0.0,0.0,0.0]    # load average
	__process_num=0
	__process_sum=0

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
				val=re.sub('^ +','',val)
				val=re.sub('\n$','',val)
				
				if Itype == 'cpu':
					self.__cpuinfo[key]=val
				elif Itype == 'mem':
					self.__meminfo[key]=val
		
		
	#####
	# __cpuinfo,__meminfoのゲッター
	#####
	def GetterInfo(self,Itype,Item):
		if Itype == 'cpu':
			return self.__cpuinfo[Item]
		elif Itype == 'mem':
			return self.__meminfo[Item]
	

	#####
	# /proc/loadavgを読みとる．
	#####
	def ReadLoadAvg(self):
		with open(self.__proc_DIR+'/loadavg','r') as f:
			oneline=f.read()
		oneline_list=oneline.split(' ')
		for i in range(3):
			self.__loadave[i]=float(oneline_list[i])
		self.__process_num=oneline_list[3]
		self.__process_sum=oneline_list[4]
		
	#####
	# LoadAverageを読み取る
	#####
	def GetterLoadAvg(self,minute):
		if minute == 5:
			return self.__loadave[1]	
		elif minute == 15:
			return self.__loadave[2]
		return self.__loadave[0]	


	def GetterDisk:

	def GetterHostname:

