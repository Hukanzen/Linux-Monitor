#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include "Curl.hpp"
#include "SystemAnalyzer.hpp"

#ifndef uint
#define uint unsigned int
#endif
#define N 128

int main(void)
{
	int            delay = 1;
	int            nCPU  = 4;
	SystemAnalyzer analyzer(delay);

	uint cpuUsage  = analyzer.GetCPUUsage(nCPU);
	uint memUsage  = analyzer.GetMemoryUsage();
	uint diskUsage = analyzer.GetDiskUsage();

#ifdef DEBUG
	fprintf(stdout, "%d,%d,%d", cpuUsage, memUsage, diskUsage);
#endif

	// myCurlLib      curlLib("http://localhost:40080/getdata.cgi");
	myCurlLib curlLib("http://host.docker.internal:40080/getdata.cgi");

	char ipaddr[N]   = {"2130706433"};
	char hostname[N] = {"hige"};
	char post[N];
	sprintf(post, "ipaddr=%s&delay=%d&cpu=%u&mem=%u&disk=%u&hostname=%s", ipaddr,
	        delay, cpuUsage, memUsage, diskUsage, hostname);
	curlLib.PostData(post);
	curlLib.Perform();

	fprintf(stdout, "%s\n", post);

	// fprintf(stdout,"HELLO\n");

	return 0;
}