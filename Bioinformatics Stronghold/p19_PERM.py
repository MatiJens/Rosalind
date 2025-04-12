import math
from itertools import permutations
from math import factorial

with open ("txt/rosalind_perm.txt", "r") as f:
    data = f.read().split()
    n = int(data[0])
    comb = [i + 1 for i in range(n)]
    result = permutations(comb)

    print(factorial(n))
    for perm in result:
        print(" ".join(map(str, perm)))
