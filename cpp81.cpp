#include <iostream>
#include <string>
using namespace std;

struct product {
    string name;
    int weight;
    int price;    
};

int main() {
    // put your code here
    product p[5];
    int weight=0;
    int price=0;
    for(int i;i<5;i++) {
        cin>>p[i].name>>p[i].weight>>p[i].price;
        weight+=p[i].weight;
        price+=p[i].price;               
    }
    cout<<weight<<" "<<price<<endl;
    return 0;
}