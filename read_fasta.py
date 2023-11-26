def read_fasta(path):
    with open (path) as f:
        sq_name = ''
        sq = ''
        lines = f.readlines()
        sq_name = lines[0]
        for line in lines[1:]:
            sq += line
        l = []
        l.append(sq_name)
        l.append(sq)
        return l

#print(read_fasta('/home/qrewetka/Rabin-Karp-algorithm/example.fa'))