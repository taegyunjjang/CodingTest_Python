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

    map<string, int> m;
    
    string name;
    for (int i = 0; i < N; i++) {
        cin >> name;
        m.insert({name, 1});
    }

    int cnt = 0;
    vector<string> v;
    for (int i = 0; i < M; i++) {
        cin >> name;
        if (m.find(name) != m.end()) {
            cnt++;
            v.push_back(name);
        }
    }
    
    sort(v.begin(), v.end());
    cout << cnt << endl;
    for (string &i: v) cout << i << endl;
}
