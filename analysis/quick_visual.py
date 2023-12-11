import pandas as pd
import matplotlib.pyplot as plt

employment_df = pd.read_csv('data/cleaned-data/wa_employment_data.csv')
fuel_price_df = pd.read_csv('data/cleaned-data/perth_metro_fuel_prices.csv')

df = employment_df.merge(fuel_price_df, on=['Year', 'Month'])
df = df.drop(['Unnamed: 0_x', 'Unnamed: 0_y'], axis=1)

employment_and_price = list(zip(df['ULP Price'], df['Number of Employed People']))
employment_and_price.sort()

y = [val[1] for val in employment_and_price]
x = [val[0] for val in employment_and_price]

plt.figure()
plt.scatter(x, y)
plt.show()