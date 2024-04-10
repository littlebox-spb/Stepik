#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int n, m, s = 0;
    std::cin >> n >> m;
    std::vector<int> arr;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            int k;
            std::cin >> k;
            arr.push_back(k);
        }
        std::sort(begin(arr), end(arr));
        for (int j = 0; j < m; j++)
        {
            std::cout << arr[j] << " ";
        }
        arr.clear();
        std::cout << "\n";
    }
    return 0;
}

// #include <iostream>

// int main()
// {
//     int n, s = 0;
//     std::cin >> n;
//     for (int i = 0; i < n; i++)
//     {
//         for (int j = 0; j < n; j++)
//         {
//             if (i == n - 1 - j)
//             {
//                 std::cout << 1;
//             }
//             else
//             {
//                 if (i > n - 1 - j)
//                 {
//                     std::cout << 2;
//                 }
//                 else
//                 {
//                     std::cout << 0;
//                 }
//             }
//         }
//         std::cout << "\n";
//     }
//     return 0;
// }

// #include <iostream>
// #include <vector>

// int main()
// {
//     int n;
//     std::cin >> n;
//     std::vector<int> arr;
//     for (int i = 0; i < n; i++)
//     {
//         int k;
//         std::cin >> k;
//         if (arr.size() == 0)
//         {
//             arr.push_back(k);
//         }
//         else
//         {
//             int f = 0;
//             for (int j = 0; j < arr.size(); j++)
//             {
//                 if (k == arr[j])
//                 {
//                     f++;
//                 }
//             }
//             if (f == 0)
//             {
//                 arr.push_back(k);
//             }
//         }
//     }
//     std::cout << arr.size();

//     return 0;
// }