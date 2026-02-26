#include <iostream>
using namespace std;

int main() {
    int total_seconds;

    cout << "Enter a total number of seconds: ";
    cin >> total_seconds;

    int hours = total_seconds / 3600;
    int remaining = total_seconds % 3600;

    int minutes = remaining / 60;
    int seconds = remaining % 60;

    cout << total_seconds << " seconds is "
         << hours << " hours, "
         << minutes << " minutes, and "
         << seconds << " seconds." << endl;

    return 0;
}