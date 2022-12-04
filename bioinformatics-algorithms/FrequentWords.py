from PatternCount import PatternCount

#txt, k = "ACGTTGCATGTCGCATGATGCATGAGAGCT", 4

with open("dataset_2_13.txt", "r") as f:
    lines = f.readlines()
    txt, k = str(lines[0][:-1]), int(lines[1][:-1])


def FrequencyWords(txt, k):
    freq_words = []
    count_i = []
    for i in range(len(txt)-k):
        pattern = txt[i:i+k]
        count_i.append(PatternCount(txt, pattern))
    max_count_i = max(count_i)
    for i in range(len(txt)-k):
        if count_i[i] == max_count_i:
            freq_words.append(txt[i:i+k])
    return set(freq_words)

def BetterFrequencyWords(txt, k):
    freq_dict = {}
    for i in range(len(txt) - k):
        pattern = txt[i:i+k]
        if pattern in freq_dict.keys():
            freq_dict[pattern] += 1
        else:
            freq_dict[pattern] = 1
    return max(freq_dict, key= lambda x: freq_dict.get(x))

print(FrequencyWords(txt, k))
print(BetterFrequencyWords(txt, k))