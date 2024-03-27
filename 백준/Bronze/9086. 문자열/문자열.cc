#include <bits/stdc++.h>
#include <iostream>

#define endl '\n'
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    string str;
    for (int i = 0; i < T; i++)
    {
        cin >> str;
        if (str.length() > 1)
            cout << str[0] << str[str.length() - 1] << endl;
        else
            cout << str[0] << str[0] << endl;
    }
}
