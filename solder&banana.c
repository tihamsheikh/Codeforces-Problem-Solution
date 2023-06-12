#include <stdio.h>
#include <math.h>

int main(void)
{
    int sum = 0, main_sum = 0, total;
    int banana, money, price; // price is the price per banana

//    banana = 4;
//    money = 17;
//    price = 0;

    scanf("%d %d %d", &price, &money, &banana);

    for(int i = 1; i <= banana; i++)
    {
        sum = i * price;
        //printf("%d\n", sum);
        main_sum += sum;
        //printf("%d\n", main_sum);
    }
    //printf("_%d_\n", main_sum);

    total = money - main_sum;

    if(total < 0)
    {
        printf("%d\n", abs(total));
    }
    else
    {
        total = 0;
        printf("%d\n", total);
    }
}
