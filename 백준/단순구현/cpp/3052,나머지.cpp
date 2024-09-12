// https://www.acmicpc.net/problem/3052

#include <stdio.h>
int main()
{
    int a,n=0,m,arr[42];
    for(m=0;m<42;m++)
    {
        arr[m]=0;
    }
    for(m=0;m<10;m++)
    {
        scanf("%d",&a);
        arr[a%42]=1;
    }
    for(m=0;m<42;m++)
    {
        if(arr[m]==1)
            n++;
    }
    printf("%d",n);
}