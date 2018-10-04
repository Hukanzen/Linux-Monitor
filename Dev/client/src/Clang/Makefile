all: client.out

client.out: Main.cpp SystemAnalyzer.cpp Curl.cpp
	g++ -o $@ $^  -lcurl -std=c++11
	
clean:
	-rm *.o
	-rm client.out
