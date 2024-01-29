# 9465 스티커

# 점수 합이 최대가 되게 스티커를 떼어내려고 한다. 변을 공유하게 된다면 떼어낼 수 없다.

import sys

n = int(input())
for i in range(n):
    m = int(input())
    value = [[int(i) for i in range(m)] for _ in range(2)]
