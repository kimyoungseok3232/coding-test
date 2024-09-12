// https://www.acmicpc.net/problem/10818

#include <stdio.h>
int main()
{
    int min = 1000000,max = -1000000,n,a;
    scanf("%d",&n);
    for(;n>0;n--)
    {
        scanf("%d",&a);
        if(min>a)
            min = a;
        if(max<a)
            max = a;
    }
    printf("%d %d",min,max);
}