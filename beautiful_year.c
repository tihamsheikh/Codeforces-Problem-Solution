#include <stdio.h>

int distinct(int n);

int main(void)
{
    int n;

    scanf("%d", &n);

    n += 1;

    while(!distinct(n))
    {
        n++;
    }


    printf("%d\n", n) ;

}

int distinct(int n)
{
    int dist[10] = {0};

    while(n > 0)
    {
        int digit = n%10;

        if(dist[digit] == 1)
        {
            return 0;
        }

        dist[digit] = 1;
        n /= 10;
    }
    return 1;
}
