# 10994 별찍기-19
# Silver4
# Implementation 알고리즘
# 풀이 날짜: 2023-07-10


n = int(input())
k = 1 + (n - 1) * 4

board = [[" " for _ in range(k)] for _ in range(k)]


low = 0
top = k
while (low != top - 1):
    for i in range(low, top):
        for j in range(low, top):
            if (i == low or i == top - 1 or j == low or j == top - 1):
                board[i][j] = "*"
    low += 2
    top -= 2

board[n * 2 - 2][n * 2 - 2] = "*"

for i in range(k):
    for j in range(k):
        print(board[i][j], end="")
    print()