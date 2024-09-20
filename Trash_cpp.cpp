#include <iostream>

using namespace std;

int main()
{
	// put your code here
	int N, K;
	cin >> N;
	int St[N];
	for (int i = 0; i < N; i++)
		cin >> St[i];
	cin >> K;
	for (int i = 0; i < N; i++)
	{
		if (K % St[i] == 0)
			cout << i + 1;
		if (i < N - 1)
			cout << ' ';
	}
	return 0;
}