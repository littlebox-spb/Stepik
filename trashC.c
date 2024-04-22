#include <stdio.h>

int main(void)
{
    int rect_width = 640, rect_height = 480;
    int w = 1, h = 1, res = 0;
    //    scanf("%d; %d", &w, &h);
    w = 64;
    h = 42;
    if ((rect_width % w))
    {
        res += rect_height / h + 1;
    }
    if ((rect_height % h))
    {
        res += rect_width / w;
    }

    printf("%d", res);

    return 0;
}