with open("txt/rosalind_subs.txt", "r") as f:
    data = f.read().split()
    DNA, motif = data[0], data[1]
    def p09_SUBS(DNA, motif):
        positions = []
        for i in range (len(DNA)):
            if DNA[:len(motif)] == motif:
                positions.append(i + 1)
            DNA = DNA[1:]
        return positions
    print (p09_SUBS(DNA, motif))