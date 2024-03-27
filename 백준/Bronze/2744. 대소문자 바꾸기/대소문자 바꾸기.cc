#include <bits/stdc++.h>
#include <iostream>

#define endl '\n'
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    getline(cin, S);

    for (int i = 0; i < S.length(); i++)
    {
        if (S[i] >= 'a' && S[i] <= 'z')
            cout << static_cast<char>(toupper(S[i]));
        else
            cout << static_cast<char>(tolower(S[i]));
    }
    cout << endl;
}
