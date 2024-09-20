#include <iostream>

using namespace std;

int main()
{
    // put your code here
    int N, K, count = 0;
    cin >> N;
    int St[N];
    for (int i = 0; i < N; i++)
    {
        cin >> St[i];
    }
    cin >> K;
    for (int i = 0; i < N; i++)
    {
        if (K >= St[i])
            count++;
    }
    cout << count;
    return 0;
}