#include <iostream>
#include <vector>

int main()
{
    int n;
    std::cin >> n;
    std::vector<int> arr;
    for (int i = 0; i < n; i++)
    {
        int k;
        std::cin >> k;
        if (arr.size() == 0)
        {
            arr.push_back(k);
        }
        else
        {
            int f = 0;
            for (int j = 0; j < arr.size(); j++)
            {
                if (k == arr[j])
                {
                    f++;
                }
            }
            if (f == 0)
            {
                arr.push_back(k);
            }
        }
    }
    std::cout << arr.size();

    return 0;
}