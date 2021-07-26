CC=g++
CCFLAGS=-g3 -Wall -w -pedantic -fmessage-length=0

O_FILES = avalon.o strings.o player.o load.o commands.o states.o globals.o comms.o room.o

avalon : $(O_FILES)
	$(CC) $(CCFLAGS) -o avalon $(O_FILES)

# dependency stuff, see: http://www.cs.berkeley.edu/~smcpeak/autodepend/autodepend.html
# pull in dependency info for *existing* .o files
-include $(O_FILES:.o=.d)

.SUFFIXES : .o .cpp

.cpp.o :  
	$(CC) $(CCFLAGS) -c $<
	$(CC) -MM $(CFLAGS) $*.cpp > $*.d

clean:
	rm -f avalon *.o *.d