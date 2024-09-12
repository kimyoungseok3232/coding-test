// https://www.acmicpc.net/problem/2588

#include <stdio.h>
int main()
{
    int a,b,c,d;
    scanf("%d %1d %1d %1d",&a,&b,&c,&d);
printf("%d\n%d\n%d\n%d",a*d,a*c,a*b,100*a*b+10*a*c+a*d);
}