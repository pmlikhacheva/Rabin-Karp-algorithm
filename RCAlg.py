
p = 20

alphabet = {"A": 0, "C": 1, "G": 2, "T": 3}

def read_fasta(file_path):
    sequences = {}
    with open(file_path) as f:
        seq_name = None
        seq = ''
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if seq_name is not None:
                    sequences[seq_name] = seq
                seq_name = line[1:]
                seq = ''
            else:
                seq += line
        if seq_name is not None:
            sequences[seq_name] = seq
    return sequences

def hashPoly(S): #проблема с хэш-функцией
    
    h = sum(alphabet[S[c]]*(p**c) for c in range(len(S)))
    return h
    
def Rabin_Carp_Alg(DNA,target):
    if len(target) > len(DNA):
        raise Exception('Wrong target sequence')
    
    if not isinstance(DNA, str) or not isinstance(target, str):
        raise TypeError("Wrong data type")
    
    answer = []
    DNA_hash = hashPoly(DNA[:len(target)])
    target_hash = hashPoly(target) #const

    for i in range(len(DNA)-len(target)+1):
        print(i)
        print(DNA_hash)
        print(target_hash)
        print(DNA[i:i+len(target)])
        print(target)
        if DNA_hash == target_hash and DNA[i:i+len(target)] == target:
            answer.append(i)
        #DNA_hash = hashPoly(DNA[i+1:i+1+len(target)])
        DNA_hash = (DNA_hash - pow(p,len(target))*alphabet[DNA[i]])/p + alphabet[DNA[i+len(target)]]

    return answer

DNA = 'ACGTAAACGT'
target = 'CGT'
print(Rabin_Carp_Alg(DNA, target))
