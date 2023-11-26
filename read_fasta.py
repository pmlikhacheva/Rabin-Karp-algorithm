def read_fasta(file_path):
    """
    :param file_path: path to fasta file with data
    :return: XZ
    """

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
