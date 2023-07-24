# 14226 이모티콘
# Gold4
# BFS(너비 우선 탐색) 알고리즘
# 풀이 날짜: 2023-07-22


# 풀이 전략
# 화면의 이모티콘 수, 클립보드의 이모티콘 수, 시간

from collections import deque


s = int(input())
visited = [[False for _ in range(2001)] for _ in range(2001)]

status = deque()
status.append([1, 0, 0])

while(status):
    emoji, clip, time = status.popleft()

    if (emoji == s):
        print(time)
        break
    
    if (0 < emoji <= 1000):
        # 복사
        if (visited[emoji][emoji] == False):
            visited[emoji][emoji] = True
            status.append([emoji, emoji, time + 1])
        # 삭제
        if (visited[emoji - 1][clip] == False):
            visited[emoji - 1][clip] = True
            status.append([emoji - 1, clip, time + 1])
        
    # 붙여넣기
    if (0 < clip <= 1000 and 0 < emoji + clip <= 2000):
        if (visited[emoji + clip][clip] == False):
            visited[emoji + clip][clip] = True
            status.append([emoji + clip, clip, time + 1])
