# 1744 수 묶기

# 입력 받은 수를 단 한 번 또는 0번 묶어서 최대 수 출력하기

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
nums = []
pos = []
neg = []
for _ in range(n):
    nums.append(int(input()))

nums.sort(reverse=True)
queue = deque(nums)
# print(queue)

ans = 0
num1 = queue[0]
while queue:
    num2 = queue[1]
    print(num1, num2)
    print(queue)
    temp1 = num1 * num2
    temp2 = num1 + num2
    if temp1 < temp2:
        ans += queue.popleft()
        num1 = num2
    else:
        pop_num1 = queue.popleft()
        pop_num2 = queue.popleft()
        print('after pop:', pop_num1, pop_num2)
        ans += pop_num1 * pop_num2
        if queue:
            num1 = queue.popleft()
    print(ans)
print(ans)
    


