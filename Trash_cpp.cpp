#include <iostream>

using namespace std;

int main() {
	int x = 1;
	int i = 10;
	while (i > 0) {
		x *= i;
		i--;
	}
	cout << x;
    return 0;
};