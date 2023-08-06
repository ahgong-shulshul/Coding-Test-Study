# 2805 나무 자르기
# Silver2
# 이진탐색
# 풀이 날짜: 2023-08-03

# 말도 안되는 숫자가 주어졌으면 이진탐색

n, m = map(int, input().split())
tree = [int(i) for i in input().split()]

tree.sort()

low = 1
high = tree[-1]
mid = 0

while(low <= high):
    mid = (low + high) // 2
    temp = 0
    for i in range(len(tree)):
        if (tree[i] - mid > 0):
            temp += tree[i] - mid
    if (temp < m):
        high = mid - 1
    else:
        low = mid + 1

print(high)