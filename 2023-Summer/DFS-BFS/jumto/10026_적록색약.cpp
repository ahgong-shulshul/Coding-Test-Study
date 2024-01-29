/*
* [백준 1987] 알파벳
* 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 
* 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

* 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 
* 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 
* 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

* 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 
* 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

* [알고리즘]
* 깊이 우선 탐색, 너비 우선 탐색
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


	// 적록색약 x
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (graph1[i][j] != 'X') current = graph1[i][j];
			else continue;
			if (dfs(i, j)) res1++;
		}
	}

	// 적록색약 o 
	// R을 G로 바꾸고 다시 dfs로 탐색
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