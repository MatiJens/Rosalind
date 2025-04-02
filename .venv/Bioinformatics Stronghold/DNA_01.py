def countNucleotide(DNA):
    if isinstance(DNA, str):
        nucleotides = [0, 0, 0, 0]
        for nucleotide in DNA:
            if nucleotide == 'A':
                nucleotides[0] += 1
                print("A")
            elif nucleotide == 'C':
                nucleotides[1] += 1
                print("C")
            elif nucleotide == 'G':
                nucleotides[2] += 1
                print("G")
            elif nucleotide == 'T':
                nucleotides[3] += 1
                print("T")
            else:
                continue
        print(nucleotides[0] + " " + nucleotides[1] + " " + nucleotides[2] + " " + nucleotides[3])
    else:
        TypeError("Argument should be str type")
