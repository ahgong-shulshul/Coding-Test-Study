# 1377 버블 소트
# Gold2
# 정렬 알고리즘
# 풀이 날짜: 2023-07-26

# 다른 풀이방법을 생각해봐야 할듯...

n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))

std = sorted(A)
flag = 0
cnt = 0
while(flag == 0 and len(std) != 0):
    num = std.pop()
    # 가장 큰 원소 제거
    for i in range(len(A)):
        if (A[i] == num):
            del A[i]
            # cnt += 1
            break
    # cnt += 1
    for i in range(len(A) - 1):
        front = A[i]
        back = A[i + 1]
        if (back < front):  # 정렬이 안됨
            break
        elif (i == len(A) - 2):
            flag = 1
        if (i == len(A) - 2):
            cnt += 1


print(cnt + 1)

"""
n = int(input())
A = []
A.append("")
for _ in range(n):
    A.append(int(input()))

changed = False
for i in range(1, n + 1):
    changed = False
    for j in range(1, n-i+1):
        if (A[j] > A[j + 1]):
            changed = True
            A[j], A[j + 1] = A[j + 1], A[j]

    if (changed == False):
        print(i)
        break
"""
        

"""
10 1 5 2 3
1 5 2 3 10
1 2 3 5 10

"""