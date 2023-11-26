
p = 20

alphabet = {"A": 1, "C": 2, "G": 3, "T": 4}


def calc_hash(s):
    res = alphabet[s[0]]
    for i in range(1, len(s)):
        res = res * p + alphabet[s[i]]
    return res


def next_hash(S, prev, h):
    res = (h - alphabet[prev]*p**(len(S)-1))*p + alphabet[S[-1]]
    return res


def Rabin_Carp_Alg(DNA, target):
    """
    param DNA: initial sequence
    param target: substring
    return: list of indexes where the subsequence is
    """

    len_target = len(target)
    len_DNA = len(DNA)

    if len_target > len_DNA:
        raise Exception('Wrong target sequence')
    
    if not isinstance(DNA, str) or not isinstance(target, str):
        raise TypeError("Wrong data type")

    if len(set(DNA)) > 4:  # if there are some symbols except ATGC
        raise ValueError("Wrong symbols in sequence")

    answer = []
    target_hash = calc_hash(target)
    subseq = DNA[:len_target]   # part of DNA. it is moving in process from the begining to the end of sequense
    subseq_hash = calc_hash(subseq)  # hash of the part of DNA

    for i in range(len_DNA - len_target + 1):
        if subseq_hash == target_hash:
            equal = True
            for j in range(len_target):
                if subseq[j] != target[j]:
                    equal = False
                    break
            if equal:
                answer.append(i)

        subseq = DNA[i + 1:i + len_target + 1]
        subseq_hash = next_hash(subseq, DNA[i], subseq_hash)
    return answer


DNA = 'ACGTAAACGT'
target = 'CGT'
print(Rabin_Carp_Alg(DNA, target))
