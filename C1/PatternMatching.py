#pattern = "ATAT"
#genome = "GATATATGCATATACTT"
"""
with open("dataset_3_5.txt") as f:
    lines = f.readlines()
    pattern = lines[0][:-1]
    genome = lines[1][:-1]
"""

with open("Vibrio_cholerae.txt") as f:
    lines = f.readlines()
    genome = lines[0][:-1]

pattern = "CTTGATCAT"

def PatternMatching(pattern, genome):
    n,m = len(genome), len(pattern)
    starts = []
    for i in range(n-m):
        windowed_gen = genome[i:i+m]
        if windowed_gen == pattern:
            starts.append(i)
    return starts

print(*PatternMatching(pattern, genome))

