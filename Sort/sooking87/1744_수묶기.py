# 1744 수 묶기

# 입력 받은 수를 단 한 번 또는 0번 묶어서 최대 수 출력하기

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
nums = []
pos = []
neg = []
ans = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        pos.append(num)
    elif num == 1:
        ans += 1  # 1이 입력된다는 것은 1만 더하든,


nums.sort(reverse=True)
queue = deque(nums)
# print(queue)

num1 = queue.popleft()
while queue:
    num2 = queue.popleft()
    # print(num1, num2)
    # print(queue)
    temp1 = num1 * num2
    temp2 = num1 + num2
    if temp1 < temp2:
        ans += num1
        num1 = num2
    else:
        ans += temp1
        if queue:
            num1 = queue.popleft()
    print(ans)
print(ans)
