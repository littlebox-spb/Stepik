#include <iostream>

int main()
{
    int n;
    std::cin >> n;
    int arr[n], arr_count[n];
    for (int i = 0; i < n; i++)
    {
        std::cin >> arr[i];
        arr_count[i] = 0;
    }
    for (int i = 0; i < n; i++)
    {
        z = 0;
        for (int j = 0; j < n; j++)
        {
            if (arr[i] == arr[j])
            {
                arr_count[j]++;
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        if (arr_count[i] == 1 or arr_count[i] == 2)
        {
            std::cout << arr[i] << " ";
        }
    }
    return 0;
}