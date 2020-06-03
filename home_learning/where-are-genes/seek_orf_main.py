import find_orf as fo

import find_triplet as ft

import print_orf as po

sars_cov_2_genome = ""
with open("sars_cov_2.fa") as f:
    sars_cov_2_genome = "".join(
        [item.rstrip() for item in f if not item.startswith(">")]
    )

start_codon = "ATG"
start_candidates = ft.retrieve_triplet_position(sars_cov_2_genome, start_codon)

stops = []
for stop_codon in ["TAG", "TAA", "TGA"]:
    stops.extend(ft.retrieve_triplet_position(sars_cov_2_genome, stop_codon))
stops.sort()

start_candidates_frame = [[]] * 3
stops_frame = [[]] * 3
for i in range(3):
    start_candidates_frame[i] = [
        item for item in start_candidates if item % 3 == i
    ]
    stops_frame[i] = [item for item in stops if item % 3 == i]

orf_list = []
for i in range(3):
    orf_list.extend(fo.seek_orf(start_candidates_frame[i], stops_frame[i]))
orf_list.sort()

print(f"{len(orf_list)} ORF candidates found.")
print("Start    - Stop Position")

for start, stop in orf_list:
    po.print_orf(start, stop)
