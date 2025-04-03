aminoacids = {
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I",
    "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y",
    "CAU": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C",
    "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGU": "S", "AGC": "S",
    "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

with open("txt/rosalind_prot.txt", "r") as f:
    mRNA = f.read()
    def translation(mRNA):
        protein = ""
        for i in range(len(mRNA) - 2):
            startCodon = mRNA[i] + mRNA[i + 1] + mRNA[i + 2]
            if startCodon == "AUG":
                for j in range(i,len(mRNA) - 2, 3):
                    codon = mRNA[j] + mRNA[j + 1] + mRNA[j + 2]
                    if codon in aminoacids:
                        protein += aminoacids[codon]
                    elif codon == "UAA" or codon == "UAG" or codon == "UGA":
                        return protein
                    if j == (len(mRNA) - 3):
                        return "no stop codon"
            return "no start codon"
    print(translation(mRNA))



