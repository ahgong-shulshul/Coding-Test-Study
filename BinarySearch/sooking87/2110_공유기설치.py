# 2110 공유기 설치

# c개의 공유기를 n개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램 작성
import sys

input = sys.stdin.readline
n, c = map(int, input().split())
home = []
for _ in range(n):
    home.append(int(input()))

# 1 2 4 8 9
pos = [0 for _ in range(max(home) + 1)]
for i in range(n):
    pos[home[i]] = 1
print(pos)
start = 1
end = max(home)
while start <= end:
    length = (start + end) // 2
    # 첫 번째 집과 마지막 집에 각각 한 개씩 두었다고 가정
    put = min(home) + length
