#include <iostream>
using namespace std;

int main()
{
    int n, tot = 0;
    cin >> n;

    for (int i = 1; i <= n; i ++)
    {
        tot += i;
    }
    cout << tot << endl;
    return 0;
}