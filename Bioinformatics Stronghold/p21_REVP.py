with open("txt/rosalind_revp.txt", "r") as f:
    data = f.read().split()
    DNA = ""

    for line in data:
        if line.startswith(">"):
            continue
        else:
            DNA += line

    def rev(DNA):
        rev_DNA = ""
        for nucleotide in DNA:
            if nucleotide == "A":
                rev_DNA += "T"
            elif nucleotide == "T":
                rev_DNA += "A"
            elif nucleotide == "C":
                rev_DNA += "G"
            elif nucleotide == "G":
                rev_DNA += "C"
        rev_DNA = rev_DNA[::-1]
        return rev_DNA

    for j in range(4, 13):
        for i in range(len(DNA) - j + 1):
            dna_temp = DNA[i:i+j]
            if dna_temp == rev(dna_temp):
                print(i + 1, j)

