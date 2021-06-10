#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <limits.h>
#include <string.h>
#include <ifaddrs.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netdb.h>



#include "helper.h"

void sendMessage(){
	printf("Correct Port.\n");
}
void sendMessageIP(){
	printf("Correct IP Located.\n");
}
void sendMessageState(){
	printf("Arbitrary Knocking...[STATE]\n");
}

int validator(char* ipAddr){
	struct ifaddrs *ifaddr, *ifa;
	int family, s;
	char host[NI_MAXHOST];

	if (getifaddrs(&ifaddr) == -1){
		perror("getifaddrs");
		exit(EXIT_FAILURE);
	}
	for (ifa = ifaddr; ifa != NULL; ifa = ifa->ifa_next)
	{
        if (ifa->ifa_addr == NULL)
            continue;

        s=getnameinfo(ifa->ifa_addr,sizeof(struct sockaddr_in),host, NI_MAXHOST, NULL, 0, NI_NUMERICHOST);
        if((ifa->ifa_addr->sa_family==AF_INET))
        {
            if (s != 0)
            {
                printf("getnameinfo() failed: %s\n", gai_strerror(s));
                exit(EXIT_FAILURE);
            }
            if (strcmp(host, ipAddr)==0){
		#ifdef DEBUG
                	printf("\tInterface : <%s>\n",ifa->ifa_name );
                	printf("\t  Address : <%s>\n", host);
		#endif
                return 0;
        }
    }
    }
    freeifaddrs(ifaddr);
	return 1;
}
void deleteSelf(char*string){
	remove(string); 
	return;
}
/*
int main(int argc, char **argv){
	validator("127.0.0.1");
	return 0;
}
*/