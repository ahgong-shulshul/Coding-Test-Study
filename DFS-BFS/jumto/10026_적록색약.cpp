/*
* [���� 1987] ���ĺ�
* ���� Rĭ, ���� Cĭ���� �� ǥ ����� ���尡 �ִ�. ������ �� ĭ���� �빮�� ���ĺ��� �ϳ��� ���� �ְ�, 
* ���� ��� ĭ (1�� 1��) ���� ���� ���� �ִ�.

* ���� �����¿�� ������ �� ĭ ���� �� ĭ���� �̵��� �� �ִµ�, 
* ���� �̵��� ĭ�� ���� �ִ� ���ĺ��� ���ݱ��� ������ ��� ĭ�� ���� �ִ� ���ĺ����� �޶�� �Ѵ�. 
* ��, ���� ���ĺ��� ���� ĭ�� �� �� ���� �� ����.

* ���� ��ܿ��� �����ؼ�, ���� �ִ��� �� ĭ�� ���� �� �ִ����� ���ϴ� ���α׷��� �ۼ��Ͻÿ�. 
* ���� ������ ĭ�� ���� ����� ĭ�� ���Եȴ�.

* [�˰���]
* ���� �켱 Ž��, �ʺ� �켱 Ž��
*
* 
*/

#include<iostream>
#include<algorithm>
#include<vector>	
#include<stack>
#include<queue>

using namespace std;

#define MAX 100

int N;
char graph1[MAX][MAX];
char graph2[MAX][MAX];
int res1 = 0, res2 = 0;
char current;

bool dfs(int x, int y) {
	if (x >= N || x < 0 || y < 0 || y >= N)return false;
	if (graph1[x][y] == current) {
		graph1[x][y] = 'X';
		dfs(x + 1, y);
		dfs(x - 1, y);
		dfs(x, y - 1);
		dfs(x, y + 1);
		return true;
	}
	return false;
}

bool dfs2(int x, int y) {
	if (x >= N || x < 0 || y < 0 || y >= N)return false;
	if (graph2[x][y] == current) {
		graph2[x][y] = 'X';
		dfs2(x + 1, y);
		dfs2(x - 1, y);
		dfs2(x, y - 1);
		dfs2(x, y + 1);
		return true;
	}
	return false;
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	for (int i = 0; i < N; i++) {
		string tmp; cin >> tmp;
		for (int j = 0; j < N; j++) {
			graph1[i][j] = tmp[j];
			graph2[i][j] = tmp[j];
		}
	}


	// ���ϻ��� x
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (graph1[i][j] != 'X') current = graph1[i][j];
			else continue;
			if (dfs(i, j)) res1++;
		}
	}

	// ���ϻ��� o 
	// R�� G�� �ٲٰ� �ٽ� dfs�� Ž��
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (graph2[i][j] == 'R') graph2[i][j] = 'G';
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (graph2[i][j] != 'X') current = graph2[i][j];
			else continue;
			if (dfs2(i, j)) res2++;
		}
	}

	cout << res1 << " " << res2;

	return 0;
}