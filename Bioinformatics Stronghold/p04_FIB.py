with open ("txt/rosalind_fib.txt", "r") as f:
    data = f.read().split()
    months,newOffspring = int(data[0]), int(data[1])
    def p11_FIBD(months, newOffspring):
        if months == 0:
            return 0
        elif months == 1:
            return 1
        else:
            return p11_FIBD(months - 1, newOffspring) + newOffspring * p11_FIBD(months - 2, newOffspring)
    print(p11_FIBD(months,newOffspring))
