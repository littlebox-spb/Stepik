#include <iostream>

int main()
{
    int n, count = 0;
    std::cin >> n;

    for (n; n != 0; n /= 10)
    {
        if ((n % 10) % 2 == 0)
        {
            count += 1;
        }
    }
    std::cout << count;
    return 0;
}