#include <stdio.h>

int main(void)
{
    long long var_ll = 0;
    long double var_ld = 0.;
    short sh = 0;
    scanf("%lld %f %hd", &var_ll, &var_ld, &sh);
    printf("%lld %hd", var_ll, sh);
    return 0;
}

// #include <stdio.h>

// int main(void)
// {
//     int a;
//     short b;
//     float c;
//     double d;

//     scanf("%i%hd%f%lf", &a, &b, &c, &d);
//     printf("%d %d %.2f %.2f", a, b, c, d);

//     return 0;
// }

// #include <stdio.h>

// int main()
// {
//     int a = 0, b = 0, c = 0;
//     int res_scan = scanf("%d, %d", &a, &b);
//     printf("%d %d", a, b);
//     return 0;
// }

// #include <stdio.h>

// int main(void)
// {
//     unsigned char h = 12, m = 3, s = 9;

//     printf("%#04x:%#04x:%#04x", h, m, s);

//     return 0;
// }

// #include <stdio.h>

// int main(void)
// {
//     int a1 = -123, a2 = 6, a3 = 1024;

//     printf("[%5d]\n[%5d]\n[%5d]\n", a1, a2, a3);

//     return 0;
// }

// #include <stdio.h>

// int main(void)
// {
//     char byte = 65;
//     unsigned short height = 1055;
//     int distance = 1000000;
//     float pi = 3.1415f;
//     printf("%c\n%d\n%d\n%f\n", byte, height, distance, pi);

//     return 0;
// }

// #include <stdio.h>

// int main(void)
// {
// char ch = 'u';
// short sh = -55;
// int var_i = 1024;
// double var_d = 3.1415;

// printf("%c %d %d %f\n", ch, sh, var_i, var_d);

//     unsigned height = 12345012;
//     long long dist = 1234567890LL;
//     long double weight = 45.7845;

//     printf("%u %lld %.4Lf\n", height, dist, weight);

//     return 0;
// }

// #include <stdio.h>

// int main(void)
// {
//     printf("Hello, world\n");
//     return 0;
// }
