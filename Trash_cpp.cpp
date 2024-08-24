#include <iostream>

using namespace std;

int main()
{
	int j = 1;
	int i = 10;
	int res = 1;
	while (i - j > 0)
	{
		j++;
		i--;
		res *= (i + j);
	}
	cout << res;
	return 0;
}