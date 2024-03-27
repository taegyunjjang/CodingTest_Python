#include <bits/stdc++.h>
#include <iostream>

#define endl '\n'
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        int A, B;
        cin >> A >> B;
        if (A == 0 && B == 0)
            break;
        cout << A + B << endl;
    }
}
