# 24051 알고리즘 수업-삽입 정렬 1

import sys


def insertion_sort(arr):
    global cnt, k
    for i in range(1, len(arr)):
        key = arr[i]
        compare_idx = i - 1

        while compare_idx >= 0 and arr[compare_idx] > key:
            arr[compare_idx + 1] = arr[compare_idx]
            compare_idx -= 1
            cnt += 1
            if k == cnt:
                return arr[compare_idx + 1]

        if compare_idx + 1 != i:
            arr[compare_idx + 1] = key
            cnt += 1
            if k == cnt:
                return arr[compare_idx + 1]

    return -1


input = sys.stdin.readline
n, k = map(int, input().split())
nums = [int(i) for i in input().split()]
cnt = 0
print(insertion_sort(nums))
