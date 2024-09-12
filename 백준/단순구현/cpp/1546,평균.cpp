// https://www.acmicpc.net/problem/1546

#include <stdio.h>
int main()
{
    int n,m;
    double ev=0,a[1000],max=0;
    scanf("%d",&n);
    for(m=0;m<n;m++)
    {
        scanf("%lf",&a[m]);
        if(a[m]>max)
            max=a[m];
    }
    for(m=0;m<n;m++)
    {
        a[m]=100*a[m]/max;
        ev+=a[m];
    }
    ev = ev/n;
    printf("%lf",ev);
}