#include <iostream>
using namespace std;

int main() {
    int n;
    int* arr = new int[n];
    int findNum;
    int cnt = 0;
    cin >> n;
    // 배열 입력 확인하기
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cin >> findNum;
    for (int i = 0; i < n; i++) {
        if (findNum == arr[i]) {
            cnt += 1;
        }
    }
    cout << cnt << endl;
    delete[] arr;
}