#include <bits/stdc++.h>
// #include <iostream>

#define endl '\n'
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N;
    cin >> N;

    int n;
    int count[10001] = {
        0,
    };

    for (int i = 0; i < N; i++)
    {
        cin >> n;
        count[n]++;
    }

    for (int i = 1; i <= 10000; i++)
        for (int j = 0; j < count[i]; j++)
            cout << i << endl;
}
