/**
 * @file curl.hpp
 * @brief Linuxにおいて，C言語上でcurlを実現する．
 * @Auther Hukanzen
 */

#ifndef __Curl_HPP__
#define __Curl_HPP__

#include <curl/curl.h>

class myCurlLib
{

	private:
	/* CURL型ポインタ */
	CURL *curl;

	/**
	 * @brief Curlの初期化
	 * @param アクセス先URL
	 * @return
	 */
	void Curl_Init(const char *);

	/**
	 * @brief Curlの終了
	 * @param
	 * @return
	 */
	void Curl_DeInit(void);

	public:
	myCurlLib(const char *);
	~myCurlLib();

	/**
	 * @brief Post method用の準備を行う
	 * @param Post用データ
	 * @return
	 */
	void PostData(const char *);

	/**
	 * @brief アクセスを実行する
	 * @param
	 * @return 成功:0
	 */
	int Perform(void);
};

#endif