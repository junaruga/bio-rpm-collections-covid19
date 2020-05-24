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
