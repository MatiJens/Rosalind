with open("txt/rosalind_grph.txt", "r") as f:
    sequences = {}
    for line in f:
        if line[0] == '>':
            defline = line.strip()
            defline = defline.replace('>','')
        else:
            if defline not in sequences:
                sequences[defline] = ''
            sequences[defline] += line.strip()

    def p12_GRPH(sequences : dict):
        defline_pairs = []
        for defline_ext, data_ext in sequences.items():
            defline_actual = defline_ext
            suffix = data_ext[-3:]
            for defline_int, data_int in sequences.items():
                defline_last = defline_int
                if data_int[:3] == suffix:
                    if not defline_last == defline_actual:
                        defline_pairs.append(defline_actual)
                        defline_pairs.append(defline_last)
        return defline_pairs

    result = (p12_GRPH(sequences))
    for i in range(len(result)):
        if i % 2 == 1:
            print(result[i])
        elif i % 2 == 0:
            print(result[i], end = ' ')
