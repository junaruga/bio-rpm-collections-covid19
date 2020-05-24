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
