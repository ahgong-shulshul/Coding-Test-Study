# 20444 색종이와 가위

# n번의 가위질로 k개의 색종이 조각을 만들 수 있다면 YES, 아니라면 NO를 출력

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
# 1번 자름 -> 2개
# 2번 자름 -> 4개
# 3번 자름 -> 6개
# 4번 자름 -> 9개 / 8개
start = 0
end = n // 2
isPossible = False

# 가위질을 가로로 자른 횟수와 세로로 자른 횟수로 나뉨
# = 조각 개수는 (row_cut + 1) * (col_cut + 1)

# 거기에다가 row_cut과 col_cut은 대칭적이기 때문에 row_cut 기준으로 n // 2만큼 확인하면 됨
while start <= end:
    row_cut = (start + end) // 2  # mid라는게 가로로 자르는 횟수로 봄
    col_cut = n - row_cut

    pieces = (row_cut + 1) * (col_cut + 1)
    if k == pieces:
        print('YES')
        isPossible = True
        break
    if k > pieces:
        start = row_cut + 1
    else:
        end = row_cut - 1
    print(row_cut, col_cut)

if not isPossible:
    print('NO')
