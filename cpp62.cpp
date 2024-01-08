#include <iostream>

int main()
{
    int n, m;
    std::cin >> n >> m;
    int arr[n][m];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            std::cin >> arr[i][j];
        }
    }
    int min = arr[0][0], mi = 0, mj = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (min > arr[i][j])
            {
                min = arr[i][j];
                mi = i;
                mj = j;
                std::cout << min << " " << mi << " " << mj << "\n";
            }
        }
    }
    std::cout << mi << " " << mj;
    return 0;
}