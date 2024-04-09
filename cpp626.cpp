#include <iostream>

int main()
{
    int x, y, m;
    std::cin >> x >> y;
    int arr[x][y];
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            std::cin >> arr[i][j];
            std::cout << arr[i][j] << " ";
            if (j == 0)
            {
                m = arr[i][j];
            }
            else if (m > arr[i][j])
            {
                m = arr[i][j];
            }
        }
        std::cout << m << " ";
    }
    return 0;
}