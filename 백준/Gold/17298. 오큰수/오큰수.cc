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
    vector<int> v(N);
    vector<int> answer;

    for (auto &i : v)
        cin >> i;

    //  3 5 2 7
    for (int i = N - 1; i >= 0; i--)
    {
        int num = v[i];
        if (s.empty())
        {
            s.push(num);
            answer.push_back(-1);
        }
        else
        {
            if (s.top() > num)
            {
                answer.push_back(s.top());
                s.push(num);
            }
            else
            {
                while (s.top() <= num)
                {
                    s.pop();
                    if (s.empty())
                        break;
                }

                if (s.empty())
                {
                    s.push(num);
                    answer.push_back(-1);
                }
                else
                {
                    answer.push_back(s.top());
                    s.push(num);
                }
            }
        }
    }

    for (int i = N - 1; i >= 0; i--)
        cout << answer[i] << ' ';
    cout << endl;
}