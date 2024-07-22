#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int num = n / 4;
    for (int i = 0; i < num; i++) {
        cout << "long ";
    }
    cout << "int" << endl;
}