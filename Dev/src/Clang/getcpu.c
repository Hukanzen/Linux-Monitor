#include <stdio.h>
#include <stdlib.h>

double getCPUUsage(int);
double getCPUUsage(int nCPU)
{
	FILE *stat;
	
	if((stat=fopen("/proc/stat","r"))==NULL){
		fprintf(stderr,"Cant open /proc/stat");
		return -1;
	}
	
	int usr,nice,sys;
	char buf[4]; // ファイル内の文字列CPU
	int ret=fscanf(stat,"%s %d %d %d",buf,&usr,&nice,&sys);
	if(ret==-1){
		fprintf(stderr,"Cant fscanf");
		return -1;
	}
	
	fclose(stat);
	
	return ((double)(usr+nice+sys))*100.0/(double)nCPU;
}


int main(void)
{
	int nCPU=4;
	double cu;
	cu=getCPUUsage(nCPU);
	printf("cpuUsage : %lf [par] \n",cu);
	
	return 0;
}