with open("txt/rosalind_gc.txt", "r") as f:
    dnaFASTA = []
    dnaString = []
    dnaGC = []
    i = -1
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            i += 1
            dnaFASTA.append(line[1:])
            dnaString.append("")
            dnaGC.append(0)
        elif line.startswith("A") or line.startswith("T") or line.startswith("C") or line.startswith("G"):
            dnaString[i] += line
            dnaGC[i] = 100 * ((dnaString[i].count("C") + dnaString[i].count("G")) / len(dnaString[i]))
        else:
            continue
    maxGCIndex = dnaGC.index(max(dnaGC))
    print(dnaFASTA[maxGCIndex])
    print(round(max(dnaGC),6))




