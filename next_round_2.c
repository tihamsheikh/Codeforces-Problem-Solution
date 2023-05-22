#include <stdio.h>

int main(void)
{
    int n, k;
    int count = 0;

    scanf("%d %d", &n, &k);

    int a[n];

    for(int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    for(int i = 0; i < n; i++)
    {
        if(a[i] >= a[k-1] && a[i] != 0)
        {
            count += 1;
        }
    }

    printf("%d\n", count);
}
