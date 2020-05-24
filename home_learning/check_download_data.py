import os

item_list = []
with open("MN908947.3.fasta") as f:
    for data in f:
        if data.startswith(">"):
            continue  # Skip header

        item_list.append(data.rstrip())
sars_cov_2_sequence = "".join(item_list)
# print(sars_cov_2_sequence)

total_length = len(sars_cov_2_sequence)
print("Total Length: {}".format(total_length))

for base in ["A", "T", "G", "C"]:
    number = sars_cov_2_sequence.count(base)
    composition = sars_cov_2_sequence.count(base)/total_length
    print(f"{base}: {number} counts, Composition: {composition:2.1%}")
