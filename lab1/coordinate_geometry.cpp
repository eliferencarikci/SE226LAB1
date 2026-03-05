
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double x1, y1, x2, y2;

    cout << "Point x1: ";
    cin >> x1;

    cout << "Point y1: ";
    cin >> y1;

    cout << "Point x2: ";
    cin >> x2;

    cout << "Point y2: ";
    cin >> y2;

    double distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

    cout << "Distance between points = " << distance << endl;

    return 0;
}