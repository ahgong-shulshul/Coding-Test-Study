/*
* [백준 17609] 회문
* 회문(回文) 또는 팰린드롬(palindrome)은 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열을 말한다. 
* 예를 들어 ‘abba’ ‘kayak’, ‘reviver’, ‘madam’은 모두 회문이다. 만일 그 자체는 회문이 아니지만 한 문자를 삭제하여 회문으로 만들 수 있는 문자열이라면 우리는 이런 문자열을 “유사회문”(pseudo palindrome)이라고 부른다. 
* 예를 들어 ‘summuus’는 5번째나 혹은 6번째 문자 ‘u’를 제거하여 ‘summus’인 회문이 되므로 유사회문이다.

* 여러분은 제시된 문자열을 분석하여 그것이 그 자체로 회문인지, 또는 한 문자를 삭제하면 회문이 되는 “유사회문”인지, 아니면 회문이나 유사회문도 아닌 일반 문자열인지를 판단해야 한다. 
* 만일 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력해야 한다. 
* 
* [알고리즘]
* 회문인지 먼저 판단한다. 판단하는 과정에 있어서 유사회문인지 판단한다.
* 유사회문을 판단할 때는 회문인지 판단하는 과정(맨 앞과 맨 뒤의 문자 비교반복)에서 문자가 다르면 그 문자를 떼어내었을 때, 즉 그 다음문자와 같은지 비교하여 판단한다
*/

#include<iostream>
#include<algorithm>
#include<vector>	

using namespace std;

bool isPal(string s) {
	for (int i = 0; i < (s.length() / 2); i++) {
		if (s[i] != s[s.length() - i - 1]) return false;
	}
	return true;
}

bool isSubpal(string s) {
	int left = 0, right = s.size() - 1;
	while (left < right) {
		if (s[left] != s[right])return false;
		left++; right--;
	}
	return true;
}

int type(string s) {
	if (isSubpal(s)) return 0;
	int left = 0, right = s.size() - 1;

	while (left < right) {
		if (s[left] != s[right]) {
			if (isPal(s.substr(0, left) + s.substr(left + 1))) return 1;
			if (isPal(s.substr(0, right) + s.substr(right+ 1))) return 1;
			return 2;
		}
		left++; right--;
	}
	return 2;
}

int main(void) {
	int testcase;
	cin >> testcase;
	for (int t = 0; t < testcase; t++) {
		string s; cin >> s;
		int res = type(s);
		cout << res << "\n";
	}

	return 0;
}