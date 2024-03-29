#include <bits/stdc++.h>

#define endl '\n'
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    queue<int> q;

    int N;
    cin >> N;

    string command;
    int x;

    for (int i = 0; i < N; i++) {
        cin >> command;
        if (command == "push") {
            cin >> x;
            q.push(x);
        }
        else {
            if (command == "pop") {
                if (q.empty()) cout << -1 << endl;
                else {
                    int front = q.front();
                    q.pop();
                    cout << front << endl;
                }
            }
            else if (command == "size") cout << q.size() << endl;
            else if (command == "empty") cout << (q.empty() ? 1 : 0) << endl;
            else if (command == "front") cout << (q.empty() ? -1 : q.front()) << endl;
            else cout << (q.empty() ? -1 : q.back()) << endl;
        }
    }
}
