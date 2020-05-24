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

Or use the API to download.
The downloaded file by API line break is dos format.
To use it on Linux environment, convert the line break (dos: `\r\n`) to (unix: `\n`).
See [this page](https://stackoverflow.com/questions/2613800/how-to-convert-dos-windows-newline-crlf-to-unix-newline-lf-in-a-bash-script#2613834) for detail to check the way to convert it.

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

$ python3 calc_gc_content.py
Total Count: 29903
GC Content: 37.97%
```

### Exercises

* SARS-related-coronavirus [AY27411.3]
* MERS-related-coronavirus [JX869059.2]
* Guandong Chinese water stink coronavirus [MG600026.1]
