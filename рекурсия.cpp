#include <iostream>
using namespace std;

int pow(int x, int y)
{
    if (y == 0)
        return 1;
    else
        return x * pow(x, y - 1);
}

int main()
{
    // put your code here
    int x, y;
    cin >> x >> y;
    cout << x << " " << y << endl;
    cout << pow(x, y);
    return 0;
}