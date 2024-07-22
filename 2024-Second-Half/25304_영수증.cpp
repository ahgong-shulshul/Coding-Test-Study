#include <iostream>
using namespace std;

int main() {
    int total;
    int n;
    int sum = 0;
    cin >> total;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int money;
        int num;
        cin >> money >> num;
        sum += money * num;
    }

    if (total == sum) {
        cout << "Yes" << endl;
    }
    else {
        cout << "No" << endl;
    }
}