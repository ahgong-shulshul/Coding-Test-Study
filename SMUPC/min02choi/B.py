# 각 줄마다 가능한 경우 반환
def seat_available(horizon, n):
    temp = "0" * n
    cnt = 0
    for i in range(0, len(horizon) - n + 1):
        if (horizon[i:i + n] == temp):
            cnt += 1
    return cnt

row, col, n = map(int, input().split())

count = 0
for i in range(row):
    hor = input()
    count += (seat_available(hor, n))

print(count)
