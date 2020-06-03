def retrieve_triplet_position(sequence, triplet):
    """
    Return list of the triplet in the sequence
    sequence: nucleotide sequence
    triplet: any combination of the 3 characters of the nucleotide
    return: list of the start position of the triplet
    """
    if len(triplet) != 3:
        raise ValueError("Triplet should consist of three letters.")
    start_pos = 0
    triplet_list = []
    while(start_pos < len(sequence)):
        position = sequence.find(triplet, start_pos)
        if position < 0:
            break
        triplet_list.append(position)
        start_pos = position + 3
    return triplet_list
