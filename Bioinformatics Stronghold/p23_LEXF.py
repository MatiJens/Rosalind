from itertools import product

with open("txt/rosalind_lexf.txt") as f:
    DNA = ""

    for line in f:
        if all(char.isalpha() for char in line.split()):
            DNA += line.strip().replace(" ", "")
        else:
           n = int(line.strip())

    comb = product(DNA, repeat = n)
    result = [''.join(t) for t in comb]
    for pair in result:
        print(pair)
