# Print slippery sequence positions.
# https://en.wikipedia.org/wiki/Slippery_sequence

sars_cov_2_genome = ""
with open("sars_cov_2.fa") as f:
    sars_cov_2_genome = "".join(
        [item.rstrip() for item in f if not item.startswith(">")]
    )

position = 0
while(True):
    position = sars_cov_2_genome.find("TTTAAAC", position)
    if position < 0:
        break
    position += 1
    print(position)
