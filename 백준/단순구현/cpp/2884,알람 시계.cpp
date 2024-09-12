// https://www.acmicpc.net/problem/2884

#include <stdio.h>
int main()
{
    int a,b;
    scanf("%d %d",&a,&b);
    if(b<45)
    {
        if(a==0)
            a=23;
        else
            a--;
        b+=15;
    }
    else
        b-=45;
    printf("%d %d",a,b);
}