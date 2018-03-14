#include<stdio.h>
#include<unistd.h>
#include<string.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<sys/types.h>

#define SERV_PORT 5576
int main(int argc,char **argv)
{
    
    char s[7]="message";
    // char f[80];
    struct sockaddr_in servaddr,cliaddr;
    int listenfd,connfd,clilen;
    listenfd=socket(AF_INET,SOCK_STREAM,0);
    bzero(&servaddr,sizeof(servaddr));
    servaddr.sin_family=AF_INET;
    servaddr.sin_port=htons(SERV_PORT);

    
    bind(listenfd,(struct sockaddr *)&servaddr,sizeof(servaddr));
    listen(listenfd,1);
    clilen=sizeof(cliaddr);
    int len=sizeof(servaddr);
    connfd=accept(listenfd,(struct sockaddr*)&servaddr,&len);
    printf("Client connectd\n");
    send(connfd,s,sizeof(s),0);
    printf("message sent");
    close(listenfd);
}
