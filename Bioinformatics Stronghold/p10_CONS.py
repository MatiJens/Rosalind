with open("txt/rosalind_cons.txt", "r") as f:
    sequences = []
    consensusString = ""
    i = -1

    for line in f:
        if line[0] == '>':
            i += 1
            sequences.append([])
        else:
            sequences[i] += line.strip()

    profile = [ ["A:"] + [0] * len(sequences[0]),
                ["C:"] + [0] * len(sequences[0]),
                ["G:"] + [0] * len(sequences[0]),
                ["T:"] + [0] * len(sequences[0])
                ]

    for row in sequences:
        for i, nucleotide in enumerate(row):
            if nucleotide == "A":
                profile[0][i+1] += 1
            elif nucleotide == "C":
                profile[1][i+1] += 1
            elif nucleotide == "G":
                profile[2][i+1] += 1
            else:
                profile[3][i+1] += 1

    for n in range(1, len(profile[0])):
        maxNucleotides = 0
        nucleotideType = ""
        for m in range(4):
            if profile[m][n] > maxNucleotides:
                maxNucleotides = profile[m][n]
                nucleotideType = profile[m][0]
        consensusString += nucleotideType[:1]

    print(consensusString)
    for y in range(4):
        for x in range (len(profile[0])):
            print(profile[y][x], end = " ")
        print()