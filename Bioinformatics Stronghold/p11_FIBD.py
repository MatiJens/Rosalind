with open("txt/rosalind_fibd.txt", "r") as f:
    data = f.read().split()
    months, lifetime = (int(data[0])), int(data[1])
    def p11_FIBD(months, lifetime):
        rabbits = [0] * (lifetime)
        rabbits[0] = 1
        for i in range(months - 1):
            rabbits = [sum(rabbits[1:lifetime])] + rabbits[:-1]
        return sum(rabbits)
    print(p11_FIBD(months,lifetime))
