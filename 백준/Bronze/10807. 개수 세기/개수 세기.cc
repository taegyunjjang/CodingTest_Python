#include <bits/stdc++.h>
#include <iostream>

#define endl '\n'
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    int arr[N];
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    int v;
    cin >> v;

    int cnt = 0;
    for (int i = 0; i < N; i++)
        if (arr[i] == v)
            cnt += 1;

    cout << cnt << endl;
}
