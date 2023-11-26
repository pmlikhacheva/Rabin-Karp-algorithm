def read_fasta(path):
    with open(path) as f:
        lines = f.readlines()
        sq_name = lines[0]
        sq = ''.join(lines[:1])
        return sq_name, sq

#print(read_fasta('/home/qrewetka/Rabin-Karp-algorithm/example.fa'))