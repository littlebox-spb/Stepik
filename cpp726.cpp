#include <iostream>
#include <string>

int main()
{
    int count = 0;
    std::string s1 = "", s2 = "";
    std::cin >> count;
    for (int i = 0; i < count; i++)
    {
        getline(std::cin, s1);
        if (i == 0 or s1.size() > s2.size())
            s2 = s1;
    }
    std::cout << s2;
    return 0;
}