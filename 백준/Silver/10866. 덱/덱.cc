#include <bits/stdc++.h>

#define endl '\n'
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    deque<int> dq;

    int N;
    cin >> N;

    string command;
    int x;
    for (int i = 0; i < N; i++) {
        cin >> command;
        if (command == "push_back") {
            cin >> x;
            dq.push_back(x);
        }
        else if (command == "push_front") {
            cin >> x;
            dq.push_front(x);
        }
        else if (command == "pop_front") {
            if (dq.empty()) cout << -1 << endl;
            else {
                int front = dq.front();
                dq.pop_front();
                cout << front << endl;
            }
        }
        else if (command == "pop_back") {
            if (dq.empty()) cout << -1 << endl;
            else {
                int back = dq.back();
                dq.pop_back();
                cout << back << endl;
            }
        }
        else if (command == "size") cout << dq.size() << endl;
        else if (command == "empty") cout << (dq.empty() ? 1 : 0) << endl;
        else if (command == "front") cout << (dq.empty() ? -1 : dq.front()) << endl;
        else cout << (dq.empty() ? -1 : dq.back()) << endl;
    }
}
