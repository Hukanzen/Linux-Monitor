/**
 * 
 * https://myenigma.hatenablog.com/entry/2015/04/27/185822
 * 
 * @file SystemAnalyzer.h
 *
 * @brief Linuxにおいてシステム情報を取得するためのクラスライブラリ
 *
 * @note 使い方のサンプルコード
 *
 * SystemAnalyzer analyzer;
 * while(1){
 *    //CPUの使用率を取得
 *    int nCPU=4;//CPUの数
 *    unsigned int cpuUsage=analyzer.GetCPUUsage(nCPU);
 *    cout<<"CPU Usage is "<<cpuUsage<<"%"<<endl;
 *
 *    //メモリの使用率を取得
 *    unsigned int memUsage=analyzer.GetMemoryUsage();
 *    cout<<"Memory Usage is "<<memUsage<<"%"<<endl;
 *
 *    //ディスクの使用率を取得
 *    unsigned int diskUsage=analyzer.GetDiskUsage();
 *    cout<<"Disk Usage is "<<diskUsage<<"%"<<endl;
 *
 *    sleep(1);
 *  }
 *
 * @author Atsushi Sakai
 */
#ifndef SYSTEM_ANALYZER_H
#define SYSTEM_ANALYZER_H

#include <iostream>
#include <stdio.h>
#include <sys/statvfs.h>
#include <sys/sysinfo.h>
#include <sys/times.h>


/**
 * @brief Linuxにおいてシステム情報を取得するためのクラス
 */
class SystemAnalyzer
{
	public:
	SystemAnalyzer();

	//~~~~~~functions~~~~~~~

	/**
	 * @brief CPUの使用率を返す関数
	 * @param nCPU CPUの数
	 * @return システム全体のCPUの使用率[%]
	 */
	unsigned int GetCPUUsage(int);

	/**
	 * @brief 使用されているメモリの割合を取得する関数
	 *
	 * @return 使用されているメモリの割合[%] 0-100
	 */
	unsigned int GetMemoryUsage(void);

	/**
	 * @brief 使用されているディスクの割合を取得する関数
	 *
	 * @return 使用されているディスクの割合[%] 0-100
	 */
	unsigned int GetDiskUsage(void);

	private:
	//	GetCPUUsage用
	int     preTick_; // 前の/proc/statの値を保持
	clock_t preTime_; // 前の時刻を保持

	//~~~~~~Struct/Enum~~~~~~

	//~~~~~~Members~~~~~

	//~~~~~~functions~~~~~~~
};
#endif // SYSTEM_ANALYZER_H