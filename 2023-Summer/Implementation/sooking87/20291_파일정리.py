# 20291 파일 정리

# 확장자의 이름과 확장자 파일의 개수를 출력 -> 확장자 이름의 사전순으로 출력

n = int(input())
files = []
# 입력값 중 확장자만 저장
for _ in range(n):
    files.append(input().split('.')[1])

organ = {}
# 확장자 기준 있으면 + 1, 없으면 1로 딕셔너리에 추가
for i in range(n):
    value = organ.get(files[i])

    if value == None:
        organ[files[i]] = 1
    else:
        organ[files[i]] += 1

[print(key, value) for (key, value) in sorted(organ.items())]