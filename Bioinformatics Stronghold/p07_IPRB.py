from math import comb

with open("txt/rosalind_iprb.txt", "r") as f:
    data = f.read().split()
    k,m,n = int(data[0]), int(data[1]), int(data[2])
    def p07_IPRB(k,m,n):
        kk = comb(k,2)
        mm = comb(m,2)
        nn = comb(n,2)
        km = k * m
        kn = k * n
        mn = m * n
        result = (kk + 0.75 * mm + km + kn + 0.5 * mn) / (kk + mm + km + kn + mn + nn)
        return round(result,5)
    print(p07_IPRB(k,m,n))