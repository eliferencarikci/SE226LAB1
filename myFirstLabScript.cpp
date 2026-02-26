

#include <iostream>
#include <string>

using namespace std;

int main() {
    string name;
    string id;

    cout << "What is your name? ";
    getline(cin, name);
    cout << name << endl;
    cout << "Hello " << name << endl;

    cout << "What is your Student ID? ";
    getline(cin, id);
    cout << id << endl;
    cout << "Your student ID is " << id << endl;

    return 0;
}