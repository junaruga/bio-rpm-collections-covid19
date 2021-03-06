#!/bin/bash

set -eux

# 1 China + 5 Japan
ACCESSIONS=(MN908947 LC528232 LC528233 LC529905 LC534418 LC534419)
if [ "${#}" -gt 0 ]; then
    ACCESSIONS=(${@})
fi
echo "${#ACCESSIONS[@]}"
echo "${ACCESSIONS[@]}"
mkdir -p out
# Use EFetch API to download the files.
# https://dataguide.nlm.nih.gov/eutilities/utilities.html#efetch
# https://www.ncbi.nlm.nih.gov/books/NBK25499/table/chapter4.T._valid_values_of__retmode_and/?report=objectonly
for ACCESSION in ${ACCESSIONS[@]}; do
    # Whole nucleotide sequence of the genome: .fna
    # FASTA (rettype: fasta, retmode: text)
    wget -O "out/$ACCESSION.fna" "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=$ACCESSION&rettype=fasta&retmode=text"
    sleep 1
    # Fasta sequence of coresponding nucleotide: .ffn
    # CDS nucleotide FASTA (rettype: fasta_cds_na, retmode: text)
    wget -O "out/$ACCESSION.ffn" "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=$ACCESSION&rettype=fasta_cds_na&retmode=text"
    sleep 1
    # Fasta sequence of amino acid: .faa
    # CDS protein FASTA (rettype: fasta_cds_aa, retmode: text)
    wget -O "out/$ACCESSION.faa" "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=$ACCESSION&rettype=fasta_cds_aa&retmode=text"
    sleep 1
    # GenBank record: .gbk
    # GenBank flat file with full sequence (contigs) (rettype: gbwithparts, retmode: text)
    wget -O "out/$ACCESSION.gbk" "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=$ACCESSION&rettype=gbwithparts&retmode=text"
    sleep 1
done
