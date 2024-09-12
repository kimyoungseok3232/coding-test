// https://www.acmicpc.net/problem/2439

#include <stdio.h>
int main()
{
    int a,b,n,m;
    scanf("%d",&n);
    for(a=1;n>0;n--)
    {
        for(b=n;b>1;b--)
                printf(" ");
        for(m=a;m>0;m--)
                printf("*");
        printf("\n");
        a++;
    }
}