
p = 20

alphabet = {"A": 0, "C": 1, "G": 2, "T": 3}


def calc_hash(s): 
    res = alphabet[s[0]]
    for i in range(1, len(s)):
        res = res * p + alphabet[s[i]]
    return res

def next_hash(S, h):
    res = (h - alphabet[S[0]]*p**(len(S)-2))*p + alphabet[S[-1]]
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

    answer = []
    target_hash = hashPoly(target)  # is constant

    for i in range(len_DNA - len_target + 1):
        subseq = DNA[i:i + len_target]
        subseq_hash = hashPoly(subseq)

        print(i)
        print(subseq_hash)
        print(target_hash)
        print(DNA[i:i + len_target])
        print(target)

        if subseq_hash == target_hash:
            equal = True
            for j in range(len_target):
                if subseq[j] != target[j]:
                    equal = False
                    break
            if equal:
                answer.append(i)

    return answer


DNA = 'ACGTAAACGT'
target = 'CGT'
print(Rabin_Carp_Alg(DNA, target))
