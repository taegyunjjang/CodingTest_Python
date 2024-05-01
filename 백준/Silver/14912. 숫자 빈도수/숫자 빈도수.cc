#include <bits/stdc++.h>

#define endl '\n'
using namespace std;

int main()
{
    int n, d;
    cin >> n >> d;

    int cnt = 0;
    for (int i = 1; i <= n; i++)
    {
        string str = to_string(i);
        for (char ch : str)
        {
            int num = ch - '0';
            if (d == num)
                cnt += 1;
        }
    }
    cout << cnt << endl;
}