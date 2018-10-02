all: client.out

client.out: Main.cpp SystemAnalyzer.cpp Curl.cpp
	g++ -o $@ $^  -lcurl
	
clean:
	-rm *.o
	-rm client.out
