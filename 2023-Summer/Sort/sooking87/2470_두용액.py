# 2470 두 용액

# 합쳐서 0에 가까운 두 용액을 출력

import sys

input = sys.stdin.readline
n = int(input())
solution = [int(i) for i in input().split()]

solution.sort()
minus = 0
plus = len(solution) - 1
close_zero = abs(solution[minus] + solution[plus])
final = [solution[minus], solution[plus]]

while minus < plus:
    minus_val = solution[minus]
    plus_val = solution[plus]

    sum = minus_val + plus_val

    # - 용액과 + 용액의 합의 절대값이 기존보다 작다면 -> 값 update
    if close_zero > abs(sum):
        close_zero = abs(sum)
        final = [minus_val, plus_val]
        if sum == 0:
            break

    # - 용액을 기준으로 모든 + 용액을 검사하는게 아니라 정렬을 시켜놓은 것을 활용해서 두 용액의 합이 음수가 나오면 - 용액 인덱스를 하나 더하고, 두 용액의 합이 양수가 나오면 + 용액 인덱스를 하나 줄인다.
    if sum < 0:
        minus += 1
    else:
        plus -= 1

print(final[0], final[1])
