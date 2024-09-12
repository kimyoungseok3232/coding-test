// https://www.acmicpc.net/problem/2753

#include <stdio.h>
int main()
{
    int a,b=0;
    scanf("%d",&a);
    if(a%4==0)
        b++;
    if(a%100==0)
        b--;
    if(a%400==0)
        b++;
    printf("%d",b);
}