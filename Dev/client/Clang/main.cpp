#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "SystemAnalyzer.hpp"

int main(void)
{

	SystemAnalyzer analyzer;
	int            nCPU = 4;

	uint cpuUsage = analyzer.GetCPUUsage(nCPU);
	uint memUsage = analyzer.GetMemoryUsage();
	uint diskUsage = analyzer.GetDiskUsage();
	
	fprintf(stdout,"%d,%d,%d",cpuUsage,memUsage,diskUsage);

	return 0;
}