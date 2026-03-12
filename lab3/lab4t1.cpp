#include <iostream>
using namespace std;



//SWAP VALUES
void swapValues(int* p1, int* p2)
{
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}



//print array with pointer
void printArray(int* arr, int size)
{
    for(int i = 0; i < size; i++)
    {
        cout << *(arr + i) << " ";
    }
    cout << endl;
}



//find sum
int findSum(int* arr, int size)
{
    int sum = 0;

    for(int i = 0; i < size; i++)
    {
        sum += *(arr + i);
    }

    return sum;
}



//shift right
void shiftRight(int* arr, int size)
{
    int lastValue = *(arr + size - 1);

    for(int i = size - 1; i > 0; i--)
    {
        *(arr+ i) = *(arr + i - 1);
    }

    *arr = lastValue;
}



//CREATE ARRAY
int* createArray(int size)
{
    int* arr = new int[size];
    return arr;
}

//DELETE ARRAY
void deleteArray(int* arr)
{
    delete[] arr;
}

int main()
{
    cout << "Creating dynamic array..." << endl;

    int size;

    cout << "Enter array size: ";
    cin >> size;

    int* arr = createArray(size);

    cout << "enter values: ";

    for(int i = 0; i < size; i++)
    {
        cin >> *(arr + i);
    }

    cout << "array values:" << endl;
    printArray(arr, size);

    cout << "sum of values: " << findSum(arr, size) << endl;

    cout << "----------------------------------" << endl;

    int a = 5;
    int b = 8;

    cout << "swapping two numbers" << endl;

    cout << "before swap" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    swapValues(&a, &b);

    cout << "after swap" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;

    cout << "----------------------------------" << endl;

    cout << "shifting array to the right" << endl;

    shiftRight(arr, size);

    cout << "array after shiftRight: ";
    printArray(arr, size);

    cout << "----------------------------------" << endl;

    cout << "deleting array..." << endl;

    deleteArray(arr);

    cout << "memory released successfully." << endl;

    return 0;
}