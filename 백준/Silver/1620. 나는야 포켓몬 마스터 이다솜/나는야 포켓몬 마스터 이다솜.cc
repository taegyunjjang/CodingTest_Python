#include <bits/stdc++.h>

#define endl '\n'
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N, M;
    cin >> N >> M;

    map<string, int> m1;
    map<int, string> m2;

    string key;
    int val = 1;

    for (int i = 0; i < N; i++) {
        cin >> key;
        m1[key] = val;
        m2[val] = key;
        val++;
    }

    string input;
    for (int i = 0; i < M; i++) {
        cin >> input;
        if (isdigit(input[0])) {
            int num = stoi(input);
            cout << m2[num] << endl;
        }
        else cout << m1[input] << endl;
    }
}
