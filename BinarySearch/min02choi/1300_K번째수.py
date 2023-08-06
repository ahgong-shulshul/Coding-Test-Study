# 1300 K번째 수
# Gold2
# 이진탐색
# 풀이 날짜: 2023-08-01


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2
        

n = int(input())
k = int(input())

nums = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        nums.append(i * j)
print(nums)

nums.sort()

print(nums[k])