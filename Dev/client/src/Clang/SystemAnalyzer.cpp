#include <arpa/inet.h>
#include <errno.h>
#include <iostream>
#include <linux/if.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <sys/statvfs.h>
#include <sys/sysinfo.h>
#include <sys/times.h>
#include <sys/types.h>
#include <unistd.h>

#include "SystemAnalyzer.hpp"

using namespace std;

/* =================================================================
 Public
=================================================================*/
SystemAnalyzer::SystemAnalyzer(int delay)
{
	preTick_ = GetPreTick_();
	preTime_ = times(NULL);
	sleep(delay);
}

SystemAnalyzer::~SystemAnalyzer(void) {}

char *SystemAnalyzer::GetIpAddr(const char *device)
{
	int s = socket(AF_INET, SOCK_STREAM, 0);

	struct ifreq ifr;
	ifr.ifr_addr.sa_family = AF_INET;
	strcpy(ifr.ifr_name, device);
	ioctl(s, SIOCGIFADDR, &ifr);
	close(s);

	struct sockaddr_in addr;
	memcpy(&addr, &ifr.ifr_ifru.ifru_addr, sizeof(struct sockaddr_in));
	return inet_ntoa(addr.sin_addr);
}

uint SystemAnalyzer::GetCPUUsage(int nCPU)
{
	unsigned int cpuUsage = 0;
	int          Tick_    = GetPreTick_();

	// 現在の時刻を取得
	clock_t now = times(NULL);

	// if (preTick_ == 0) { //一回目の呼び出しの場合
	// 	// 取得したTick値、時刻を保存
	// 	preTick_ = Tick_;
	// 	preTime_ = now;
	// 	return 0; //	0%を返す
	// }

	// CPU利用率を算出
	// この計算式では、100% x
	// CPUを最大値としたCPU使用率が計算されてしまうので、nCPUで割る
	cpuUsage = ((double)(Tick_ - preTick_) / (now - preTime_)) * 100.0 / nCPU;

	// 取得したTick値、時刻を保存
	preTick_ = Tick_;
	preTime_ = now;

	return cpuUsage;
}

uint SystemAnalyzer::GetMemoryUsage(void)
{
	struct sysinfo info;
	sysinfo(&info);

	//メモリの枚数で正規化
	unsigned long totalram = (info.totalram * info.mem_unit) / 1024;
	unsigned long freeram  = (info.freeram * info.mem_unit) / 1024;

	//メモリ使用量を計算
	unsigned int memoryUsage =
	    (double)(totalram - freeram) / (double)totalram * 100;

	return memoryUsage;
}

uint SystemAnalyzer::GetDiskUsage(void)
{
	unsigned int diskUsage = 0;

	//システムデータの読み込み
	struct statvfs buf;
	statvfs("/", &buf);

	float availableDisk = ((float)buf.f_frsize * (float)buf.f_bavail / 1024.0);
	float allDisk       = ((float)buf.f_frsize * (float)buf.f_blocks / 1024.0);

	//使用ディスク容量の計算
	diskUsage = 100.0 - availableDisk / allDisk * 100.0;

	return diskUsage;
}

double *SystemAnalyzer::GetLoadAverage(void)
{
	// double la[3];
	double *la;
	la = new double(3);

	getloadavg(la, 3);

	return la;
}

/* =================================================================
 Private
=================================================================*/
int SystemAnalyzer::GetPreTick_(void)
{
	// 演算に使用されたTick値を取得
	FILE *infile = fopen("/proc/stat", "r");
	if (NULL == infile) {
		cout << "[GetCPUUsage]<<Cannot open /srv/proc/stat" << endl;
		return 0;
	}

	int  usr, nice, sys;
	char buf[1024]; // 文字列"cpu"の部分の入力用
	int  result = fscanf(infile, "%s %d %d %d", buf, &usr, &nice, &sys);
	if (result == -1) {
		cout << "[GetCPUUsage]<<Cannot read fscanf" << endl;
		return 0;
	}
	fclose(infile);

	return usr + nice + sys;
}
