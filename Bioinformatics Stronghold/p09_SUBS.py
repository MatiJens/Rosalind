with open("txt/rosalind_subs.txt", "r") as f:
    data = f.read().split()
    DNA, motif = data[0], data[1]
    positions = []
    for i in range (len(DNA)):
        if DNA[:len(motif)] == motif:
            print(i+1, end=" ")
        DNA = DNA[1:]