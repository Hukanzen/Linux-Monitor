#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil
import datetime
import SystemAnalyzer
import ReadMountConfig

def main():
	now = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
	print(now)
	
	RMC=ReadMountConfig.ReadMountConfig('/srv')
	print(RMC.GetIpAddr_str())
	print(RMC.GetIpAddr_uint())
	
	psutil.PROCFS_PATH = '/rootfs/proc'
	print(psutil.cpu_percent(interval=1))
	print(psutil.virtual_memory())
	print(psutil.swap_memory())
	print(psutil.disk_usage('/'))	
	
	SysAnaly=SystemAnalyzer.SystemAnalyzer('/rootfs')
	SysAnaly.ReadLoadAvg()
	print(SysAnaly.GetterLoadAvg(1))
	print(SysAnaly.GetterLoadAvg(5))
	print(SysAnaly.GetterLoadAvg(15))
	print(SysAnaly.GetterHostname())

if __name__ == '__main__':
	main()