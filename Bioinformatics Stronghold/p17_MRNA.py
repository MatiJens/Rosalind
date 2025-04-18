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

with open("txt/rosalind_mrna.txt", "r") as f:
    protein = f.read().strip()
    def p17_MRNA(protein : str):
        mRNA_count = 1
        for aminoacid in protein[1:]:
            mRNA_count *= (sum(1 for codon in aminoacids if aminoacids[codon] == aminoacid))
            #print(sum(1 for codon in aminoacids if aminoacids[codon] == aminoacid))
            if mRNA_count >= 1000000:
                print("odej")
                print(mRNA_count)
                mRNA_count = (mRNA_count % 1000000)
                print(mRNA_count)
        mRNA_count = (mRNA_count * 3) % 1000000
        return mRNA_count

    result = p17_MRNA(protein)
    print(result)