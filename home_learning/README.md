# Home Learning

This pages show the reproducing steps for [COVID-19 Biohackathon April 2020 - Home Learning](https://github.com/virtual-biohackathons/covid-19-bh20/wiki/Home-Learning).

## How to Map COVID-19 Spread?

### Tutorial

Generate maps by [the data made by Johns Hopkins University for the COVID-19 confirmed cases global](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv).

```
$ pip3 install -U --user pandas plotly
$ python3 map_covid19.py
```

### Exercises

Generate map by [the data for the COVID-19 deaths global](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv).

```
$ python3 map_covid19_exercises.py
```

## How to Download Sequences?

### Tutorial

Use [this data for SARS-CoV-2 first sequenced in Wuhan, China](https://www.ncbi.nlm.nih.gov/nuccore/MN908947) that was pointed out from [NCBI SARS-CoV-2 Sequences](https://www.ncbi.nlm.nih.gov/genbank/sars-cov-2-seqs).

To download the file by clicking "Send To", and select "Complete Record", "File - Format: FASTA", and click "Create File" button.

Save it as MN908947.3.fasta.

Or use EFetch API to download with the UNIX line break (`\n`).

```
$ wget -O MN908947.3.fasta "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=MN908947.3&rettype=fasta&retmode=text"
```

Or use the the following API to download with the DOS line break (`\r\n`).

If you want to convert the Dos to UNIX line break, you can use `sed` command. See [this page](https://stackoverflow.com/questions/2613800/how-to-convert-dos-windows-newline-crlf-to-unix-newline-lf-in-a-bash-script#2613834) for detail.

```
$ wget -O MN908947.3.fasta https://www.ncbi.nlm.nih.gov/search/api/sequence/MN908947.3/?report=fasta

$ sed -i.org $'s/\r$//' MN908947.3.fasta
```

```
$ head MN908947.3.fasta
```

Check the downloaded fasta file by the python script.

```
$ python3 check_download_data.py
Total Length: 29903
A: 8954 counts, Composition: 29.9%
T: 9594 counts, Composition: 32.1%
G: 5863 counts, Composition: 19.6%
C: 5492 counts, Composition: 18.4%
```

Run the following bash script to download files in `out` directory by specified accession IDs.

```
$ ./retrive_sequence.sh
```

### Exercises

Download the files by the specified accession IDs.

```
$ ./retrive_sequence.sh NC_045512 MT509512
```

## How to calculate GC content

Calculate GC content from the downloaded data `MN908947.3.fasta`.

```
$ python3 calc_gc_content.py
Total Count: 29903
GC Content: 37.97%
```

### Exercises

####  SARS-related-coronavirus [AY27411.3]

https://www.ncbi.nlm.nih.gov/nuccore/AY27411.3

```
$ wget -O AY27411.3.fasta "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AY27411.3&rettype=fasta&retmode=text"
...
2020-06-03 11:51:14 ERROR 400: Bad Request.
```

The data is not found.

####  MERS-related-coronavirus [JX869059.2]

https://www.ncbi.nlm.nih.gov/nuccore/JX869059.2

```
$ wget -O JX869059.2.fasta "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JX869059.2&rettype=fasta&retmode=text"

$ python3 calc_gc_content.py JX869059.2.fasta
Total Count: 30119
GC Content: 41.24%
```

#### Guandong Chinese water stink coronavirus [MG600026.1]

https://www.ncbi.nlm.nih.gov/nuccore/MG600026.1

```
$ wget -O MG600026.1.fasta "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=MG600026.1&rettype=fasta&retmode=text"

$ python3 calc_gc_content.py MG600026.1.fasta
Total Count: 22445
GC Content: 35.21%
```

## Where are Genes?

### Store the nucleotide sequence as a python string

```
$ wget -O sars_cov_2.fa "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=MN908947&rettype=fasta"

$ md5sum sars_cov_2.fa
2d67a6effebccc797fbd60f4b5659770  sars_cov_2.fa

$ python3 print_genome_length.py
29903
```

### Let's find the Open Reading Frame in the sequence

```
$ python3 find_triplet_test.py
test_seek_orf_exact_match (__main__.TestRetrieveTripletPosition) ... ok
test_seek_orf_exact_multiple_match (__main__.TestRetrieveTripletPosition) ... ok
test_seek_orf_no_match (__main__.TestRetrieveTripletPosition) ... ok
test_seek_orf_non_triplet (__main__.TestRetrieveTripletPosition) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

### How small the target protein is

TODO: What is this script doing?

```
$ python3 find_orf_test.py
test_seek_orf (__main__.TestSeekOrf) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

### Let's seek ORF

```
$ python3 seek_orf_main.py | wc -l
559

$ python3 seek_orf_main.py
557 ORF candidates found.
Start    - Stop Position
     107 -      136	Nucleotide Length:     30	Amino Acid Length:        9
     266 -    13483	Nucleotide Length:  13218	Amino Acid Length:     4405
     468 -      533	Nucleotide Length:     66	Amino Acid Length:       21
     489 -      533	Nucleotide Length:     45	Amino Acid Length:       14
     507 -      533	Nucleotide Length:     27	Amino Acid Length:        8
     518 -    13483	Nucleotide Length:  12966	Amino Acid Length:     4321
...
   29618 -    29674	Nucleotide Length:     57	Amino Acid Length:       18
   29771 -    29806	Nucleotide Length:     36	Amino Acid Length:       11
   29806 -    29844	Nucleotide Length:     39	Amino Acid Length:       12
```

### Let's see slippery sequence on the SARS-CoV-2 genome

```
$ python3 print_slippery_position.py 
1664
6085
6745
13462
16669
18475
20227
20817
24436
```

## How to Draw Phylogenetic Tree

Install Miniconda referring [the Miniconda](https://docs.conda.io/en/latest/miniconda.html) and [Installing in silient mode](https://docs.anaconda.com/anaconda/install/silent-mode/).

`/home/root/local/miniconda3-py38-4.8.3` is installed directory in my case.

```
$ wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.8.3-Linux-x86_64.sh
$ sudo mkdir /home/root/local/miniconda3-py38-4.8.3
$ sudo chown jaruga:jaruga /home/root/local/miniconda3-py38-4.8.3

$ bash Miniconda3-py38_4.8.3-Linux-x86_64.sh -b -u -p /home/root/local/miniconda3-py38-4.8.3
...
installation finished.
```

Note I recommend to skip the following step with `eval`, `conda init`, `conda config` commands, moving on `vi ~/.bashrc` step.

As I don't want `.bashrc` is modified by `conda init`, I reverted it.

```
$ eval "$(/home/root/local/miniconda3-py38-4.8.3/bin/conda shell.bash hook)"

(base) $ command -v conda
conda

(base) $ conda init
modified      /home/jaruga/.bashrc

(base) $ conda config --set auto_activate_base false
```

Add `conda`'s bin directory `PATH` with lower priority after the standard bin directories like this.

```
$ vi ~/.bashrc
...
PATH="${PATH}:/home/root/local/miniconda3-py38-4.8.3/bin"
...
export PATH

$ source ~/.bashrc
```

```
$ which conda
/home/root/local/miniconda3-py38-4.8.3/bin/conda

$ which python3
/usr/bin/python3

$ which python
/usr/bin/python
```

```
$ conda install -c bioconda -y mafft
$ conda install -c genomedk -y raxml-ng
```

```
$ conda list
# packages in environment at /home/root/local/miniconda3-py38-4.8.3:
#
# Name                    Version                   Build  Channel
...
mafft                     7.467                h516909a_0    bioconda
...
raxml-ng                  0.6.0                         0    genomedk
...

$ command -v mafft
/home/root/local/miniconda3-py38-4.8.3/bin/mafft

$ command -v raxml-ng
/home/root/local/miniconda3-py38-4.8.3/bin/raxml-ng
```

```
$ wget https://raw.githubusercontent.com/pitagora-network/home-learning/master/multi.fa
```

The following command creates `multi.aln` file.

```
$ mafft --leavegappyregion --auto multi.fa > multi.aln
```

The following command creates `multi.aln.raxml.*` files.

```
$ raxml-ng -msa multi.aln --all --model GTR+G --bs-trees 100
```

Upload `multi.aln.raxml.bestTree` file clicking "Upload a tree" button at https://itol.embl.de/ .

Then here is [the result](https://itol.embl.de/tree/94112133107179951592513704).
