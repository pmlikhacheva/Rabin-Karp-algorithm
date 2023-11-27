def read_fasta(path):
    """
    reads data from fasta file

    :param path: path to fasta file with data
    :return: list with name of sequence and string with data
    """

    with open(path) as f:
        lines = f.readlines()
        sq_name = lines[0]
        sq = ''.join(''.join(lines[1:]).split())
        return sq_name, sq
