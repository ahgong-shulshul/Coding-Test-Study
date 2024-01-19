# 14916 거스름돈

# 거스름돈 동전의 개수가 최소가 되도록 거슬러주기

coins = [5, 2]
money = int(input())
count = 0

while True:
    # 5원부터 거스름돈 구하기 -> 최소가 되기 위함
    if money % 5 == 0:
        count += money // 5
        money = 0
    # 거스를 수 없으면(음수) -> -1 출력
    # 거스를 수 있으면(0) -> count 출력
    if money < 0:
        print(-1)
        break
    elif money == 0:
        print(count)
        break
    # 5원을 못거스르면 2원씩 빼기
    money -= 2
    count += 1
