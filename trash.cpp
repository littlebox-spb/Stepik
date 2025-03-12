#include <iostream>

int main() {
    // put your code here
    int k1, k2, k3;
    std::cin>>k1>>k2>>k3;
    if (abs(k1-k2)>abs(k2-k3)) {
        std::cout<<abs(k1-k2);
    }
    else {
        std::cout<<abs(k2-k3);
    }
    return 0;
}