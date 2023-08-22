# 1764 듣보잡
# Silver4
# String (이분탐색 알고리즘 사용)
# 풀이 날짜: 2023-08-22


n, m = map(int, input().split())

dut = [input() for _ in range(n)]
bo = [input() for _ in range(m)]
dut.sort()
bo.sort()

answer = []

# bo를 배경으로 깔음    
for name in dut:
    low = 0
    high = len(bo) - 1
    while (low <= high):
        mid = (low + high) // 2

        if (name == bo[mid]):
            answer.append(name)
            break
        if (name < bo[mid]):
            high = mid - 1
        if (name > bo[mid]):
            low = mid + 1

print(len(answer))
for i in answer:
    print(i)
