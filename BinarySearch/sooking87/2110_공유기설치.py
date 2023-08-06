# 2110 공유기 설치

# c개의 공유기를 n개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램 작성
import sys

input = sys.stdin.readline
n, c = map(int, input().split())
home = []
for _ in range(n):
    home.append(int(input()))
home.sort()
# 1 2 4 8 9

start = 1
end = max(home) - min(home)
isPossible = False

while start <= end:
    length = (start + end) // 2
    put = min(home) + length
    # 첫 번째 집과 마지막 집에 각각 한 개씩 두었다고 가정
    for i in range(c - 1):
        print('-')
