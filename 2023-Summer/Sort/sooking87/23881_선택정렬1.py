# 23881 알고리즘 수업-선택 정렬 1

# N, K를 입력받고, K번째 바뀐 숫자를 출력
import sys

def selection(arr):
    global count, answer
    for i in range(n - 1, 0, -1):
        max_idx = i
        for j in range(i - 1, -1, -1):
            if arr[max_idx] < arr[j]:
                max_idx = j

        if i != max_idx:
            if count == k:
                answer = f'{arr[i]} {arr[max_idx]}'
                break
            arr[max_idx], arr[i] = arr[i], arr[max_idx]
            count += 1
    return answer

input = sys.stdin.readline
n, k = map(int, input().split())
arr = [int(i) for i in input().split()]
answer = -1
count = 1

print(selection(arr))
