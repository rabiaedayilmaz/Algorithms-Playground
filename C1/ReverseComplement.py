#dna = "AAAACCCGGT"

with open("dataset_3_2.txt", "r") as f:
    lines = f.readlines()
    dna = (next(iter(lines)))[:-1]


def ReverseComplement(dna):
    n = len(dna)
    complements = {"A": "T",
                   "G": "C",
                   "T": "A",
                   "C": "G"}
    reversed_complement = n * [None]
    for i in range(n):
        gene = dna[i]
        reversed_complement[i] = complements[gene]
    return "".join(reversed_complement[::-1])

reversed_complement = ReverseComplement(dna)

print(reversed_complement)