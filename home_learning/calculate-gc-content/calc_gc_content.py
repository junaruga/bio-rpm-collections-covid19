import sys

fasta_file = "MN908947.3.fasta"
if len(sys.argv) > 1:
    fasta_file = sys.argv[1]

lines = open(fasta_file, 'r').readlines()[1:]

count = 0

for line in lines:
    line = line.rstrip()
    for x in line:
        count += 1

print("Total Count: " + str(count))

a = t = c = g = 0

for line in lines:
    for x in line:
        if x == "A":
            a += 1
        elif x == "T":
            t += 1
        elif x == "G":
            g += 1
        elif x == "C":
            c += 1

# GC content
# https://en.wikipedia.org/wiki/GC-content
gc_content = (g + c) / (a + t + g + c) * 100
print(f"GC Content: {gc_content:2.2f}%")
