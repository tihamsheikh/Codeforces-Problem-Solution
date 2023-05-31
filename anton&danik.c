#include <stdio.h>
#include <string.h>

int main(void)
{
    int anton = 0, dan = 0;
    int n;

    scanf("%d", &n); // takes the len of string

    char s[n];
    scanf("%s", &s); // takes the full input string

    for(int i = 0; i < n; i++)
    {
        if(s[i] == 'A')
        {
            anton++;
        }
        else if(s[i] == 'D')
        {
            dan++;
        }
    }
    //printf("%d %d\n", anton, dan);

    if(anton > dan)
    {
        printf("Anton\n");
    }
    else if(dan > anton)
    {
        printf("Danik\n");
    }
    else
    {
        printf("Friendship\n");
    }
}
