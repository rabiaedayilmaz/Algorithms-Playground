file = "dataset_2_6.txt"
x ="TCATTGGTC"

with open(file, "r") as f:
    lines = f.readlines()

gene = lines[0][:-1]
pattern = lines[1][:-1]

def PatternCount(txt, pat):
    count = 0
    for idx in range(len(txt) - len(pat) + 1):
        if txt[idx:idx+len(pat)] == pat:
            count +=1
    return count

print(PatternCount(str(gene), str(pattern)))
