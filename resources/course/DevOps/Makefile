CC=gcc
LDFLAGS=-lpcap
SRC=sniffex.c
BIN=sniffex


all: $(BIN)

sniffex: sniffex.c
	$(CC) $(CFLAGS) sniffex.c -o sniffex -lpcap
debug: sniffex.c
	$(CC) $(CFLAGS) sniffex.c -o sniffex -lpcap -D DEBUG
valgrind: sniffex.c
	$(CC) $(CFLAGS) sniffex.c -o sniffex -lpcap
	valgrind --tool=memcheck --leak-check=yes --show-reachable=yes --num-callers=20 --track-fds=yes ./sniffex
clean:
	rm -f sniffex
