# 2805 나무 자르기

# 높이 h 지정 - > 모두 잘라 - > 필요한 만큼만 집으로 가져가려고 하는데, 이때 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
height = [int(i) for i in input().split()]

# 4 8
# 20 15 10 17

start = 1
end = max(height)

while start <= end:
    mid = (start + end) // 2
    # 얻은 나무의 길이 구하기
    # 나무가 자를 길이보다 짧다면 얻을 수 있는 길이가 없음.
    get = sum([(t - mid) if t - mid > 0 else 0 for t in height])

    # print(get, m, '자른 길이:', mid)
    if get >= m:
        start = mid + 1
        
    elif get < m:
        end = mid - 1

print(end)