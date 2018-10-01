all: client.out

main.o:main.cpp
	g++ -c -o $@ $<

SystemAnalyzer.o: SystemAnalyzer.cpp SystemAnalyzer.hpp
	g++ -c -o $@ SystemAnalyzer.cpp
	
Curl.o: Curl.cpp Curl.hpp
	g++ -c -o $@ Curl.cpp
	
client.out: main.o SystemAnalyzer.o Curl.o  -lcurl
	g++ -o $@ $^
	
clean:
	-rm *.o
	-rm client.out
