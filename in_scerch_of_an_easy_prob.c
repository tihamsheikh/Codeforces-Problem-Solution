#include <stdio.h>

int main(void)
{
    int n, p;

    int count = 0;

    scanf("%d", &n);

    for(int i = 0; i < n; i++)
    {
        scanf("%d", &p);

        //printf("%d\n", p);

        if(p == 1)
        {
            count++;
        }
    }

    if(count != 0)
    {
        printf("HARD\n");
    }
    else
    {
        printf("EASY\n");
    }
}
