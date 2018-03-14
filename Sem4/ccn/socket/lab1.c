#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<errno.h>
main()
{
    int sock,cli;
     struct sockaddr_in server,clientDetail;
    unsigned int len;
    char mesg[] ="Hello world  ";
    int sentconf;
    if((sock=socket(PF_INET,SOCK_STREAM,0))==-1)
    {
        perror("There are some issues creating a socket:");
        exit(-1);
    }
    server.sin_family=AF_INET;
    server.sin_port=htons(10000);
    server.sin_addr.s_addr=INADDR_ANY;
    bzero(&server.sin_zero,8);
    len=sizeof(server);
    if((bind(sock,(struct sockaddr*)&server,len))==-1)
    {
        perror("Error in binding");
        exit(-1);
    }
    if((listen(sock,5))==-1)
    {
        perror("Error in listening");
        exit(-1);
    }
    while(1)
    {
        if((cli=accept(sock,(struct sockaddr*)&clientDetail,&len))==-1)
        {
            perror("Error in Accepting");
            exit(-1);
        }
        sentconf=send(cli,mesg,strlen(mesg),0);
        printf("Sending %d bytes to clientDetail : %s\n",sentconf,inet_ntoa(clientDetail.sin_addr));
        close(cli);
    }
}