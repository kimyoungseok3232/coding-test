// https://www.acmicpc.net/problem/2577

#include <stdio.h>
int main()
{
    int a,b,c,abc,y,n[10];
    scanf("%d %d %d",&a,&b,&c);
    abc=a*b*c;
    for(y=0;y<10;y++)
    {
        n[y]=0;
    }
    while(abc>0)
    {
        for(y=0;y<10;y++)
        {
            if(abc%10==y)
                n[y]++;
        }
        abc=abc/10;
    }
        for(y=0;y<10;y++)
        {
            printf("%d\n",n[y]);
        }
}