#include <bits/stdc++.h>

#define endl '\n'
using namespace std;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    stack<int> s;
    int N;
    cin >> N;
    cin.ignore();

    string str;
    int x;
    for (int i = 0; i < N; i++) {
        cin >> str;
        if (str == "push") {
            cin >> x;
            s.push(x);
        }
        else {
            if (str == "pop") {
                if (s.size() == 0) cout << -1 << endl;
                else {
                    int top = s.top();
                    s.pop();
                    cout << top << endl;
                }
            }
            else if (str == "size") cout << s.size() << endl;
            else if (str == "empty") cout << (s.empty() ? 1 : 0) << endl;
            else cout << (s.empty() ? -1 : s.top()) << endl;
        }
    }
}
