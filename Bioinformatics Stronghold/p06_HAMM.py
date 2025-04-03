with open("txt/rosalind_hamm.txt", "r") as f:
    data = f.read().split()
    dnaA, dnaB = data[0], data[1]
    dH = 0
    for charA, charB in zip(dnaA, dnaB):
        if charA != charB:
            dH += 1
    print(dH)

