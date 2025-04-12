aminoacids_DNA = {
    "TTT": "F", "TTC": "F",
    "TTA": "L", "TTG": "L",
    "CTA": "L", "CTG": "L", "CTT": "L", "CTC": "L",
    "ATT": "I", "ATC": "I", "ATA": "I",
    "ATG": "M",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TAT": "Y", "TAC": "Y",
    "CAT": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "AAT": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TGT": "C", "TGC": "C",
    "TGG": "W",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGT": "S", "AGC": "S",
    "AGA": "R", "AGG": "R",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

with open("txt/rosalind_orf.txt", "r") as f:

    DNA = ""
    for line in f:
        if line.startswith(">"):
            continue
        else:
            DNA += line.strip()

    def reverse(DNA):
        reverse_DNA = []
        for i in range(len(DNA)):
            if DNA[i] == 'A':
                reverse_DNA.insert(0, 'T')
            elif DNA[i] == 'T':
                reverse_DNA.insert(0, 'A')
            elif DNA[i] == 'C':
                reverse_DNA.insert(0, 'G')
            else:
                reverse_DNA.insert(0, 'C')
        return reverse_DNA

    def p18_ORF(DNA):
        orf = set()
        for _ in range(2):
            DNA = reverse(DNA)
            for i in range(0, len(DNA) - 2):
                protein = []
                codon_start = DNA[i] + DNA[i + 1] + DNA[i + 2]
                if codon_start == "ATG":
                    protein.append("M")
                    for j in range((i + 3), len(DNA) - 2, 3):
                        codon = DNA[j] + DNA[j + 1] + DNA[j + 2]
                        if codon in aminoacids_DNA:
                            protein.append(aminoacids_DNA[codon])
                        elif codon == "TAA" or codon == "TAG" or codon == "TGA":
                            orf.add(("".join(protein)))
                            break
        return orf

    result = p18_ORF(DNA)

    for protein in result:
        print(protein)
