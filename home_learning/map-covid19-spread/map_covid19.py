import pandas as pd
import plotly.express as px

# Read the cvs file
df1 = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv", sep=",")

# Take a look to df1
print(df1.head())

# Using Plotly library to generate maps
fig = px.scatter_geo(df1, lat="Lat",lon="Long", size=((df1["4/5/20"])),
                     hover_name="Country/Region", color=(df1["4/5/20"])/1000,
                     projection="natural earth")
fig.show()
