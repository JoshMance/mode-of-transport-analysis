import requests
import pandas as pd

url = 'https://www.abs.gov.au/articles/50-years-capital-city-population-change'
html = requests.get(url).content
df_list = pd.read_html(html)
len(df_list)
df = df_list[-3]
print(df)
df.to_csv('my data.csv')