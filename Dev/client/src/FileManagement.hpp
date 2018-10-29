#ifndef __FILEMANAGEMENT_H__
#define __FILEMANAGEMENT_H__

#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

class FileManagement
{
	public:
	/**
	 * @brief
	 * @param
	 * @return
	 */
	FileManagement(char *);
	~FileManagement(void);

	private:
	vector<vector<char>>
	    filedata; // 2次元配列　http://negi-magnet.hatenablog.com/entry/2013/01/13/225816
	int filelinenum = 32, stringnum = 32; // resize用データサイズ

	/**
	 * @brief
	 * @param
	 * @return
	 */
	void ResizeVector_filedata(void);

	/**
	 * @brief ファイルを読み込んで，配列に格納する
	 * @param ファイル名
	 * @return なし
	 */
	void GetLineFile(char *);
};

#endif