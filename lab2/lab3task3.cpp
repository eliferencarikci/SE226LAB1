#include <iostream>
using namespace std;

int main() {
    int n;

    while (true) {
        cout << "Please enter a number between 3 and 9: ";
        cin >> n;

        if (n >= 3 && n <= 9)
            break;

        cout << "Invalid input. Please enter a number between 3 and 9" << endl;
    }

    for (int i = 1; i < 2 * n; i++) {
        if (i <= n) {
            for (int j = 0; j < i; j++)
                cout << "*";
        }
        else {
            for (int j = 0; j < 2 * n - i; j++)
                cout << "*";
        }
        cout << endl;
    }

    return 0;
}