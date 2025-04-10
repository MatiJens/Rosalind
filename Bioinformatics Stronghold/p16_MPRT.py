from collections import defaultdict

import requests

with open("txt/rosalind_mprt.txt", "r") as f:
    sequences = {}
    id_list = []
    for i, txt_line in enumerate(f):
        protein = requests.get(f'http://www.uniprot.org/uniprot/{txt_line.strip().split("_")[0]}.fasta').text.splitlines()
        id_list.append(txt_line.strip())
        for line in protein:
            if line.startswith(">"):
                continue
            else:
                if id_list[i] not in sequences:
                    sequences[id_list[i]] = ""
                sequences[id_list[i]] += line

    def p16_MPRT(sequences : dict):
        motifs = defaultdict(str)
        for key, value in sequences.items():
            for i in range((len(value) - 3)):
                if (value[i] == "N") and (value[i + 1] != "P") and (value[i + 2] == "S" or value[i + 2] == "T") and (value[i + 3] != "P"):
                    motifs[key] += f"{(i + 1)} "
        return motifs

    result = p16_MPRT(sequences)

    for key, value in result.items():
        print(f"{key}\n{value}".strip())