# 1431 시리얼 번호
# Silver3
# 정렬 알고리즘
# 풀이 날짜: 2023-07-29


# from collections import deque

n = int(input())
serial = []
for i in range(n):           
    serial.append(input())

idx = 0
change = 0
serial.sort(key=len)

while (len(serial) > 0):
    temp = []
    temp.append(serial[idx])

    # 길이가 다르면 temp안에 있던 것 처리
    if (len(serial[idx]) != len(serial[idx + 1])):
        num_dic = {}
        for sri in temp:
            nums = 0
            for word in sri:
                if (48 <= ord(word) <= 57):
                    nums += int(word)

        ########################################################
        # 딕셔너리에 넣는 과정이 잘못된거같긴하다. 왜 튜플로?
            if nums in num_dic:
                num_dic[nums].append(sri)
            else:
                num_dic[nums] = list(sri)

        # 딕셔너리의 각 key에 대해서(숫자의 합이 동일한 serial번호에 대해서) 딕셔너리 순으로 정렬
        num_dic = sorted(num_dic.items())   # 키 값으로 정렬
        print(num_dic)
        
        ########################################################

        # 딕셔너리 내부 정렬?
        # key 값으로 정렬 하고 그 뒤에 각 key마다 정렬을 수행해야 함
        for k in range(len(num_dic)):
            print(num_dic[k])
            num_dic[k].index(1).sort()

        ########################################################

        # 딕셔너리에 저장된 순서대로 출력
        for k in range(len(num_dic)):
            for j in num_dic.values():
                print(j)

        del serial[0:idx]
        idx = 0
    idx += 1

