with open("txt/rosalind_revc.txt", "r") as f:
    DNA = f.read()
    def p03_REVC(DNA):
        rDNA = ''
        for nucleotide in DNA:
            if nucleotide == "A":
                rDNA = "T" + rDNA
            elif nucleotide == "T":
                rDNA = "A" + rDNA
            elif nucleotide == "C":
                rDNA = "G" + rDNA
            elif nucleotide == "G":
                rDNA = "C" + rDNA
            else:
                continue
        return rDNA
    print(p03_REVC(DNA))