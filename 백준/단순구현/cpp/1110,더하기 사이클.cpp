// https://www.acmicpc.net/problem/1110

#include <stdio.h>
int main()
{
    int A,a,n=0;
    scanf("%d",&a);
    A=a;
    do
    {
        a=a%10*10+(a/10+a%10)%10;
        n++;
    }
    while(a!=A);
    printf("%d",n);
}