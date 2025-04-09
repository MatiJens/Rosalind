from math import comb

with open("txt/rosalind_lia.txt", "r") as f:
    data = f.read().split()
    k, N = int(data[0]), int(data[1])

    def p15_LIA(k, N):
        population = pow(2,k)
        prob = 0
        for i in range(N, pow(2,k) + 1):
            prob += comb(population,i) * pow(0.25,i) * pow(1 - 0.25,population - i) # rozklad dwumianowy
        return prob

    result = p15_LIA(k, N)
    print(round(result, 3))
