#include <iostream>

using namespace std;

int f(int a, int b, int c)
{
	return (a * 3 + b * 2 + c) / (a + b + c);
}

int main()
{
	int a = 5;
	int b = 4;
	int c = 3;
	cout << f(a, b, c);
	return 0;
}