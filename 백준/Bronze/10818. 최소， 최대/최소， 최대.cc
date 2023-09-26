#include <iostream>
using namespace std;

int main()
{
    int N;
    cin >> N;

    int num;
    cin >> num;
    
    int m = num;
    int M = num;

    for (int i = 1; i < N; i++)
    {
        cin >> num;
        if (m > num)
        {
            m = num;
        }
        if (M < num)
        {
            M = num;
        }
    }

    cout << m << " " << M << endl;
    return 0;
}