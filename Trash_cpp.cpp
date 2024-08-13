#include <iostream>

using namespace std;

int main()
{
    int x = 20;
    int y = 50;
    bool z = (y == x || y > x);
    float w = 3.14;
    if ((x & y) == 16 && z | w)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }
    return 0;
};