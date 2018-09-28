#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "SystemAnalyzer.hpp"

int main(void)
{

	SystemAnalyzer analyzer;
	int            nCPU = 4;

	uint cpuUsage = analyzer.GetCPUUsage(nCPU);
	printf("cpuUsage : %d\n", cpuUsage);

	uint memUsage = analyzer.GetMemoryUsage();
	printf("memUsage : %d\n", memUsage);

	uint diskUsage = analyzer.GetDiskUsage();
	printf("diskUsage : %d\n", diskUsage);

	return 0;
}