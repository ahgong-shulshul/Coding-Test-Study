#include <iostream>
using namespace std;

int main() {
    int n;
    int x;
    int cnt = 0;
    int* arr = new int[n];
    cin >> n >> x;
    // 배열 입력받기
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    // x보다 작은 수 찾기
    for (int i = 0; i < n; i++) {
        if (arr[i] < x) {
            cout << arr[i] << ' ';
        }
    }
    delete[] arr;
}