import time


"""with open("E_coli.txt", "r") as f:
    lines = f.readlines()
    sequence = lines[0][:-1]
k, l, t = 9, 500, 3"""


sequence = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
k, l, t = 5, 50, 4

def CountKmers(seq, k):
    seq_dict = {}
    for i in range(len(seq)-k+1):
        pat = seq[i: i+k]
        if pat in seq_dict.keys():
            seq_dict[pat] += 1
        else:
            seq_dict[pat] = 1
    return seq_dict

def FindClumps(sequence, k, l, t):
    """
    :param sequence: a str for gene
    :param k: an int for k-mers
    :param l: an int for window length
    :param t: an int for the lowest required frequency value
    :return: all the k-mers forming (L-t) clumps
    """
    clumps = []
    for i in range(len(sequence)-l+1):
        freqs = CountKmers(sequence, k)
        for k_, v_ in freqs.items():
            if v_ >= t:
                clumps.append(k_)
    return list(set(clumps))



tic = time.time()
print(*FindClumps(sequence, k, l, t))
toc = time.time() - tic
print(f"Took {toc/60} mins.")