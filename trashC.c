#include <stdio.h>

int main(void)
{
    int n, m;
    // if (scanf("%hhd %hhd", &n, &m) != 2)
    //     printf("Error");
    scanf("%hh %hh", &n, &m);
    printf("%d %d", &n, &m);
    while (m > n)
    {
        if (!n % 3)
            printf("%d ", n);
        n++;
    }
    return 0;
}

// #include <stdio.h>

// int main(void)
// {
//     int rect_width = 640, rect_height = 480;
//     int w = 1, h = 1, res = 0;
//     //    scanf("%d; %d", &w, &h);
//     w = 64;
//     h = 42;
//     if ((rect_width % w))
//     {
//         res += rect_height / h + 1;
//     }
//     if ((rect_height % h))
//     {
//         res += rect_width / w;
//     }

//     printf("%d", res);

//     return 0;
// }