#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
import socket

class SystemAnalyzer:
	__loadave=[0.0,0.0,0.0]    # load average 1min,5min,15min
	
	def __init__(self,location):
		self.__location_DIR=location # /procのをマウントしている場所
		self.__proc_DIR=location+'/proc' # /proc
		self.__etc_DIR=location+'/etc'


	#####
	# /proc/loadavgを読みとる．
	#####
	def ReadLoadAvg(self):
		with open(self.__proc_DIR+'/loadavg','r') as f:
			oneline=f.read()
		oneline_list=oneline.split(' ')
		for i in range(3):
			self.__loadave[i]=float(oneline_list[i])

		
	#####
	# LoadAverageを読み取る
	#####
	def GetterLoadAvg(self,minute):
		if minute == 5:
			return self.__loadave[1]	
		elif minute == 15:
			return self.__loadave[2]
		return self.__loadave[0]	



	#####
	# ホスト名を取得
	#####
	def GetterHostname(self):
		with open(self.__etc_DIR+'/hostname','r')as f: # /procだと書き換わる?
			oneline=f.read()
			oneline=re.sub('\n$','',oneline)

		return oneline
		# return 1

