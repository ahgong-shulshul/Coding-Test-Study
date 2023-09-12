n, t = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(t + 1)] for _ in range(n + 1)]

for _ in range(n):
    stuff.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, t + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])


total_cost = 0
for i in range(len(stuff)):
    total_cost += stuff[i][1]

print(total_cost - knapsack[n][t])