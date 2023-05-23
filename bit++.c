#include <stdio.h>
#include <string.h>

int main(void)
{
    int n;
    int count = 0;
    char* in = "++X";
    char* in2 = "X++";
    char* de = "--X";
    char* de2 = "X--";

    scanf("%d", &n);

    char* ch[3];

    for(int i = 0; i < n; i++)
    {
        scanf("%s", &*ch);
        //ch[3] = '\0';
        //printf("%s\n", ch);

        if(strcmp(ch, in) == 0 || strcmp(ch, in2) == 0)
        {
            count++;
        }
        if(strcmp(ch, de) == 0 || strcmp(ch, de2) == 0)
        {
            count--;
        }
        //memset(ch, 0, strlen(ch));
    }
    printf("%d\n", count);
}
