#include <stdio.h>
#include <math.h>

int main(void)
{
    int count = 0;
    int l, b;

    scanf("%d %d", &l, &b);

    // 1 <= lukman <= bob <= 10

    for(int i = l; i <= b; i++) // luk * 3 and bob * 2
    {
        count++;

        //printf("%d %d\n", l, b);

        l *= 3;
        b *= 2;


        if(l > b)
        {
            break;
        }
    }
    printf("%d\n", count);
}
