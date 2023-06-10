#include <stdio.h>

int main(void)
{
    int count = 0, count2 = 0;
    int max = 0, min = 0, xtra = 0;
    int n = 6;

    char s[100000], j[n];

    for(int i = 0; i < n; i++)
    {
        scanf("%c%c", &s[i], &j[i]);
        printf("%c\n", s[i]);
    }

    for(int i = 0; i < n; i++)
    {
        if(s[i] != s[i+1])
        {
            count++;
        }
    }

    printf("max: %d min: %d xtra: %d\n", max, min, xtra);
    printf("count: %d count2: %d\n", count, count2);
}
