with open("txt/rosalind_iev.txt", "r") as f:
    data = f.read().split()

    def p13_IEV(data):
        dominant_offspring = float(data[0]) * 2 + float(data[1]) * 2 + float(data[2]) * 2 + float(data[3]) * 1.5 + float(data[4])
        return dominant_offspring
    result = p13_IEV(data)
    print(result)