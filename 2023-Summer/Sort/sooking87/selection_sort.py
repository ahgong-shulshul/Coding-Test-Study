n = int(input())
nums = [int(i) for i in input().split()]

for i in range(0, n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if nums[min_idx] > nums[j]:
            min_idx = j

    nums[i], nums[min_idx] = nums[min_idx], nums[i]
print(nums)