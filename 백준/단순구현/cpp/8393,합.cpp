// https://www.acmicpc.net/problem/8393

#include <stdio.h>
int main()
{
    int a,n;
    scanf("%d",&n);
    for(a=0;n>0;n--)
    {
        a+=n;
    }
    printf("%d",a);
}