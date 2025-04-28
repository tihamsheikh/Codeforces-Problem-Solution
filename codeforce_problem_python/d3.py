# include <stdio.h>
# include <stdlib.h>

typedef
struct
{
    char * name[32];
int
number;
}
person;

int
main()
{
    person
me, you;

me.name[0] = "Hemie";
me.number = "927237";
you.name[1] = "Siodn";
you.number = "3847394";

printf("%d\n", me.name[0]);
printf("%d\n", me.number);
printf("%d\n", you.name[1]);
printf("%d\n", you.number);
}
--