#include <bits/stdc++.h>
#include <iostream>

#define endl '\n'
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int arr[30] = {
        0,
    };

    int num;
    for (int i = 0; i < 28; i++)
    {
        cin >> num;
        arr[num - 1] = 1;
    }

    for (int i = 0; i < 30; i++)
        if (arr[i] == 0)
            cout << i + 1 << endl;
}
