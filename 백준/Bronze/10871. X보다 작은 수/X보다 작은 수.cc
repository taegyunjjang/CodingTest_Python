#include <bits/stdc++.h>
#include <iostream>

#define endl '\n'
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, X;
    cin >> N >> X;
    int arr[N];
    for (int i = 0; i < N; i++) 
        cin >> arr[i];
    for (int i = 0; i < N; i++) {
        if (arr[i] < X)
            cout << arr[i] << ' ';
    }    
}
