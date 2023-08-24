# 20210 파일 탐색기
# Gold2
# String
# 풀이 날짜: 2023-08-24

# 일단 한번 정렬을 하고, 특정 인덱스를 하나 잡고 순회
# 해당 인덱스가 숫자인 친구들을 다 큐에 넣음(숫자가 나왔는데 그 다음 문자가 알파벳이면 뒤는 체크 안해도 됨.)(큐에 들어간 친구들은 다 정렬이 되어야만 함.)
# 큐에 들어온 단어들을 각각 순회해서 

# 큐에 들어갔다면 들어간 애들끼리 이 과정을 반복해야 함.(이미 서열이 정해진 거기 때문)

# 큐에 안들어간 친구들에서 이제 탐색(위의 과정을 반복)


# 뒤지게 어렵네

from collections import deque

"""

n = int(input())
words = [input() for _ in range(n)]

words.sort()
print(words)

queue = deque(words)
num_que = deque()


# idx = 0
# for i in range(len(words)):
#     # 숫자인 경우
#     print(words[i][idx])
#     if ('0' <= words[i][idx] <= '9'):
#         num_que.append(words[i])
#     if ('0' <= words[i][idx] <= '9' and i + 1 != len(words)):
#         if ('a' <= words[i + 1] <= 'z'):
#             break
# idx += 1

fix = []

idx = 0     # 이걸 모든 인덱스에 대해서 해야함
for i in range(len(queue)):
    # 숫자이면 숫자 큐에 넣어줌
    if ('0' <= words[i][idx] <= '9'):
        num_que.append(queue.popleft())
    # 알파벳이면 fix 큐에 넣어줌
    else:
        fix.append(queue[i])

    if (i + 1 == len(queue)):
        break
"""

#######################################################

n = int(input())

all_words = []

# 문자는 문자 하나로, 숫자는 붙여서 (일단은 문자 형태로) 저장
for _ in range(n):
    word = input()
    temp = []
    num = ""
    for i in range(len(word)):

        if ('A' <= word[i] <= 'z' and num != ""):
            temp.append(num)
            num = ""

        if ('A' <= word[i] <= 'z'):
            temp.append(word[i])
        else:
            num += word[i]

    if (num != ""):
        temp.append(num)
    all_words.append(temp)

print(all_words)
print()
all_words.sort()
for i in range(len(all_words)):
    print(all_words[i])

num_temp = []
idx = 0
next = []
while(True):
    # 특정 인덱스의 문자가 숫자인 단어 골라내기
    for i in range(all_words):
        if ('0' <= all_words[i][idx][0] <= '9'):
            num_temp.append(all_words[i])
        else:
            next.append()
    
    # 특정 인덱스에서 숫자로 걸린 애들 끼리 서열 정하기
    for j in range(len(num_temp)):
        num_temp.sort()
            

# 숫자 비교 만약 값이 똑같으면 길이가 긴게 우선순위가 낮음

    
