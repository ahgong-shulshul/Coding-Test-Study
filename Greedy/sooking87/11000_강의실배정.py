# 11000 강의실 배정

# 강의실을 최소로 개설할 수 있는 강의실 수 구하기
import heapq
import sys

# 입력받기
input = sys.stdin.readline  # 얘의 용도?
n = int(input())
classes = []
for _ in range(n):
    temp = list(map(int, input().split()))
    classes.append(temp)

# 정렬순: S -> T 즉, S순으로 정렬 후 수업 진행 시간이 작은 순대로 정렬됨
classes.sort()
heap = []
heapq.heappush(heap, classes[0][1])  # 첫 번째 강의가 끝나는 시간을 넣음

for i in range(1, n):
    if heap[0] > classes[i][0]:
        heapq.heappush(heap, classes[i][1])
    if heap[0] <= classes[i][0]:
        heapq.heappop(heap)
        heapq.heappush(heap, classes[i][1])
print(len(heap))