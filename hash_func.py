BASE = 20

alphabet = {"A": 1, "C": 2, "G": 3, "T": 4}


def calc_hash(s):
    res = alphabet[s[0]]
    for i in range(1, len(s)):
        res = res * BASE + alphabet[s[i]]
    return res


def next_hash(S, prev, h):
    res = (h - alphabet[prev]*BASE**(len(S)-1))*BASE + alphabet[S[-1]]
    return res
