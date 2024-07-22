#include <iostream>
using namespace std;

int main() {
    int max = 0;
    int maxIdx = 0;
    int temp;
    for (int i = 0; i < 9; i++) {
        cin >> temp;
        if (max < temp) {
            max = temp;
            maxIdx = i+1;
        }
    }
    cout << max << "\n" << maxIdx << endl;
}