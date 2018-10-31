#!/usr/bin/env python3

import SystemAnalyzer

def main():
	SysAnaly=SystemAnalyzer.SystemAnalyzer('/srv/')
	print(SysAnaly.GetIpAddr_str())
	
	
if __name__ == '__main__':
	main()


