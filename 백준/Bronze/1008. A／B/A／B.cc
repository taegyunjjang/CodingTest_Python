#include <iostream>
using namespace std;

int main() {
    double a, b;
    cin >> a >> b;
    // 정답과 출력값의 절대오차 또는 상대오차가 10^-9 이하
    cout.precision(10);
    cout << a / b << endl;
    return 0;
}