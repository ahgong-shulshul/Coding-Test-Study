# 22860 폴더 정리(small)

# 폴더 -> 1, 파일 -> 0으로 입력되고, 다음 입력된 경로의 파일의 종류의 개수와 파일의 총 개수(같은 파일이 여러 개 있을 경우 하나로 계산)

from anytree import Node, RenderTree

# 폴더의 총 개수 N, 파일의 총 개수 M
n, m = map(int, input().split())

# 와,, 어떻게 입력을 받아야되지?
# 트리 구조로 받고싶음.