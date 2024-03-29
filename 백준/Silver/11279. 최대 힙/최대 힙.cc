#include <bits/stdc++.h>

#define endl '\n'
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N;
    cin >> N;

    priority_queue<int> pq;

    int x;
    for (int i = 0; i < N; i++) {
        cin >> x;
        if (x == 0) {
            if (pq.empty()) cout << 0 << endl;
            else {
                int top = pq.top();
                pq.pop();
                cout << top << endl;
            }
        }
        else pq.push(x);
    }
}
