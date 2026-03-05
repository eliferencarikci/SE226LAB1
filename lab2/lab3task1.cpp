#include <iostream>
using namespace std;

int main() {

    int x;
    cout << "Please enter a positive integer greater than 1: ";
    cin >> x;

    int count = 0;

    cout << x;

    while (x != 1) {

        if (x % 2 == 0)
            x = x / 2;
        else
            x = x * 3 + 1;

        cout << " -> " << x;
        count++;
    }

    cout << endl << "Total Steps: " << count << endl;

    return 0;
}