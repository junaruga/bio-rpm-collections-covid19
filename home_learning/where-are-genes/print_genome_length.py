sars_cov_2_genome = ""
with open("sars_cov_2.fa") as f:
    sars_cov_2_genome = "".join([item.rstrip() for item in f if not item.startswith(">")])

print(len(sars_cov_2_genome))
