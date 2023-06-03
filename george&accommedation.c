#include <stdio.h>

int main(void)
{
    int n;
    int count = 0;
    int q, p;

    scanf("%d", &n);

    for(int i = 0; i < n; i++)
    {
        scanf("%d %d", &p, &q);

        if((p+2) <= q)
        {
            count++;
            //printf("p+2: %d p: %d q: %d count: %d\n", p+2, p, q, count);
        }
    }
    printf("%d\n", count);
}
