with open("txt/rosalind_rna.txt", "r") as f:
    DNA = f.read()
    def p02_RNA(DNA):
        RNA = ''
        for nucleotide in DNA:
            if nucleotide == 'T':
                RNA += 'U'
            else:
                RNA += nucleotide
        return RNA
    print(p02_RNA(DNA))