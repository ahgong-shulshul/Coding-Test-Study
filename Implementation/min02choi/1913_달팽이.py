# 1913 달팽이
# Silver3
# Implementation 알고리즘
# 풀이 날짜: 2023-07-10

# 풀이 전략


n = int(input())
k = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

repet = 0
count = 1
dir = "u"
col, row = n // 2, n //2
till_cnt = -1

for num in range(1, n ** 2):
    board[col][row] = num
    till_cnt += 1

    # 자리 체인지
    if (till_cnt == count):
        # 모서리에 도달하였으므로 방향 전환
        if (dir == "u"):
            dir = "r"
        elif (dir == "r"):
            dir = "d"
        elif (dir == "d"):
            dir = "l"
        elif (dir == "l"):
            dir = "u"

        repet += 1

        if (repet == 2):
            count += 1
            repet = 0

        till_cnt = 0
    
    # 그 다음 자리로 이동
    if (dir == "u"):
        col -= 1
    elif (dir == "r"):
        row += 1
    elif (dir == "d"):
        col += 1
    elif (dir == "l"):
        row -= 1

board[0][0] = n**2

x, y = 0, 0

for i in range(n):
    for j in range(n):
        if (board[i][j] == k):
            x, y = i, j
        print(board[i][j], end=" ")
    print()
print(x + 1, y + 1)