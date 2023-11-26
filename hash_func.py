BASE = 20

alphabet = {
    "A": 1, "C": 2, "G": 3, "T": 4
}


def calc_hash(s):
    """
    calculates hash
    :param s: string with ATGC elements
    :return: number as a hash
    """

    res = alphabet[s[0]]
    for i in range(1, len(s)):
        res = res * BASE + alphabet[s[i]]

    return res


def next_hash(s, prev, h):
    """
    recalculates hash of next subsequence basing on hash of current subsequence
    :param s: next subsequence
    :param prev: first symbol of previous subsequence
    :param h: previous hash
    :return: recalculates hash
    """

    res = (h - alphabet[prev]*BASE**(len(s)-1))*BASE + alphabet[s[-1]]

    return res
