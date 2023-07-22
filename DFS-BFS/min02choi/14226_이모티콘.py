# 14226 이모티콘
# Gold4
# BFS(너비 우선 탐색) 알고리즘
# 풀이 날짜: 2023-07-22


# 풀이 전략
# 화면의 이모티콘 수, 클립보드의 이모티콘 수, 시간

from collections import deque


s = int(input())

visited = [[False] * 1000 for i in range(1000)]

status = deque()
status.append([1, 0, 0])

while(status):
    cur = status.popleft()
    emoji = cur[0]
    clip = cur[1]
    time = cur[2]

    if (emoji == s):
        print(time)
        break
    
    if (emoji > 0):
        # 복사
        if (visited[emoji][emoji] == False):
            visited[emoji][emoji] = True
            status.append([emoji, emoji, time + 1])

        # 삭제
        if (visited[emoji - 1][clip] == False):
            visited[emoji - 1][clip] = True
            status.append([emoji - 1, clip, time + 1])
        
    # 붙여넣기
    if (clip > 0):
        if (visited[emoji + clip][clip] == False):
            visited[emoji + clip][clip] = True
            status.append([emoji + clip, clip, time + 1])

