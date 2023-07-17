import itertools as it

str = '1234'
li = ['a', 'b', 'c']

pro_str = it.product(str, repeat=3)
pro_li = it.product(li, repeat=2)
print('product:', list(pro_str))
print('product:', list(pro_li))

per_str = it.permutations(str, 2)
per_li = it.permutations(li, 2)
print('permytation:', list(per_str))
print('permutation:', list(per_li))

com_str = it.combinations(str, 2)
com_li = it.combinations(li, 2)
print('combinations:', list(com_str))
print('combinations:', list(com_li))