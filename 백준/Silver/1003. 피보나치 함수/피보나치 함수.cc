#include <iostream>
using namespace std;

int main()
{
    int num, n;
    int max = 1;
    int arr[40];
    arr[0] = 1; arr[1] = 1;
    
    cin >> num;
    int iArr[num];

    for (int i = 0; i < num; i++) {
        cin >> n;
        iArr[i] = n;

        if (max < n) {
            max = n;
        }
    }

    for (int j = 2; j <= max; j++) {
        arr[j] = arr[j - 2] + arr[j - 1];
    }
    

    for (int k = 0; k < num; k++)
    {
        if (iArr[k] == 0) {
            cout << "1 0" << endl;
        } else if (iArr[k] == 1) {
            cout << "0 1" << endl;
        } else {
            cout << arr[iArr[k] - 2] << " " << arr[iArr[k] - 1] << endl;
        }
    }

    return 0;
}