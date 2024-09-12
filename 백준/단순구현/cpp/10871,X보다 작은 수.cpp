// https://www.acmicpc.net/problem/10871

#include <stdio.h>
int main()
{
    int a,n,x;
    scanf("%d %d",&n,&x);
    for(;n>0;n--)
    {
        scanf("%d",&a);
        if(a<x)
            printf("%d ",a);
    }
}