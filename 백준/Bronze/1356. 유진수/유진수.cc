#include <bits/stdc++.h>

#define endl '\n'
using namespace std;

int main()
{
    string str;
    cin >> str;
    int l = str.length();

    if (l == 1) {
        cout << "NO" << endl;
        exit(0);
    }

    int tmp = 1;
    for (int i = 0; i < l; i++){
        int num = str[i] - '0';
        tmp *= num;

        int cmp = 1;
        for (int j = i + 1; j < l; j++){
            int n = str[j] - '0';
            cmp *= n;
        }

        if (tmp == cmp){
            cout << "YES" << endl;
            exit(0);
        }

    }
    cout << "NO" << endl;

}