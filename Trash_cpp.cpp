#include <iostream>

using namespace std;

// Объявление и определение функции
void increment(int &num)
{
	num++;
}

int main()
{
	int num = 5;

	cout << "Before increment: " << num << endl;

	// Calling the increment function and passing num by reference
	increment(num);

	cout << "After increment: " << num << endl;

	return 0;
}