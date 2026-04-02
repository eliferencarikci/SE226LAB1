#include <iostream>
using namespace std;

double S(int n) {
    //base case
    if (n==0)
        return 0;

    double sign;
    if (n%2==0)
        sign=-1;
    else
        sign=1;



    
    //recursive case
    return (sign/n)+S(n-1);
}


int main() {
    int n;
    cout<<"Enter value for n: ";
    cin>>n;

    double result = S(n);
    cout<<"Result:"<<result;

    return 0;


}