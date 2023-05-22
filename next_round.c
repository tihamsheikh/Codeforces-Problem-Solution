#include <stdio.h>

int main(void)
{
    int n, k;
    int a[100];
    int count = 0;

    scanf("%d %d", &n, &k);

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



//            if(a[i] > k)
//            {
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
                        if(a[i] >= k && count == 0)
                        {
                            for(int j = 0; j < n; j++)
                            {
                                if(a[j] >= k && a[j] >= a[j+1])
                                {
                                    count += 1;
                                }
                                if(j+1 == n)
                                {
                                    if(a[n-1] >= k)
                                    {
                                        count += 1;
                                    }
                                }
                            }
                        }
                        //count += 1;
                        //printf("-- count: %d | -- a[%d]: %d\n", count, i, a[i]);
                    }
//                    else
//                        continue;
//                }

                if((i+1) == n)
                {
                    if(a[n-1] > k)
                    {
                        count += 1;
                        //printf("%d -- %d\n", count, a[i]);
                    }
                }
            }

            if(a[i] == k && count < 1)
            {
                printf("foo\n");
                count += 1;
            }
            else if(a[i] == k && count+1 < 1)
            {
                printf("baz\n");
                count += 1;
            }
        }
    }

    //printf("%d\n", count);
    printf("%d\n", count);
}
