from itertools import zip_longest

with open("txt/rosalind_lcsm.txt", "r") as f:
    sequences = {}
    for line in f:
        if line.startswith(">"):
            defline = line.strip()
            defline = defline.replace(">", "")
        else:
            if not defline in sequences:
                sequences[defline] = ""
            sequences[defline] += line.strip()

    def p14_LCSM(sequences : dict):
        data = list(sequences.values())
        shortest = min(data, key=len)
        motifs = []
        for i in range(len(shortest)):
            for j in range(len(shortest)):
                motif = shortest[i:j + i + 1]
                if all(motif in seq for seq in data):
                    motifs.append(motif)
        return max(motifs, key=len)
    result = p14_LCSM(sequences)
    print(result)