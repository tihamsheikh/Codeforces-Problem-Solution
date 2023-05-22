#include <stdio.h>

int main(void)
{
    int n, k;

    int count = 0;

    scanf("%d %d", &n, &k);
    int a[n];

    if(n >= k && n > 0 && n <= 50 && k > 0 && k <= 50)
    {
        //printf("working\n");

        for(int i = 0; i < n; i++)
        {
            scanf("%d", &a[i]);
            //printf("%d\n", a[i]);
        }

        for(int i = 0; i < n; i++)
        {
            //printf("1. count: %d\n", count);

            //printf("fine\n");

            if(n == 1)
            {
                count = 1;
                break;
            }



            if(a[i] > k && a[i] != 0)
            {
               //printf("1- count: %d | 1- a[%d]: %d\n", count, i, a[i]);
               // Fuck you

                if(i < n)
                {
                    if(a[i] >= a[i+1])
                    {
                        if(a[i] > k)
                        {
                            count += 1;
                        }

                        //count += 1;
                        //printf("-- count: %d | -- a[%d]: %d\n", count, i, a[i]);
                    }
//                    else
//                        continue;
                }

                if((i+1) == n)
                {
                    if(a[n-1] > k)
                    {
                        count += 1;
//                        //printf("%d -- %d\n", count, a[i]);
                    }
                }
            }
            else if(count == 0 && a[i] != 0)
            {
                for(int j = 0; j < n; j++)
                {
                    if(a[i] == a[i+1])
                    {
                        count += 1;
                    }
                    if(i+1 == n)
                    {
                        if(a[n-1] == a[n-2])
                        {
                            count += 1;
                        }
                    }
                }
            }
        }
    }

    //printf("%d\n", count);
    printf("%d\n", count);
}
