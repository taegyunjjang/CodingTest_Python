#include <iostream>
using namespace std;

int main()
{
    int num;
    int max = 0;
    int maxIdx = 0;

    for (int i = 1; i <= 9; i++)
    {
        cin >> num;
        if (max < num)
        {
            max = num;
            maxIdx = i;
        }
    }
    cout << max << endl;
    cout << maxIdx << endl;

    return 0;
}