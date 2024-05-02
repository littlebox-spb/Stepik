#include <stdio.h>

int main(void)
{
    char symbol;
    if (scanf("%c", &symbol) != 1)
    {
        printf("Input error.");
        return 0;
    }

    switch (symbol)
    {
    case 'e':
        symbol = 'E';
    }
    printf("%c", symbol);

    return 0;
}