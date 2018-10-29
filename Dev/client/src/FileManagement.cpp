#include <fstream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>

#include "FileManagement.hpp"

using namespace std;
/*==============================================================================
 Public
==============================================================================*/

FileManagement::FileManagement(char *fname)
{
	ResizeVector_filedata();
	GetLineFile(fname);
}

FileManagement::~FileManagement(void) {}

/*==============================================================================
 Private
==============================================================================*/
void FileManagement::ResizeVector_filedata(void)
{
	filedata.resize(filelinenum);
	for (int i = 0; i < filelinenum; i++) {
		filedata[i].resize(stringnum);
	}
}

void FileManagement::GetLineFile(char *fname)
{
	ifstream fin;
	fin.open(fname, ios::binary);
	fin.read((char *)&filedata[0], filelinenum * sizeof(char) * stringnum);
	fin.close();
	fin.clear();
}