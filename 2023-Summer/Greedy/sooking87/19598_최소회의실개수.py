# 19598 최소 회의실 개수

# N개의 회의를 모두 진행할 수 있는 최소 회의실 개수

import sys
import heapq

input = sys.stdin.readline
n = int(input())
meetings = []
for _ in range(n):
    temp = [int(i) for i in input().split()]
    meetings.append(temp)

meetings.sort()
heap = []
heapq.heappush(heap, meetings[0][1])

for i in range(1, n):
    if meetings[i][0] < heap[0]:
        heapq.heappush(heap, meetings[i][1])
    if meetings[i][0] >= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, meetings[i][1])

print(len(heap))