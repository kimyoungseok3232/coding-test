// https://www.acmicpc.net/problem/2562

#include <stdio.h>
int main() 
{
    int arr[9], big = 0, m;
    for (int i = 0; i < 9; i++)
    {
        scanf("%d", &arr[i]);
        if (arr[i] > big)
        {
            big = arr[i];
            m = i;
        }
    }
    printf("%d\n%d", big, m+1);
}