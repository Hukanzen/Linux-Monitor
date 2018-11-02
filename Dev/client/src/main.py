#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime 
import SystemAnalyzer


def main():
	SysAnaly=SystemAnalyzer.SystemAnalyzer('/srv')
	print(SysAnaly.GetIpAddr_str())
	print(SysAnaly.GetIpAddr_uint())
	SysAnaly.ReadInfo('cpu')
	SysAnaly.ReadInfo('mem')
	print(SysAnaly.GetterInfo('cpu','model name'))
	print(SysAnaly.GetterInfo('mem','MemTotal'))
	SysAnaly.ReadLoadAvg()
	print(SysAnaly.GetterLoadAvg(1))
	print(SysAnaly.GetterLoadAvg(5))
	print(SysAnaly.GetterLoadAvg(15))
	now = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
	print(now)
	print(SysAnaly.GetterHostname())
	
if __name__ == '__main__':
	main()


