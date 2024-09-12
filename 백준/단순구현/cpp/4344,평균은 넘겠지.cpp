// https://www.acmicpc.net/problem/4344

#include <stdio.h>
int main()
{
    int x;
    scanf("%d",&x);
    for(;x>0;x--)
    {
        int n,m,ov=0;
        double avg=0;
        scanf("%d",&n);
        int sc[n];
        for(m=0;m<n;m++)
        {
            scanf("%d",&sc[m]);
            avg+=sc[m];
        }
        avg = avg/n;
        for(m=0;m<n;m++)
        {
            if(sc[m]>avg)
                ov++;
        }
        printf("%.3lf%\n",(double)ov/(double)n*100);
    }
}