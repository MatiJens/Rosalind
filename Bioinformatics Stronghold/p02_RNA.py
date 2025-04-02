with open("txt/rosalind_rna.txt", "r") as f:
    DNA = f.read()
    RNA = ''
    for nucleotide in DNA:
        if nucleotide == 'T':
            RNA += 'U'
        else:
            RNA += nucleotide
    print(RNA)
