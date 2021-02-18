#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int a, b;
    scanf("%d\n%d", &a, &b);
    int index;
    for(index = a; index<=b;index++) {
        if(index > 0 && index <= 9) {
            if(index == 1) 
                printf("one");
            if(index == 2)
                printf("two");
            if (index == 3)
                printf("three");
            if (index == 4)
                printf("four");
            if (index == 5)
                printf("five");
            if (index == 6)
                printf("six");
            if (index == 7)
                printf("seven");
            if (index == 8)
                printf("eight");
            if (index == 9)
                printf("nine");
        } 
        if(index > 9) {
            if(index % 2 == 0)
                printf("even");
            if(index % 2 != 0)
                printf("odd");
        }
        printf("\n");
    }

    return 0;
}
