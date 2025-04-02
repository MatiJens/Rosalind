with open("txt/rosalind_dna.txt", "r") as f:
    DNA = f.read()
    nucleotides = [0, 0, 0, 0]
    for nucleotide in DNA:
        if nucleotide == 'A':
            nucleotides[0] += 1
        elif nucleotide == 'C':
            nucleotides[1] += 1
        elif nucleotide == 'G':
            nucleotides[2] += 1
        elif nucleotide == 'T':
            nucleotides[3] += 1
        else:
            continue
    print(" ".join(map(str, nucleotides)))
