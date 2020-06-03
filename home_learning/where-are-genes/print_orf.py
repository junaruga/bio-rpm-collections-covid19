def print_orf(start, stop):
    print(f"{start + 1:8} - {stop + 3:8}\tNucleotide Length: {stop + 3 - start:6}\tAmino Acid Length: {int((stop - start) / 3):8}")
