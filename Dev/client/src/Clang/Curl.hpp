#ifndef __Curl_HPP__
#define __Curl_HPP__

#include <curl/curl.h>

class myCurlLib
{

	private:
	void  Curl_Init(const char *);
	void  Curl_DeInit(void);
	CURL *curl;

	public:
	myCurlLib(const char *);
	~myCurlLib();

	void PostData(const char *);
	int  Perform(void);
};

#endif