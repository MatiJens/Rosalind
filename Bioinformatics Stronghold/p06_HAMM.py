with open("txt/rosalind_hamm.txt", "r") as f:
    data = f.read().split()
    dnaA, dnaB = data[0], data[1]
    def p06_HAMM(dnaA, dnaB):
        dH = 0
        for charA, charB in zip(dnaA, dnaB):
            if charA != charB:
                dH += 1
        return dH
    print(p06_HAMM(dnaA, dnaB))

