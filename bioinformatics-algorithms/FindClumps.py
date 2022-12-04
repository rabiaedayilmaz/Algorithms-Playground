import time


with open("E_coli.txt", "r") as f:
    lines = f.readlines()
    sequence = lines[0][:-1]
k, l, t = 9, 500, 3


"""sequence = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
k, l, t = 5, 50, 4"""

def CountKmers(seq, k):
    seq_dict = {}
    for i in range(len(seq)-k+1):
        pat = seq[i: i+k]
        if pat in seq_dict.keys():
            seq_dict[pat] += 1
        else:
            seq_dict[pat] = 1
    return seq_dict

def IndicesKmers(seq, k):
    seq_dict = {}
    for i in range(len(seq)-k+1):
        pat = seq[i: i+k]
        if pat in seq_dict.keys():
            seq_dict[pat].append(i)
        else:
            seq_dict[pat] = [i]
    return seq_dict

def FindClumps(sequence, k, l, t):
    """
    Parameters:
        sequence: a string the genome expression
        k: an int desired k-mer size
        l: an int window size
        t: an int clump size
    Returns:
        a list of k-mer clumps of genome
    """
    clumps = []
    for i in range(len(sequence)-l+1):
        freqs = CountKmers(sequence, k)
        for k_, v_ in freqs.items():
            if v_ >= t:
                clumps.append(k_)
    return list(set(clumps))

def BetterFindClumps(s, k, l, t):
    """
        Parameters:
            s: a string the genome expression
            k: an int desired k-mer size
            l: an int window size
            t: an int clump size
        Returns:
            a list of k-mer clumps of genome
        """

    from collections import defaultdict
    # init vars for result and start indices of kmers
    res = set()
    indices = defaultdict(list)
    for i in range(len(s) - k + 1):
        # get the k-mer by windowing genome expression
        kterm = s[i: i+k]
        # while k-mer genome exists in dict
        # delete k-mers if:
        # length of overlapping k-mer length windowed genome sequences is larger than window size
        while indices[kterm] and i+k-indices[kterm][0] > l:
            indices[kterm].pop(0)
        # save the start indices of k-mers
        indices[kterm].append(i)
        # select the k-mers that has amount of start indices equals t-clump size
        if len(indices[kterm]) == t:
            res.add(kterm)
    return res


tic = time.time()
#print(*FindClumps(sequence, k, l, t))
print(len(BetterFindClumps(sequence, k, l, t)))
toc = time.time() - tic
print(f"Took {toc/60} mins.")