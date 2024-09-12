// https://www.acmicpc.net/problem/2438

#include <stdio.h>
int main()
{
    int a,n,m;
    scanf("%d",&n);
    for(a=1;n>0;n--)
    {
        for(m=a;m>0;m--)
                printf("*");
        printf("\n");
        a++;
    }
}