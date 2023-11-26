
p = 20

alphabet = {"A": 0, "C": 1, "G": 2, "T": 3}


def hashPoly(S):  # проблема с хэш-функцией

    h = sum(alphabet[S[c]]*(p**c) for c in range(len(S)))
    return h


def Rabin_Carp_Alg(DNA, target):
    """
    param DNA: initial sequence
    param target: substring
    return: list of indexes where the subsequence is
    """

    len_target = len(target)  # calculate length to simplify
    len_DNA = len(DNA)

    if len_target > len_DNA:
        raise Exception('Wrong target sequence')  # some exceptions
    
    if not isinstance(DNA, str) or not isinstance(target, str):
        raise TypeError("Wrong data type")

    if len(set(DNA)) > 4:  # if there are some symbols except ATGC
        raise ValueError("Wrong symbols in sequence")

    answer = []
    target_hash = hashPoly(target)

    for i in range(len_DNA - len_target + 1):
        subseq = DNA[i:i + len_target]  # part of DNA. it is moving in process from the begining to the end of sequense
        subseq_hash = hashPoly(subseq)  # hash of the part of DNA

        if subseq_hash == target_hash:
            equal = True
            for j in range(len_target):  # begin comparing symbol by symbol
                if subseq[j] != target[j]:
                    equal = False
                    break
            if equal:  # add to answer only if hashes are equal and subseqs are the same
                answer.append(i)

    return answer


DNA = 'ACGTAAACGT'
target = 'CGT'
print(Rabin_Carp_Alg(DNA, target))
