#include <stdio.h>

int main(void)
{
    int a[5][5];
    int count;

    for(int i = 0; i < 5; i++)
    {
        for(int j = 0; j < 5; j++)
        {
            scanf("%d", &a[i][j]);
            //printf("%d\n", a[i][j]);
        }
    }

    if(a[2][2] == 1)
    {
        count = 0;
    }
    else if(a[2][1] == 1 || a[2][3] == 1 || a[1][2] == 1 || a[3][2] == 1)
    {
        count = 1;
    }
    else if(a[1][1] == 1|| a[1][3] == 1|| a[3][3] == 1 || a[3][1] == 1 || a[2][0] == 1 || a[0][2] == 1 || a[4][2] == 1 || a[2][4] == 1)
    {
        count = 2;
    }
    else if(a[1][0] == 1|| a[3][0] == 1|| a[0][1] == 1 || a[4][1] == 1 || a[4][3] == 1 || a[0][3] == 1 || a[1][4] == 1 || a[3][4] == 1)
    {
        count = 3;
    }
    else if(a[0][0] == 1 || a[0][4] == 1 || a[4][0] == 1 || a[4][4] == 1)
    {
        count = 4;
    }

    printf("%d\n", count);
}
