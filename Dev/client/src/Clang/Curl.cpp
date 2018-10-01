#include <curl/curl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "Curl.hpp"

#define DEBUG

myCurlLib::myCurlLib(const char *url) { Curl_Init(url); }

myCurlLib::~myCurlLib() { Curl_DeInit(); }

void myCurlLib::Curl_Init(const char *url)
{
	curl = curl_easy_init();
	curl_easy_setopt(curl, CURLOPT_URL, url);
	curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0);
}

void myCurlLib::Curl_DeInit(void) { curl_easy_cleanup(curl); }

void myCurlLib::PostData(const char *post_data)
{
	curl_easy_setopt(curl, CURLOPT_POST, 1);
	curl_easy_setopt(curl, CURLOPT_POSTFIELDS, post_data);
	curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, strlen(post_data));
}

int myCurlLib::Perform(void)
{
	int res = curl_easy_perform(curl);
#ifdef DEBUG
	printf("res = %d\n", res);
#endif
	return res;
}