def seek_orf(start_list, stop_list, minimum_amino_acid_length=7,
             longest_only=False):
    minumum_nucleotide_length = 3 * minimum_amino_acid_length
    region_list = []
    start_list.append(stop_list[-1])
    start = start_list.pop(0)
    stop = stop_list.pop(0)
    while(True):
        while(stop <= start):
            if len(stop_list):
                stop = stop_list.pop(0)
            else:
                return region_list
        if stop - start >= minumum_nucleotide_length:
            region_list.append((start, stop))
        if longest_only:
            while(start < stop):
                if len(start_list):
                    start = start_list.pop(0)
        else:
            if len(start_list):
                start = start_list.pop(0)
