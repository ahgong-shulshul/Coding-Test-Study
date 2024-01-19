# 17609 회문
# Gold5
# String
# 풀이 날짜: 2023-08-23

# 회문이면 1 리턴, 회문이 아니면 0리턴
def is_palindrome(text):
    for i in range(len(text) // 2):

        # 유사회문인지 탐색
        if (text[i] != text[-i -1]):

            flag = 0    # 0이면 유사회문이 아님
            # 일단 해당 인덱스번째 제거
            temp1 = text
            temp1 = list(temp1)
            temp1[i] = ""
            temp1 = "".join(temp1)

            temp2 = text
            temp2 = list(temp2)
            temp2[-i -1] = ""
            temp2 = "".join(temp2)

            # 뺀 문자가 회문인가?
            for j in range(i, len(temp1) // 2 + 1):
                if (temp1[j] != temp1[-j -1]):
                    break
                if (j == len(temp1) // 2):
                    flag = 1

            if (flag == 0):
                for j in range(i, len(temp2) // 2 + 1):
                    if (temp2[j] != temp2[-j -1]):
                        break
                    if (j == len(temp2) // 2):
                        flag = 1
            
            if (flag == 1):
                return 1
            else:
                return 2

    return 0


n = int(input())

for i in range(n):
    text = input()
    print(is_palindrome(text))
