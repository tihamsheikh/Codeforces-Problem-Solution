#include <stdio.h>

int main(void)
{
    int bit_1, bit_2, bit_3;
    int n;
    int fin = 0;

    scanf("%d", &n);

    for(int i = 0; i < n; i++)
    {
        int count = 0;

        scanf("%d %d %d", &bit_1, &bit_2, &bit_3);

        if((bit_1 == 0 || bit_1 == 1) && (bit_2 == 0 || bit_2 == 1) && (bit_3 == 0 || bit_3 == 1))
        {
            if((bit_1 == 1 && bit_2 == 1 && bit_3 == 1) || (bit_1 == 1 && bit_2 == 1 && bit_3 == 0) || (bit_1 == 1 && bit_2 == 0 && bit_3 == 1) || (bit_1 == 0 && bit_2 == 1 && bit_3 == 1))
            {
                count += 1;

                //printf("count = %d\n", count);
            }

        }

        if(count >= 1)
        {
            fin += 1;
        }
    }


    printf("%d\n", fin);
}
