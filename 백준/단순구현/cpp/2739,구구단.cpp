// https://www.acmicpc.net/problem/2739

#include <stdio.h>
int main()
{
    int a,b;
    scanf("%d",&a);
    for(b=1;b<10;b++)
    {
        printf("%d * %d = %d\n",a,b,a*b);
    }
}