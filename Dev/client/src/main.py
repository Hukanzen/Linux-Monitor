#!/usr/bin/env python3

import SystemAnalyzer

def main():
	SysAnaly=SystemAnalyzer.SystemAnalyzer('/srv')
	print(SysAnaly.GetIpAddr_str())
	SysAnaly.ReadInfo('cpu')
	SysAnaly.ReadInfo('mem')
	print(SysAnaly.GetterInfo('cpu'))
	print(SysAnaly.GetterInfo('mem'))
	
	
if __name__ == '__main__':
	main()


